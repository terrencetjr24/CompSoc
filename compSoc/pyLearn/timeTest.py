import time

def calcProd():
    prod = 1
    for i in range(1,400000):
        prod = prod * i;
    return prod
def misc():
    startTim = time.time()
    prod = calcProd()
    endTim = time.time()

    print(f"The result is {len(str(prod))} digits long")
    print(f"The calculation took %d {endTim - startTim}")

def new():
    for i in range(3):
        print("tick")
        time.sleep(1)
        print('tock')
        time.sleep(1)
    
if __name__ == '__main__':
    new()
