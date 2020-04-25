import numpy as np
import math
n = int(input())
x = np.array(list(map(int, input().split())))

p0 = math.floor(x.sum()/n)
p1 = math.ceil(x.sum()/n)
cost0 = np.sum((x-p0)**2)
cost1 = np.sum((x-p1)**2)
print(min(cost0, cost1))
