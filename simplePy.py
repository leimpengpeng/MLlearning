import numpy as np
A = np.random.normal(25.0, 5.0, 10)
print (A)

def SquareIt(x):
    return x * x
print (SquareIt(2)) 

def DoSomething(f, x):
    return f(x)

print (DoSomething(SquareIt,3))

print(1 == 3)

# Like a map or hash table in other languages
captains = {}
captains["Enterprise"] = "Kirk"
captains["Enterprise D"] = "Picard"
captains["Deep Space Nine"] = "Sisko"
captains["Voyager"] = "Janeway"

print(captains["Voyager"])

for ship in captains:
    print(ship + ": " + captains[ship])