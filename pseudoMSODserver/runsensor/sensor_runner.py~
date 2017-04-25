import time
#from threading import Timer


def print_time():
    print "From print_time", time.time()

def receiver():
    print("I'm in the receiver function now")
    print("waiting for 4 seconds")
    time.sleep(4)
    print("Returning from receiver")

def calculabrate():
    print("Now I'm in the calculabrating function now")
    print("waiting for 3 seconds")
    time.sleep(3)
    print("Returning from receiver")


calcTime = 15

if __name__ == "__main__":

    tic = time.time()
    while True:
        receiver()

        elapsedTime = time.time()-tic
        if elapsedTime >= calcTime:
            calculabrate()
            tic = time.time()


"""
def print_some_times():
    print time.time()
    Timer(5, print_time, ()).start()
    Timer(10, print_time, ()).start()
    time.sleep(11)  # sleep while time-delay events execute
    print time.time()
"""
