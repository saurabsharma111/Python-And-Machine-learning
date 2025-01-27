#multiprocessing
#P
import multiprocessing
import time

def square():
    for i in range(6):
        time.sleep(1)
        print(f"Square:{i**2}")

def cube():
    for i in range(6):
        time.sleep(1)
        print(f"Cube:{i**3}")

if __name__=="__main__":
    #create two process
    p1 = multiprocessing.Process(target=square)
    p2 = multiprocessing.Process(target=cube)
    #time
    t=time.time()
    #start the process
    p1.start()
    p2.start()
    #wait for both process to finish
    p1.join()
    p2.join()
    finish= time.time()-t
    print(f"Time taken by both process to finish:{finish}")