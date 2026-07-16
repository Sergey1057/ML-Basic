from models import MediaFile
from storage import StorageProvider

class MediaManager:
    """Сервис для CRUD операций над медиа-файлами."""
    def __init__(self, storage: StorageProvider):
        self.storage = storage  # Работаем с абстракцией, а не с конкретным хранилищем

    def create_file(self, media_file: MediaFile, content: bytes) -> None:
        """Создать файл в системе и сохранить в хранилище."""
        self.storage.save(media_file.storage_uri, content)
        print(f"Метаданные файла {media_file.base_info.name} записаны в БД.")

    def update_metadata(self, media_file: MediaFile, new_metadata: Any) -> MediaFile:
        """Обновить специфичные метаданные файла."""
        media_file.specific_metadata = new_metadata
        print(f"Метаданные файла {media_file.base_info.file_id} обновлены в БД.")
        return media_file

    def delete_file(self, media_file: MediaFile) -> None:
        """Удалить файл из хранилища и записи о нем."""
        self.storage.delete(media_file.storage_uri)
        print(f"Запись о файле {media_file.base_info.file_id} удалена из БД.")


class MediaProcessor:
    """Сервис для тяжелых операций (конвертация, ИИ-фичи)."""
    def __init__(self, storage: StorageProvider):
        self.storage = storage

    def convert_video_format(self, media_file: MediaFile, target_format: str) -> str:
        """Конвертирует видео. Возвращает новый URI."""
        file_bytes = self.storage.read(media_file.storage_uri)
        print(f"Декодирование видео через ffmpeg, изменение формата на {target_format}...")
        new_uri = media_file.storage_uri.replace(media_file.base_info.extension, target_format)
        self.storage.save(new_uri, b"converted_video_data")
        return new_uri

    def extract_audio_features(self, media_file: MediaFile) -> list:
        """Извлечение признаков ."""
        file_bytes = self.storage.read(media_file.storage_uri)
        return [0.12, 0.95, 0.01]  # Пример 
