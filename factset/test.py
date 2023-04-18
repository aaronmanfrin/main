from OL import *
from getfood import *


food = getFood()
order = getOrder()
friend = getFriendOrder()
if order =='':
    print("Today I'm going to have "+food+" for lunch!"+friend)
else:
    print("Today I'm going to have "+order+" for lunch!"+friend)

 