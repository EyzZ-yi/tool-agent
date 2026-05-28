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

   ## 如何运行
   1. 安装依赖：`pip install -r requirements.txt`
   2. 在项目根目录创建 `.env` 文件，写入你的 DeepSeek API key：(DEEPSEEK_API_KEY=你的API)
   3. 打开 `demo.ipynb`，从上到下依次运行每个 cell