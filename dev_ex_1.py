#Kieran burnett
#Dev ex 1
cake = "It's a lie"

import random
country = ["France","Russia","England","Germany","Egypt","Greece","Ireland","Spain","Sweden","Australia"]
capital = ["Paris","Moscow","London","Berlin","Cairo","Athens","Dublin","Madrid","Stockholm","Canbarra"]

def selector(country,capital):
    points = 0
    for count in range(5):
        num = random.randint(1,10)
        guess = input("Please enter the capital of {0}: ".format(country[num]))
        if guess.lower == capital[num].lower:
            print("You got it right")
            points = points + 1
        else:
            print("you got it wrong")
    return points
        
def main(country,capital):
    points = selector(country,capital)
    print("You got {0}/5 right".format(points))
main(country,capital)
    
