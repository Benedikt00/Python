import time

from pysinewave import *

# Create a sine wave, with a starting pitch of 12, and a pitch change speed of 10/second.
sinewave = SineWave(pitch_per_second = 999999)



# Turn the sine wave on.
sinewave.play()

# Sleep for 2 seconds, as the sinewave keeps playing.
time.sleep(2)

# Set the goal pitch to -5.
sinewave.set_frequency(440)

# Sleep for 3 seconds, as the sinewave smoothly slides its pitch down from 12 to -5, and stays there.
time.sleep(3)

