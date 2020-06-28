"""
import time

initial = time.time()

currentTime = time.time() - initial


tempo = 1 / (116.021 / 60)


while True:

    currentTime = time.time() - initial

    if currentTime > 2:

        print(currentTime)

        inital = currentTime
        currentTime = 0

        #print('beat')

        
"""

from timer import Timer
t = Timer()
t.start()

