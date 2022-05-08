"""""
Question :

  The prime factors of 13195 are 5, 7, 13 and 29.
  What is the largest prime factor of the number 600851475143 ?

"""

number = 600851475143 
i = 2
 # loop for define the largest of prime factor

while number != 1 :
    Cycle_of_numbers = number % i
    if Cycle_of_numbers == 0 :
         number = number / i
         mylist = [i]
    else :
        i = i+1

print(max(mylist))

#output = 6857