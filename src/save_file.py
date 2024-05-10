# src/save_file.pdf

import tempfile
import shutil


def save_file(file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        # Write the uploaded PDF to the temporary file
        shutil.copyfileobj(file, tmp_file)
        tmp_file_path = tmp_file.name  # Get the path to the temporary file
        return tmp_file_path
