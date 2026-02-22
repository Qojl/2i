from TwoI import respond
import pytest

def test_hi():
    assert respond("Hi") == "Hello"

def test_hello():
    assert respond("Hello") == "Hi"

def test_error():
    with pytest.raises(ValueError):
        respond("Bye")
