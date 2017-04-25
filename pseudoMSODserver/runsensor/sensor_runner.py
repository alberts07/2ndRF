import time
import calibration
import receive


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

