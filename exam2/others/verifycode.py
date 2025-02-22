import random

def verifycode(n,length=2):
    vc = random.randint(0,10)
    if vc > length:
        return 1
    return vc + verifycode(i)

for i in range(6):
    print(verifycode(i,6),end='')