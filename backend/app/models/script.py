from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as PyEnum
from app.database import Base

class ScriptStatus(str, PyEnum):
    DRAFT = 'draft'
    REVIEWING = 'reviewing'
    APPROVED = 'approved'

class Script(Base):
    __tablename__ = 'scripts'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    novel_id = Column(Integer, ForeignKey('novels.id'), nullable=True)
    
    title = Column(String(255), nullable=False)
    description = Column(Text)
    content = Column(Text)
    
    scene_count = Column(Integer, default=0)
    character_count = Column(Integer, default=0)
    status = Column(Enum(ScriptStatus), default=ScriptStatus.DRAFT)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Script {self.title}>'