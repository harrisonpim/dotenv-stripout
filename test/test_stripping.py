from dotenv_stripout.stripout import strip_line


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
