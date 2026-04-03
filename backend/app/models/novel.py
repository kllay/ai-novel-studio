from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as PyEnum
from app.database import Base

class NovelStatus(str, PyEnum):
    DRAFT = 'draft'
    OUTLINE = 'outline'
    WRITING = 'writing'
    FINISHED = 'finished'

class Novel(Base):
    __tablename__ = 'novels'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    theme = Column(String(255), comment='选题关键词')
    genre = Column(String(100), comment='类型')
    
    outline_level = Column(String(50), comment='粗纲/细纲')
    outline_content = Column(Text, comment='纲内容')
    full_content = Column(Text, comment='完整正文')
    
    word_count = Column(Integer, default=0)
    chapter_count = Column(Integer, default=0)
    status = Column(Enum(NovelStatus), default=NovelStatus.DRAFT)
    
    metadata = Column(JSON)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    ai_logs = relationship('AILog', back_populates='novel', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Novel {self.title}>'

class AILog(Base):
    __tablename__ = 'ai_logs'
    
    id = Column(Integer, primary_key=True, index=True)
    novel_id = Column(Integer, ForeignKey('novels.id'))
    task_type = Column(String(50), comment='任务类型')
    prompt = Column(Text, comment='提示词')
    response = Column(Text, comment='回复')
    model_used = Column(String(100), comment='使用的模型')
    tokens_used = Column(Integer, comment='消耗token数')
    
    created_at = Column(DateTime, default=datetime.utcnow)
    novel = relationship('Novel', back_populates='ai_logs')