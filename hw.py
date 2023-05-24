# Exercise #1
# Cube Number Test... Print out all cubed numbers up to the total value 1000, so if the cubed number is over 1000 break the loop.
for i in range (11):
    i**3
    print(i**3)
# Exercise #2
# Get first prime numbers up to 100
for Number  in range (1, 101):
    count = 0
    for i in range(2,(Number//2+1)):
        if (Number %i==0):
             count=count+1
             break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ') 

# # HINT::
# # An else after an if runs if the if didn’t
# # An else after a for runs if the for didn’t break


# Exercise 3
# Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors
age = input('How old are you?')
if int(age)<18:
    print ('kids')
elif int(age)in range(18,65):
    print ('adults')
else:
    print('seniors')