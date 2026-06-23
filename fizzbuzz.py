for i in range(1, 50):
    if i % 3 == 0 and i % 5 == 0: #check multiples of both 3 and 5
        print("FizzBuzz")
    elif i % 3 == 0: #check multiples of 3
        print("Fizz")
    elif i % 5 == 0: #check multiples of 5
        print("Buzz")
    else:
        print(i) #print remaining numbers