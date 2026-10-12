from fastapi import APIRouter,Depends,HTTPException
from app.models import Memo
from app.pydantic import MemoCreate,MemoUpdate,MemoRead
from app.yilai import get_db,settings
from sqlalchemy.orm import sessionmaker, Session,joinedload
from app.service import MemoService

router=APIRouter(prefix='/memo')
# 列表接口：GET 返回分页列表
@router.get('/list')
def get_list(
    db:Session=Depends(get_db),
    page:int=1,
    size:int=10
):
    return MemoService.get_m(db,page,size)

# 新增接口：POST 创建 Memo，返回响应模型，状态码 201
@router.post('/add',response_model=MemoRead,status_code=201)
def add_memo(
    memo:MemoCreate,
    db:Session=Depends(get_db)
):
    return MemoService.add_m(memo,db)

# 更新接口：PUT 更新 Memo 数据
@router.put('/update/{id}',response_model=MemoRead)
def update_memo(
    id:int,
    memo:MemoUpdate,
    db:Session=Depends(get_db)
):
    return MemoService.update_m(id,memo,db)

# 删除接口：DELETE 删除数据，无效 ID 返回 404。
@router.delete('/delete/{id}')
def delete_memo(
    id:int,
    db:Session=Depends(get_db)
):
    return MemoService.delete_m(id,db)

# 更新接口：PUT 更新 Memo 数据。
@router.get('/{id}')
def get_mid(
    id:int,
    db:Session=Depends(get_db)
):
    return MemoService.get_m_id(id,db)
    