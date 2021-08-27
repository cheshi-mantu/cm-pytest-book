import hello

def test_main(capsys):
    hello.main()
    output, _ = capsys.readouterr()
    assert output == "Hello, World!\n"