from pathlib import Path

from dotenv_stripout.stripout import list_dotenv_file_paths

data_dir = Path(__file__).parent / "data"
names_to_match = [".env", ".env.something", "something.env.something"]
names_to_not_match = [".environment"]
directories = [data_dir, data_dir / "subdir", data_dir / "subdir" / "subsubdir"]
paths_to_match = [dir / name for dir in directories for name in names_to_match]
paths_to_not_match = [
    dir / name for dir in directories for name in names_to_not_match
]

found_paths = set(list_dotenv_file_paths())


def test_all_correct_paths_found():
    for path in paths_to_match:
        assert path in found_paths


def test_no_incorrect_paths_found():
    for path in paths_to_not_match:
        assert path not in found_paths
