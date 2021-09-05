#WHILE LOOP
number = 1

while (number <= 10):
    # print(number)
    number += 1
    
# a = 1
# while a == 1:
#     print ("Welcome to the most famous club in all of Vegas!!")
#     age = int(input("How old are you? "))
#     if age >= 21:
#         print("Please come in...")
#     elif age >= 18:
#         print("You need to be over 21! Get Out!!")
#     else:
#         print("You are still a kid!, get out!")

#FOR LOOP
# for num in range(0, 10):
#     print(num)

# for letter in "Python":
#     print("Current Letter: " + letter)

#NESTED LOOP
lines = int(input("How many lines? "))
row = 0
while (row < lines):
    col = 0
    while(col < lines):
        print("*", end='')
        col += 1
    row += 1
    print()