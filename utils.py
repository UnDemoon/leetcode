'''
    工具集
'''


def loadFile(file: str) -> str:
    with open(file, 'r', ) as f:
        res = f.read()
    return res
