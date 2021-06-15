from pylint import epylint as lint

def code_style(file, rcfile='../../.pylintrc'):
    print("\n---------------------------- Code Style ----------------------------")
    (pylint_stdout, pylint_stderr) = lint.py_run(f'{file} --rcfile {rcfile}', return_std=True)
    output = pylint_stdout.getvalue()
    return (output, len(output.split("\n")) - 2)