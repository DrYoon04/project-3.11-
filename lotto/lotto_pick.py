import random
import pandas as pd
number = list(range(1,46))
pick_number = []


for i in range(1, 7):
    pick = random.choice(number)
    number.remove(pick)
    if pick not in pick_number:
        pick_number.append(pick)
    


print(pick_number.sort())