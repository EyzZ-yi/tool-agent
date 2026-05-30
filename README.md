# Weather Agent + RAG

一个基于 LLM Tool Calling 和 RAG(检索增强生成)的个人 AI 助手。
具备公共信息查询(天气、时间)和个人笔记智能检索能力,提供流式聊天界面。

## 核心能力

- 🌤️ **公共信息查询**:天气、当地时间(可扩展更多工具)
- 📓 **个人笔记智能检索**:基于向量检索的 RAG,在私人笔记库中找答案
- 🤖 **智能工具选择**:LLM 自主判断何时调用哪个工具,何时直接回答
- ⚡ **并行工具调用**:一次提问可同时触发多个工具(如"杭州天气 + 我的笔记")
- 💬 **流式输出**:回答逐字显示,接近 ChatGPT 体验
- 💾 **磁盘缓存**:向量库本地持久化,启动 0 秒、0 调用成本

## 技术架构
┌──────────────────────────────────┐
│  app.py(Streamlit 界面层)       │
│  - 聊天 UI、对话历史、流式渲染     │
└────────────┬─────────────────────┘
 from agent import run_agent
             |
             ▼
┌──────────────────────────────────┐
│  agent.py(业务逻辑层)            │
│  - run_agent: tool calling 循环   │
│  - 双路径处理(用工具/直接答)     │
│  - RAG 检索逻辑                   │
└────────────┬─────────────────────┘
             │
       ┌─────┴──────┐
       ▼            ▼
   工具实现层        向量库层
  (get_weather    (notes.py +
  / get_time /    knowledge_base.pkl)
  search_notes)


**分层设计**:界面层独立于业务逻辑,改前端或换后端互不影响。

## 技术栈

- **Python 3.12**
- **Streamlit**:Web 界面 + 流式渲染
- **DeepSeek API**:Chat 模型(`deepseek-chat`),负责对话和工具决策
- **通义千问 API**:Embedding 模型(`text-embedding-v3`),负责语义检索
- **numpy**:余弦相似度计算
- **OpenAI SDK**:统一兼容多家 LLM API

## 关键工程实现

### 1. Tool Calling 双路径处理

LLM 可能选择调工具(Path A),也可能直接回答(Path B):

```python
if assistant_message.tool_calls:
    # Path A:执行工具 → 把结果塞回 messages → 第二次调用 LLM 生成回答
    for tc in assistant_message.tool_calls:
        result = function_registry[tc.function.name](**args)
        messages.append({"role": "tool", "content": result, ...})
    final_resp = chat_client.chat.completions.create(...)
    return final_resp.choices[0].message.content
else:
    # Path B:直接返回 LLM 自身回答
    return assistant_message.content
```

### 2. Function Registry 模式

新增工具只需改一行,无需修改循环逻辑:

```python
function_registry = {
    "get_time": get_time,
    "get_weather": get_weather,
    "search_my_notes": search_my_notes,
}
result = function_registry[function_name](**function_args)
```

### 3. RAG 检索流程
用户问题 → embedding 化 → 与笔记库余弦相似度比较 → Top-K 召回 → 喂给 LLM 生成回答
阈值过滤(score < 0.3 直接返回"未找到"),避免 LLM 基于低质量召回胡编。

### 4. 向量库磁盘缓存

首次启动调用 embedding API 构建,之后从 `knowledge_base.pkl` 读取,
避免每次启动重新调用、节省 API 费用。

## 行为观察(亲手实验得出)

| 测试用例 | LLM 行为 | 工程含义 |
|---------|---------|---------|
| "我增肌早餐吃什么" | 调用 search_my_notes,精确返回 | RAG 在私人知识场景下最有效 |
| "巴黎天气" | 调用 get_weather → 工具返回 error → LLM 不绕过工具瞎编 | Grounding(工具约束)生效 |
| "巴黎是哪国首都" | 不调任何工具,直接回答 | LLM 自主判断"稳定常识"无需查询 |
| "杭州几点 + 笔记里有什么 X" | 并行返回 2 个 tool_calls | LLM 自主任务分解能力 |
| "我增肌训练怎么练" | 综合多段笔记,生成个性化方案 | RAG + LLM 推理协同价值 |

## 项目结构
weather_agent/
├── app.py              # Streamlit 界面
├── agent.py            # Agent 业务逻辑
├── notes.py            # 个人笔记数据(私有,不入 git)
├── knowledge_base.pkl  # 向量库缓存(自动生成,不入 git)
├── requirements.txt    # 依赖清单
├── .env                # API key(不入 git)
└── README.md

## 快速开始

### 1. Clone 项目

```bash
git clone https://github.com/EyzZ-yi/tool-agent.git
cd tool-agent
```

### 2. 创建虚拟环境并装依赖

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. 配置 API key

新建 `.env` 文件:
DEEPSEEK_API_KEY=sk-你的-deepseek-key
DASHSCOPE_API_KEY=sk-你的-通义千问-key

申请地址:
- DeepSeek: https://platform.deepseek.com
- 通义千问: https://dashscope.console.aliyun.com

### 4. 准备笔记数据

创建 `notes.py`,内容为一个字符串列表:

```python
notes = [
    "你的第一段笔记...",
    "你的第二段笔记...",
    # ...
]
```

### 5. 运行

```bash
streamlit run app.py
```

浏览器自动打开 `http://localhost:8501`。

## 开发心得

### 关于 LLM 应用的"概率本质"

LLM 的工具选择不是关键词匹配,而是基于语义意图的概率判断。
同样的关键词、不同句式,行为可能完全不同。
例如:
- "给我迪杰斯特拉的模板" → 调 search_my_notes(取个人数据)
- "迪杰斯特拉是什么" → 不调工具(查通用知识)

工程师的工作是用 prompt 和 tool description 让概率向期望方向倾斜,
而非追求 100% 确定性。

### 关于 RAG 的能力边界

Embedding 编码的是"主题",不是"事实"。
所以 RAG 会出现:
- 主题相关但事实无关的内容被召回(如"巴黎旅游"被问"巴黎天气"召回)
- 反义语义无法区分(开心 vs 难过 余弦相似度可能 0.7+)

工程上需要:
- 阈值过滤(分数太低直接放弃)
- 把相关度返回给 LLM,让它感知召回质量
- 必要时上 rerank(二次精排)

## TODO

- [ ] Path B 真正流式(目前为伪流式,需要更复杂的 tool_calls 累积处理)
- [ ] 工具描述精细化,降低"灰色地带"问题选错工具的概率
- [ ] 加更多工具(计算器、当前日期、网页 fetch)
- [ ] 支持笔记动态导入(从 Markdown / PDF 文件)
- [ ] 部署到云端(Streamlit Cloud / Vercel)

## 开发时间线

- 5/27-5/29:完成 Tool Calling 基础 + RAG 检索 demo(在 demo.ipynb)
- 5/30:整合为 Web 应用,加入流式输出、磁盘缓存,完成项目化重构

## License

MIT