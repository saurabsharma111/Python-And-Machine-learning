#multiprocessing with thread pool executor
from concurrent.futures import ProcessPoolExecutor
import time
# Create a ThreadPoolExecutor with 5 worker threads
def printnum(num):
    time.sleep(1)
    return f"Number:{num}"

num=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]

t=time.time()

with ProcessPoolExecutor(max_workers=3) as executor:
    results= executor.map(printnum,num)

for result in results:
    print(result)

finish= time.time()-t
print(f"Time taken by both process to finish:{finish}")