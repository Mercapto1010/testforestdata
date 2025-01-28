# Multiprocessing using Processpool executor

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(num):
    time.sleep(1)
    return f"Square: {num*num}"

num = [1,2,3,4,5,6,7,8,9,10,11,12,13]

if __name__ == '__main__':

    with ProcessPoolExecutor(max_workers= 3) as executor:
        results = executor.map(square_number,num)

    for result in results:
        print(result)
