from sqlalchemy import Column,Integer,String,Float,DateTime,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from app.yilai import engine

# 数据模型定义：用 sqlalchemy 定义主表 Memo（含 id 与业务字段）。
# 关系与约束：对关键字段添加类型与默认值约束（如时间字段默认当前时间）；
Base=declarative_base()

class Memo(Base):
    __tablename__='memo'
    id=Column(Integer,primary_key=True)
    title=Column(String(100),nullable=False)
    content=Column(String(100),nullable=False)
    time=Column(DateTime,default=datetime.now)

Base.metadata.create_all(engine)
