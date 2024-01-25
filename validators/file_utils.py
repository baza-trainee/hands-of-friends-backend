import os
from django.db.models.fields.files import FieldFile


class FileUtility:
    """Utility class for file-related operations."""

    @staticmethod
    def get_file_extension(file_name: str) -> str:
        """Extract the file extension from the file name."""
        return file_name.rsplit(".", 1)[-1].lower()

    @staticmethod
    def get_file_size(file: FieldFile) -> int:
        """Get the size of the file."""
        if hasattr(file, "temporary_file_path"):
            return os.path.getsize(file.temporary_file_path())
        else:
            file.seek(0, os.SEEK_END)
            file_size = file.tell()
            file.seek(0)
            return file_size
