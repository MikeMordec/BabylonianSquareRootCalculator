print ("Michael Mordec, 6/17/22, Lab 3, CSC 242:")
# Babylonian Method
# Programmer: Michael Mordec

def Babylonian(number):
    x = number
    # (1) choose y = 1 as an initial estimate of square root(x)
    y = 1
    # (2) if x > 2 , let y = x / 2
    if(x > 2):
        y = x / 2.0

    i = 1
    while (True):

        # (3) let y = the average of y and x / y 
        y = ((y)+(x/y))/2.0
        
        # (4) if y ^ 2 is not close enough to x , then repeat step (3)
        delta = abs(y*y - x)
        print(i, y)
        if(delta < 0.001):
            # (5) return y , as the square root of x 
            return y
        i = i + 1
        

print ("----- The Babylonian Method -----\n")

radicand = float(input("please enter a positive real number "))
radical = Babylonian(radicand)

print ("the square root of", radicand, "is", radical)
