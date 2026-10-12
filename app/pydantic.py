from pydantic import BaseModel
from datetime import datetime

# Pydantic 请求模型：定义 MemoCreate 用于接收新增数据
class MemoCreate(BaseModel):
    title:str
    content:str

# Pydantic 请求模型：定义 MemoUpdate 用于接收更新数据
class MemoUpdate(BaseModel):
    title:str
    content:str

# Pydantic 响应模型：定义 MemoRead 并作为接口 response_model 约束返回字段。\
class MemoRead(BaseModel):
    id:int
    title:str
    content:str
    time:datetime