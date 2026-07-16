from datetime import datetime
from models import BaseMetadata, VideoMetadata, MediaFile
from storage import S3StorageProvider, LocalStorageProvider
from services import MediaManager, MediaProcessor

# 1. Инициализируем компоненты (например, выбираем S3 как облачное хранилище)
s3_storage = S3StorageProvider()
manager = MediaManager(storage=s3_storage)
processor = MediaProcessor(storage=s3_storage)

# 2. Создаем объект видеофайла и его метаданные
base_info = BaseMetadata(
    file_id="vid_1029",
    name="interview.mp4",
    size_bytes=104857600,
    created_at=datetime.now(),
    owner_id="user_42",
    extension="mp4"
)
video_meta = VideoMetadata(resolution="1920x1080", fps=60, duration_seconds=120.5, codec="h264")
my_video = MediaFile(base_info=base_info, specific_metadata=video_meta, storage_uri="s3://my-bucket/content/interview.mp4")

# 3. Демонстрация действий (CRUD + Бизнес-логика)
print("--- Выполнение операций ---")
# Создание (сохранение)
manager.create_file(my_video, content=b"raw_video_binary_data")

# Действие: Конвертация
new_path = processor.convert_video_format(my_video, target_format="avi")

# Обновление метаданных (например, поменялся кодек после конвертации)
new_video_meta = VideoMetadata(resolution="1920x1080", fps=60, duration_seconds=120.5, codec="mpeg4")
manager.update_metadata(my_video, new_video_meta)

# Удаление
manager.delete_file(my_video)

# 4. Попробуйте ответить на вопросы: много ли кода придется дописать / переписать при добавлении новых типов файлов и способов их хранения?

"""
 При добавлении нового типа файлов (например, 3D-модели):В models.py дописывается один класс Model3DMetadata.
Существующие классы MediaFile, BaseMetadata, а также менеджеры хранилищ остаются нетронутыми.
При добавлении нового способа хранения (например, Google Cloud Storage ):В storage.py создается новый класс (например, GoogleCloudStorageProvider), 
который наследуется от StorageProvider и реализует 3 его обязательных метода (read, save, delete).
В main.py мы просто заменяем S3StorageProvider() на GoogleCloudStorageProvider(). Весь остальной код (MediaManager, методы конвертации и логика пользователей)
продолжит работать автоматически, так как они завязаны на общий интерфейс.
"""