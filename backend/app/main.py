from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from app.config import settings
from app.database import init_db

logging.basicConfig(level=settings.LOG_LEVEL)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info('🚀 启动 AI Novel Studio')
    init_db()
    yield
    logger.info('🛑 关闭服务')

app = FastAPI(
    title=settings.API_TITLE,
    version=settings.API_VERSION,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get('/', tags=['健康检查'])
async def root():
    return {
        'message': '🎬 AI Novel Studio API',
        'version': settings.API_VERSION,
        'status': '✅ 运行中'
    }

@app.get('/health', tags=['健康检查'])
async def health():
    return {'status': 'healthy'}