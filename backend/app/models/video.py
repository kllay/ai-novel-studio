from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, ForeignKey, JSON
from datetime import datetime
from enum import Enum as PyEnum
from app.database import Base

class VideoStatus(str, PyEnum):
    PENDING = 'pending'
    PROCESSING = 'processing'
    COMPLETED = 'completed'
    FAILED = 'failed'

class Video(Base):
    __tablename__ = 'videos'
    
    id = Column(Integer, primary_key=True, index=True)
    script_id = Column(Integer, ForeignKey('scripts.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    title = Column(String(255), nullable=False)
    description = Column(Text)
    
    video_path = Column(String(500))
    thumbnail_path = Column(String(500))
    
    duration = Column(Integer)
    file_size = Column(Integer)
    resolution = Column(String(50))
    
    generation_params = Column(JSON)
    status = Column(Enum(VideoStatus), default=VideoStatus.PENDING)
    error_message = Column(Text)
    progress = Column(Integer, default=0)
    
    capcut_draft = Column(JSON)
    capcut_export_path = Column(String(500))
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Video {self.title}>'