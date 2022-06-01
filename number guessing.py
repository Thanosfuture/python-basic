import random

answer = random.randint(1 , 25)
print("I am guessing num from 1 to 30 ")

count = 0


while(True):
    count = count+1
    print( " can you guess it ?")
    prediction = int(input())
    if prediction > answer:
        print("answer is too high")
    elif prediction < answer:
        print("answer is too low")
    else:
        print("It is correct !")
        break
print("you have attempt for " +str(count) + "times")