#Обчислити значення виразу (1+cos(0.1))(2+cos(0.2))*...*(9+cos(0.9))
import math
counter = 1
for i in range(1,10):
    counter *= (i+math.cos(0.1*i))
print(counter)
