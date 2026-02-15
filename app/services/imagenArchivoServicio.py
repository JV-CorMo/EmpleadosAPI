from pathlib import Path
import shutil
import uuid

MEDIA_DIR = Path("app/media/empleados")
MEDIA_DIR.mkdir(parents=True, exist_ok=True)

class FileService:

    @staticmethod
    def save_employee_image(upload_file):
        extension = upload_file.filename.split(".")[-1]
        unique_name = f"{uuid.uuid4()}.{extension}"
        file_path = MEDIA_DIR / unique_name

        with file_path.open("wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)

        return f"/media/empleados/{unique_name}"