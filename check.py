from pathlib import Path
ns = {}
exec(compile(Path('calc.py').read_text(), 'calc.py', 'exec'), ns)
for n in (0, 1, 7, 20):
    assert ns['total'](n) == 2 * n + ns['STUDENT_NUMBER']
print('OK')
