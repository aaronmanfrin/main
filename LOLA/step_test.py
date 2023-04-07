
from ast import main

step = 0

main_list=[1,2,3,4,3,5,7,10,22,23,24,17,16,16,15,18,27,34]
## List of values to print at step = 3: 4,10,22,23,24,34

for i in range(len(main_list)):
    y=0 ## represents 1st day in step
    x=1 ## represents 2nd day in step
    count=0 ## to count #of loops
    while x <=step:
        if main_list[i-y]>=main_list[i-x]:
            count +=1
        y+=1
        x+=1
    if count == step:
        print(main_list[i])