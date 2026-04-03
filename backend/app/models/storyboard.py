from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, JSON, Float
from datetime import datetime
from app.database import Base

class Storyboard(Base):
    __tablename__ = 'storyboards'
    
    id = Column(Integer, primary_key=True, index=True)
    scene_id = Column(Integer, nullable=False)
    
    frame_number = Column(Integer)
    title = Column(String(255))
    description = Column(Text)
    
    static_image_path = Column(String(500))
    first_frame_path = Column(String(500))
    last_frame_path = Column(String(500))
    
    animation_type = Column(String(100))
    animation_params = Column(JSON)
    duration = Column(Float, default=2.0)
    
    generation_params = Column(JSON)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Storyboard {self.frame_number}>'