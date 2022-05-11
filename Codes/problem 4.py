#Question :

"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers

"""
answer = []

for num1 in range(999,100,-1):
    for num2 in range(999,100,-1):
        tmp = str(num1*num2)
        answer.append(num1*num2) if tmp == tmp[::-1] else None

print(max(answer))

#Output : 906609
