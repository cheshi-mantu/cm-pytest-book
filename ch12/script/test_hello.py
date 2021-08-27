import subprocess

def test_hello():
    command = ["python", "hello.py"]
    pipe = subprocess.run(command, stdout=subprocess.PIPE)
    output = pipe.stdout.decode('utf8')
    assert output == "Hello, World!\n"

