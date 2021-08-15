from .stripout import list_dotenv_file_paths, strip_file

for file in list_dotenv_file_paths():
    strip_file(file)
