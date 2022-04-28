#Question :
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#The sum of these multiples is 23.Find the sum of all the multiples of 3 or 5 below 1000.

s=sum(set(range(0,1000,3)) | set(range(0,1000,5)))
print(s)

#Output : 233168
