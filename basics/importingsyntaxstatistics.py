#import statistics as s
#from statistics import mean
#from statistics import *  #this one is for importing everythin with the normal name as mean, variance, etc
from statistics import variance as v, mean as m


example_list = [1,3,2,7,3,6,0,7,4,2,1,5,7,8,3]

#x = statistics.mean(example_list)
#x = statistics.stdev(example_list)
x = v(example_list)
y = m(example_list)


print(x)
print(y)
