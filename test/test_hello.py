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
