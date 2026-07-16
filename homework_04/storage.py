from abc import ABC, abstractmethod
from models import MediaFile

class StorageProvider(ABC):
    """Абстрактный класс для работы с любым типом хранилища."""
    
    @abstractmethod
    def read(self, storage_uri: str) -> bytes:
        """Чтение бинарных данных файла из хранилища."""
        pass

    @abstractmethod
    def save(self, storage_uri: str, content: bytes) -> None:
        """Сохранение бинарных данных в хранилище."""
        pass

    @abstractmethod
    def delete(self, storage_uri: str) -> None:
        """Удаление файла из хранилища."""
        pass


class LocalStorageProvider(StorageProvider):
    """Реализация для локального диска."""
    def read(self, storage_uri: str) -> bytes:
        return b"local_file_data"

    def save(self, storage_uri: str, content: bytes) -> None:
        print(f"Файл успешно сохранен на локальный диск: {storage_uri}")

    def delete(self, storage_uri: str) -> None:
        print(f"Файл удален с локального диска: {storage_uri}")


class S3StorageProvider(StorageProvider):
    """Реализация для S3-like хранилищ (AWS, MinIO, Yandex Cloud)."""
    def read(self, storage_uri: str) -> bytes:
        return b"s3_file_data"

    def save(self, storage_uri: str, content: bytes) -> None:
        print(f"Файл успешно загружен в S3: {storage_uri}")

    def delete(self, storage_uri: str) -> None:
        print(f"Файл удален из S3: {storage_uri}")
