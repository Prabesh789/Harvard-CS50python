from hello import hello


def test_default():
    assert hello() == "Hello, world"


def test_arg():
    assert hello("Prabesh") == "Hello, Prabesh"


"""
we can do loop for testting strings but we will keep our testing simple and clear
def test_arg():
    for name in ["Prabesh", "David", "Ron"]:
        assert hello(name) == f"Hello, {name}"

        
"""
'''Inside the test folder create __init__.py file

This has the effect even if this file is empty, of telling the python to treat that floder not as not just a module but a package. 

A package is a Python module or multiple modules that are organized inside a folder. and a file __init__.py is an a visual indicator
to a python indeed it should treat the folder as a package. 
'''
