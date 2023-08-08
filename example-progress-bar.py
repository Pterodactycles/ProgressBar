
import sys
from ProgressBar import ProgressBar as pb

import time

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

progress = pb() # initialize the progress bar 
total = 100
for index in range(1, total+1):
    progress.display_progress(index,total,width=35,inline=True,time=True)
    time.sleep(0.3)

# there are a couple of nuances to note when using the progressbar class.
# the class is basic, has no error catching, and given unintended values for
# 'index' and 'total', will still calculate unrealistic values.
# The iteration number must begin at 1, not zero. This is because when calculating
# the percentage completed, a division by the iteration number is used, which 
# will produce a zero division error if iteration = 0.
# in order to reach 100%, the iteration number must equal the total number.
# sometimes this involves using code akin to:

# progress.display_progress(index +1,total)

# Regardless, feel free to do whatever with this code
