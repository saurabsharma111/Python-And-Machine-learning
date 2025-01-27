import threading
import time
def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(i)

def print_letters():
    for letter in "abcde":
        time.sleep(2)
        print(letter)
#create two thread
t1= threading.Thread(target=print_numbers)
t2= threading.Thread(target=print_letters)

t=time.time()
#START THE THREAD
t1.start()
t2.start()
#wait for the thread to complete
t1.join()
t2.join()
# print_numbers()
# print_letters()
finish=time.time()-t
print(finish)