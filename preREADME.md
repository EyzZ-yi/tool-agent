# Weather Agent Demo
   
   我的第一个 AI 工程项目：使用 DeepSeek API 实现的 tool calling agent，
   支持查询多个城市的天气和时间。
   
   ## 技术栈
   - Python 3.12
   - DeepSeek API (OpenAI 兼容)
   - Jupyter Notebook
   
   ## 实现的核心功能
   - 单工具调用
   - 多工具并行调用
   - Function registry 模式
   
   ## 我的学习心得
   - LLM只负责决策，函数负责执行
   - tool的工作流程
   [user message] + [tools 描述]
        ↓
   第一次 API 调用
        ↓
   模型决策：需要调 tool
        ↓ 
   模型返回 assistant_message
  （content 为空，tool_calls 有 N 个）
        ↓
   将这条 assistant_message 整条 append 到 messages
  （保存"模型想调什么"的记录）
        ↓
   for 循环：执行每一个 tool_call
        ↓
   每执行一个工具，把结果以 tool message 形式
   append 到 messages
  （必须带 tool_call_id 对应）
        ↓
   第二次 API 调用
        ↓
   模型看到所有 tool 结果
        ↓
   生成最终自然语言回答
        ↓
   返回给用户

## v2 更新:RAG 知识检索 + 个性化建议

新增 `search_my_notes` 工具,基于 embedding + 余弦相似度检索个人笔记。
现在 agent 能基于个人数据(健身记录、电脑配置、学习笔记)给出个性化回答。

### 能力示例
- "我增肌早餐吃什么?" → 基于个人饮食计划返回精确数据
- "我电脑什么配置?" → 完整复述硬件清单 + 价格
- "能不能安排一周健身计划?" → **基于个人训练记录和目标,生成个性化方案**
- "杭州几点 + 我笔记里 X" → 并行调用 2 个工具
- "巴黎首都?" → 不调工具,直接基于 LLM 知识回答

### 技术亮点
- Function registry 模式:加新工具只改一行
- 双路径处理:LLM 决定调工具(Path A) / 直接回答(Path B)
- 检索质量信号:把相关度分数返回给 LLM,让它感知召回质量

## 如何运行
1. 安装依赖：`pip install -r requirements.txt`
2. 在项目根目录创建 `.env` 文件，写入你的 DeepSeek API key：(DEEPSEEK_API_KEY=你的API)
3. 在 `notes.py` 里替换成你自己的数据
4. 打开 `demo.ipynb`，从上到下依次运行每个 cell
