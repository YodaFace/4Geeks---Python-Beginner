
user_input = int(input('How many people are coming to your wedding?\n'))

if user_input < 50:
    price = 4000
elif user_input > 50 and user_input < 101:
    price = 10000
elif user_input > 100 and user_input < 201:
    price = 15000
else: 
    price = 20000


print('Your wedding will cost '+str(price)+' dollars')



# if user_input > 200:
#     print ("Your wedding will cost $20,000")
# elif user_input > 100 and user_input < 201:
#     print ("Your wedding will cost $15,000")
# elif user_input > 50 and user_input < 101:
#     print ("Your wedding will cost $15,000")
# else:
#     print ("Your wedding will cost $4,000")


# Up to 50 people $4,000 
# Up to 100 people $10,000 
# Up to 200 people $15,000 
# More than 200 people $20,000