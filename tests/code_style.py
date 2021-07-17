from pylint import epylint as lint

def code_style(file, total_points, rcfile='../../.pylintrc'):
    print("\n============================== Code Style Start ==============================")
    (pylint_stdout, pylint_stderr) = lint.py_run(f'{file} --rcfile {rcfile}', return_std=True)
    output = pylint_stdout.getvalue()
    points_off = len(output.split("\n")) - 2
    points_off = 0 if points_off < 0 else points_off
    code_style_points = 0 if points_off > total_points else total_points - points_off
    passed = points_off <= 0
    if passed:
        print("\nPASSED", f"+{total_points}")
    else:
        print("\nFAILED")
        print(output)
        print('-' + str(points_off))
    print(f"\n============================== Code Style End {code_style_points}/{total_points} ==============================")
    return code_style_points