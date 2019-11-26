import math
test=454
for i in xrange(1,int(math.sqrt(test))):
  if test % i == 0: print i
