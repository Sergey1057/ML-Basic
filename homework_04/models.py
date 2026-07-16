from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, Dict, Any

@dataclass
class BaseMetadata:
    """Общие метаданные для всех типов файлов."""
    file_id: str
    name: str
    size_bytes: int
    created_at: datetime
    owner_id: str
    extension: str

@dataclass
class AudioMetadata:
    """Специфичные метаданные для аудио."""
    bitrate: int
    duration_seconds: float
    codec: str
    artist: Optional[str] = None

@dataclass
class VideoMetadata:
    """Специфичные метаданные для видео."""
    resolution: str  # например, "1920x1080"
    fps: int
    duration_seconds: float
    codec: str

@dataclass
class PhotoMetadata:
    """Специфичные метаданные для фото."""
    resolution: str
    color_space: str  # например, "RGB"
    has_alpha: bool

@dataclass
class MediaFile:
    """Основной класс медиа-файла, объединяющий базу и специфичные метаданные."""
    base_info: BaseMetadata
    # Сюда передается один из классов метаданных (AudioMetadata, VideoMetadata и т.д.)
    specific_metadata: Any  
    # Ссылка на местоположение (URI), например: "s3://bucket/video.mp4" или "/local/path/photo.png"
    storage_uri: str  
