from pathlib import Path
from  dotenv_stripout.stripout import strip_line, strip_file


def test_normal_line():
    input_line = "MY_SECRET_PASSWORD=IqLTLrFviwHTDKWGZoR7uB2JtM1wjwE34MBwoztE"
    expected_output_line = "MY_SECRET_PASSWORD="
    output_line = strip_line(input_line)
    assert output_line == expected_output_line


def test_line_without_value():
    input_line = "MY_SECRET_PASSWORD="
    expected_output_line = "MY_SECRET_PASSWORD="
    output_line = strip_line(input_line)
    assert output_line == expected_output_line


def test_line_without_equals():
    input_line = "MY_SECRET_PASSWORD"
    expected_output_line = "MY_SECRET_PASSWORD="
    output_line = strip_line(input_line)
    assert output_line == expected_output_line

def test_ignores_commented_line():
    input_line = "# THIS IS A COMMENT"
    output_line = strip_line(input_line)
    assert output_line == input_line

def test_ignores_empty_line():
    input_line = ""
    output_line = strip_line(input_line)
    assert output_line == ""

def test_ignores_line_with_only_whitespace():
    input_line = " "
    output_line = strip_line(input_line)
    assert output_line == ""

def test_ignores_line_with_only_whitespace_and_comment():
    input_line = " # THIS IS A COMMENT"
    expected_output_line = "# THIS IS A COMMENT"
    output_line = strip_line(input_line)
    assert output_line == expected_output_line

def test_handles_commented_line_in_a_file():
    test_file_path = Path(__file__).parent / "data" / ".env"
    copy_path = Path(__file__).parent / "data" / ".env.copy"
    copy_path.write_text(test_file_path.read_text())
    strip_file(copy_path)
    with copy_path.open("r") as f:
        lines = f.readlines()
    copy_path.unlink()
    assert lines[0] == "# THIS IS A COMMENT\n"
