import random

def genHiHello() -> str:
    return ["Hi","Hello"][random.randint(0,1)]

def respond(msg: str) -> str:
    """
    HiHelloライブラリの応答関数
    """
    msg = msg.strip()
    if msg == "Hi":
        return "Hello"
    elif msg == "Hello":
        return "Hi"
    else:
        raise ValueError(f"Unsupported message: {msg}")

def show():
    print("Hello,World!")
    
def kasosuta():
    print("kasosuta Good")
    
