# pool_ops.py
#
# Text explaining script usage
# Parameters:

# ...
# output:
# ecef x y z coords
#
# Written by Dylan Hogge
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.
# import Python modules
import sys  # argv
import math  # mathematical functions

# initialize script arguments
c_in = float('nan')   
h_in = float('nan')   
w_in = float('nan')   
n_filt = float('nan') 
h_filt = float('nan') 
w_filt = float('nan') 
s = float('nan')      
p = float('nan')

# parse script arguments
if len(sys.argv) == 8:
  c_in = float(sys.argv[1])
  h_in = float(sys.argv[2])
  w_in = float(sys.argv[3])
  h_pool = float(sys.argv[4])
  w_pool = float(sys.argv[5])
  s = float(sys.argv[6])
  p = float(sys.argv[7])
else:
  print(\
   'Usage: '\
   'python3 conv_ops.py c_in h_in w_in h_pool w_pool s p'\
  )
  exit()
  
# write script below this line
c_out = c_in
h_out = floor(((h_in+2*p-h_pool)/s)+1)
w_out = floor(((w_in+2*p-w_pool)/s)+1)
adds = c_in*h_out*w_out*(h_pool*w_pool-1)
muls = 0 
divs = c_in*h_out*w_out

print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed

