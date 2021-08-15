from subprocess import check_output


def run_command(command):
    return check_output(command.split(), text=True).strip()
