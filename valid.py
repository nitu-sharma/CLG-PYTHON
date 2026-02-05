# loop
for i in range(10):
    print (i)
    # whileLoop
    count = 0 
    while count<5:
        print(count)
        count +=1 
        
# Question
# sum of n natural number
n = 10
sum = 0
for i in range(1,n+1):
    sum += i
print("The sum of first", n, "natural numbers is:", sum)
# table of n
n =10
print ("table of", n)
for i in range(1,11):
    print(n,"x",i,"=",n*i)
    
    table of n  natiural number 
n = int(input("Enter a number: "))
print ("table of", n)
for i in range(1,11 ):
    print(n,"x",i,"=",n*i)
sum od n naturall number using while loop
n = int (input("Enter the number: "))
sum = 0
count = 1
while count <= n:
    sum += count
    count += 1
print("The sum of first", n, "natural numbers is:", sum)

# factorial of n natural number
n = int (input("Enter the number: "))
factorial = 1
count = 1
while count <= n:
     factorial *= count
     count += 1
     print("the factorial of", n, "is", factorial) 
# even number from 1 to n usling for loop
n = int(input("Enter the number: "))
print("Even number from 1 to", n, "are:")
for i in range(1, n+1):
    if i%2 == 0:
        print (i)