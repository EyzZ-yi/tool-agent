import os
from dotenv import load_dotenv
from openai import OpenAI
import numpy as np
import json

load_dotenv()

#Embedding ues alibaba
embedding_client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# Chatting use DeepSeek
chat_client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

#初始化向量库
# def build_knowledge_base():
#     all_vectors=[]
#     for i in range(0,len(notes),10) :
#         mind=notes[i:i+10]
#         resp=embedding_client.embeddings.create(
#             model="text-embedding-v3",
#             input=mind
#         )
#         all_vectors.extend(item.embedding for item in resp.data)
#     kb=[]
#     for i in range(len(notes)) :
#         kb.append({
#             "text": notes[i],
#             "vector": all_vectors[i]
#         })
#     return kb

# 优化构建向量库
import pickle
from notes import notes
def build_knowledge_base():
    cache_file = "knowledge_base.pkl"
    
    # 如果磁盘上已经有缓存,直接读
    if os.path.exists(cache_file):
        print("从磁盘加载向量库...")
        with open(cache_file, "rb") as f:
            return pickle.load(f)
    
    # 没缓存,才调 API
    print(f"第一次构建向量库,共 {len(notes)} 段笔记...")
    all_vectors = []
    for i in range(0, len(notes), 10):
        batch = notes[i:i+10]
        resp = embedding_client.embeddings.create(
            model="text-embedding-v3",
            input=batch
        )
        all_vectors.extend(item.embedding for item in resp.data)
    
    kb = []
    for i in range(len(notes)):
        kb.append({
            "text": notes[i],
            "vector": all_vectors[i]
        })
    
    # 存到磁盘
    with open(cache_file, "wb") as f:
        pickle.dump(kb, f)
    print("向量库已缓存到磁盘")
    return kb

knowledge_base = build_knowledge_base()

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "查询指定城市的当前天气信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市名称，例如 北京、上海、杭州"
                    }
                },
                "required": ["city"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_time",
            "description": "查询指定城市当地的时间",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市名称，例如 北京、上海、杭州"
                    }
                },
                "required": ["city"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_my_notes",
            "description": "在用户的个人笔记库中检索相关内容。适用于:用户询问自己的健身计划、电脑配置、学习笔记、个人记录等私人信息时使用。如果是天气、时间这类公共信息查询,不要用这个工具。",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "要在笔记中搜索的内容,应该是用户问题的核心关键词,例如 '增肌早餐'、'电脑配置'、'RAG 流程'"
                    }
                },
                "required": ["query"]
            }
        }
    }
]

def get_weather(city: str) -> str:
    fake_data = {
        "北京": {"temp": 18, "condition": "晴"},
        "上海": {"temp": 22, "condition": "小雨"},
        "杭州": {"temp": 20, "condition": "多云"},
    }
    if city in fake_data:
        return json.dumps(fake_data[city], ensure_ascii=False)
    else:
        return json.dumps({"error": f"没有 {city} 的数据"}, ensure_ascii=False)


def get_time(city: str) -> str:
    fake_times = {
        "北京": "14:30",
        "上海": "14:30",
        "杭州": "14:30",
        "纽约": "02:30",
    }
    return json.dumps({"time": fake_times.get(city, "未知")}, ensure_ascii=False)


def search_my_notes(query :str) -> str:
    relevant_notes=retrieve(query, top_k=3)
    if not relevant_notes or relevant_notes[0]["score"]<0.3 :
        return "没找到相关笔记内容"
    result=""
    for i, r in enumerate(relevant_notes) :
        result+=f"第{i+1}个笔记的相关度为:{r['score']}\n内容为:{r['text']}\n\n"
    return result.strip()

#serach_my_notes的辅助函数
def cosine_similarity(v1, v2):
    """算两个向量的余弦相似度"""
    v1 = np.array(v1)
    v2 = np.array(v2)
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def retrieve(query: str, top_k: int = 3) ->list:
    """
    根据用户问题,从知识库找最相关的 top_k 条
    返回:[{text, score}, ...]
    """
    # 1.用户问题也embedding化
    resp=embedding_client.embeddings.create(
        model="text-embedding-v3",
        input=query
    )
    query_vector = resp.data[0].embedding
    # 2. 算 query 和每条笔记的相似度
    scored_notes=[]
    for item in knowledge_base:
        score=cosine_similarity(query_vector,item["vector"])
        scored_notes.append({
            "text":item["text"],
            "score":score
        })
    scored_notes.sort(key=lambda x: x["score"], reverse=True)
    return scored_notes[:top_k]




#agent流程
def run_agent(question) :
    messages = [
        {"role": "user", "content": question}
    ]
    #第一次API调用
    resp = chat_client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        tools=tools
    )
    #将LLM返回的调用工具请求添加到LLM的“记忆”中
    assistant_message=resp.choices[0].message
    messages.append(assistant_message)
    #创造一个工具对照表，快速查询获得工具
    function_registry = {
        "get_time" : get_time ,
        "get_weather" : get_weather,
        "search_my_notes": search_my_notes
    }
    if assistant_message.tool_calls :
        #将LLM需要的工具依次添加到他的“记忆”里
        for tc in resp.choices[0].message.tool_calls:
            tool_call = tc
            function_name = tc.function.name
            function_args = json.loads(tc.function.arguments)
            messages.append({
            "role": "tool",
            "tool_call_id": tc.id,
            "content": function_registry[function_name](**function_args)
            
        })
        #第二次API调用，LLM给出答案
        final_resp = chat_client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            tools=tools,
            stream=True
        )
        # 持续 yield 每个 chunk 的文本片段,流式输出
        for chunk in final_resp:
            content = chunk.choices[0].delta.content
            if content:
                yield content
        #return final_resp.choices[0].message.content
    else :
        #return assistant_message.content 
        # Path B:LLM 没调工具,直接答
        # 这里 assistant_message.content 已经是完整字符串了
        # 我们模拟流式,一个字一个字 yield 出去(虽然没真的流式)
        # 或者直接 yield 一次完整字符串也行
        yield assistant_message.content
#函数从"返回字符串"变成了"生成器"