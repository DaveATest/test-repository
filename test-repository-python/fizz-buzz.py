#Last Edit: 3/1/17 by David Greer
#Test Edit via DaveATest account on Github on 4/23/17

#The loop below implements the "FizzBuzz" problem,
#where the numbers from 1 to 100 are printed, with
#Fizz being printed if a number is a multiple of 3,
#Buzz being printed if a number is a multiple of 5,
#and FizzBuzz if a number is a multiple of 3 and 5

for i in range(1, 101): #for all integers from 1 to 100
    if (i%15 == 0): #checks if i is a multiple of 3 and 5
        print("FizzBuzz")
    elif (i%3 == 0): #checks if i is a multiple of 3
        print("Fizz")
    elif (i%5 == 0): #checks if i is a multiple of 5
        print("Buzz")
    else:
        print(i)