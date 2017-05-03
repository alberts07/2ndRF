import time
import calibration.calibrateNetNoGps as cal
import receive.RXMode as rec


calcTime = 60 # Seconds between YF-calculations

if __name__ == "__main__":

    tic = time.time()
    while True:
        rec.receiveMode()

        elapsedTime = time.time()-tic
        if elapsedTime >= calcTime:
            cal.calculabrate()
            tic = time.time()

