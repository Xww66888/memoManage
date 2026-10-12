from fastapi import APIRouter,Depends,HTTPException
from app.models import Memo
from app.pydantic import MemoCreate,MemoUpdate,MemoRead
from app.yilai import get_db,settings
from sqlalchemy.orm import sessionmaker, Session,joinedload

# 将 Memo 业务逻辑封装为 MemoService 类（体现封装）
class MemoService:
    @staticmethod
    def get_m( db:Session=Depends(get_db),page:int=1,size:int=10):
        offset=(page-1)*size
        m=db.query(Memo).offset(offset).limit(size).all()
        return m
    @staticmethod
    def add_m(memo:MemoCreate,db:Session=Depends(get_db)):
        m=Memo(**memo.model_dump())
        db.add(m)
        db.commit()
        db.refresh(m)
        return m
    @staticmethod
    def update_m(id:int,memo:MemoUpdate,db:Session=Depends(get_db)):
        m=db.query(Memo).get(id)
        if not m:
            raise HTTPException(status_code=404,detail="备忘录不存在")
        for k,v in memo.model_dump().items():
            setattr(m,k,v)
        db.commit()
        db.refresh(m)
        return m
    @staticmethod
    def delete_m(id:int,db:Session=Depends(get_db)):
        m=db.query(Memo).get(id)
        if not m:
            raise HTTPException(status_code=404,detail="备忘录不存在")
        db.delete(m)
        db.commit()
        return {"msg":"删除成功"}
    @staticmethod
    def get_m_id(id:int,db:Session=Depends(get_db)):
        m=db.query(Memo).get(id)
        if not m:
            raise HTTPException(status_code=404,detail="备忘录不存在")
        return m
    