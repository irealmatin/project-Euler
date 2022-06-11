"""
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

# Function for tell that  number 1-20 is divisible
def isdivisible(n):
    for i in range(2,21):
        if n % i !=0:
            return False
    return True

# To check numbers, we start with 20 because the result must be divisible by 20
n = 20
while True:
    if isdivisible(n):
        break
    n +=20  #increment n for new loop

# if found n => stop please
print(n)



