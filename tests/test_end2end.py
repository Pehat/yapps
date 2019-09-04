import subprocess

def test_end2end():
    retcode = subprocess.call(["yapps2", "examples/expr.g", "examples/expr.py"])
    assert retcode == 0
    p = subprocess.Popen(
        ["python", "examples/expr.py", "goal"],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE
    )
    p_stdout, p_stderr = p.communicate(b"1+2*3+4")
    assert p_stdout == b"11\n"
