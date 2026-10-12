from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

# 配置依赖注入：实现 get_settings 依赖，在接口中注入配置（如应用标题）。
class Settings(BaseSettings):
    DATABASE_URL:str
    APP_TITLE:str
    class Config:
        env_file=".env"

settings=Settings()

# 数据库引擎与依赖：创建 sqlalchemy 引擎，实现 get_db 会话依赖注入供接口使用
engine=create_engine(settings.DATABASE_URL)
Sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db():
    db=Sessionlocal()
    try:
        yield db
    finally:
        db.close()