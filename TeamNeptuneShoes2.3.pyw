import random
import time


#Shrikar
neptune1 = (['Hello, and Welcome to Neptune Shoes.',
             'Hello, my name is Neptune and how can I help you?',
             'Hi, may I help you?.',
             'Welcome to Neptune Shoes.',
             'Welcome, my name is Neptune and I am here to help you.',
             'Hope you are doing well, my name is Neptune.'])

print(random.choice(neptune1))

time.sleep(1)
#Shrikar

#Tofty
neptune2 = (['You can select from Boots, Flip-Flops, Loafers, Oxfords and Trainers. We have numbered all the items we sell.',
             'We have plenty of options from Boots, Flip-Flops, Loafers, Oxfords and Trainers. Every pair we sell has got a number.',
             'We have got Boots, Flip-Flops, Loafers, Oxfords and Trainers. We have numbered all our footwear.',
             'We currently have options from Boots, Flip-Flops, Loafers, Oxfords and Trainers. Every pair we sell is numbered.'])


print(random.choice(neptune2))

time.sleep(1)
#Tofty
#Shrikar
shoes_price = {'Black Chelsea Boots': 55.00, 'Brown Chelsea Boots': 55.00, 'Black Combat Boots': 65.00,
            'Brown Combat Boots': 65.00, 'Black Chukka Boots': 45.00, 'Brown Chukka Boots': 45.00,
            'Black Flip-Flops': 20.00, 'Brown Flip-Flops': 20.00, 'Grey Flip-Flops': 20.00, 'Black Flip-Flops (No Toe Strap)': 25.00,
            'Brown Flip-Flops (No Toe Strap)': 25.00, 'Grey Flip-Flops (No Toe Strap)': 25.00, 'Black Loafers': 30.00, 'Brown Loafers': 30.00,
            'Black Oxfords': 35.00, 'Brown Oxfords': 35.00, 'Solid White': 50.00, 'Solid Black': 50.00, 'Black Low-Tops': 45.00, 'White Low-Tops': 45.00,
            'Grey Low-Tops': 45.00, 'Blue Low-Tops': 45.00, 'Red Low-Tops': 45.00, 'Black Hi-Tops': 55.00, 'White Hi-Tops': 55.00,
            'Grey Hi-Tops': 55.00, 'Blue Hi-Tops': 55.00, 'Red Hi-Tops': 55.00, 'Black Runners': 40.00, 'White Runners': 40.00,
            'Grey Runners': 40.00, 'Blue Runners': 40.00, 'Red Runners': 40.00, 'Black Gym Shoes': 60.00, 'White Gym Shoes': 60.00,
            'Grey Gym Shoes': 60.00, 'Blue Gym Shoes': 60.00, 'Red Gym Shoes': 60.00}
#Shrikar
#Victory
boots_price  = {'Black Chelsea Boots': 55.00, 'Brown Chelsea Boots': 55.00, 'Black Combat Boots': 65.00,
            'Brown Combat Boots': 65.00, 'Black Chukka Boots': 45.00, 'Brown Chukka Boots': 45.00}
               
flip_flops_price = {'Black Flip-Flops': 20.00, 'Brown Flip-Flops': 20.00, 'Grey Flip-Flops': 20.00, 'Black Flip-Flops (No Toe Strap)': 25.00,
            'Brown Flip-Flops (No Toe Strap)': 25.00, 'Grey Flip-Flops (No Toe Strap)': 25.00}
               
loafers_price = {'Black Loafers': 30.00, 'Brown Loafers': 30.00}
               
oxfords_price = {'Black Oxfords': 35.00, 'Brown Oxfords': 35.00}

trainers_price = {'Solid White': 50.00, 'Solid Black': 50.00, 'Black Low-Tops': 45.00, 'White Low-Tops': 45.00,
            'Grey Low-Tops': 45.00, 'Blue Low-Tops': 45.00, 'Red Low-Tops': 45.00, 'Black Hi-Tops': 55.00, 'White Hi-Tops': 55.00,
            'Grey Hi-Tops': 55.00, 'Blue Hi-Tops': 55.00, 'Red Hi-Tops': 55.00, 'Black Runners': 40.00, 'White Runners': 40.00,
            'Grey Runners': 40.00, 'Blue Runners': 40.00, 'Red Runners': 40.00, 'Black Gym Shoes': 60.00, 'White Gym Shoes': 60.00,
            'Grey Gym Shoes': 60.00, 'Blue Gym Shoes': 60.00, 'Red Gym Shoes': 60.00}
#Victory
#Donell
neptune3 = (['We have a bunch of shoes to select from.',
             'Please take a look at the selection of footwear we have.',
             'There are a bunch of shoes to select from, please take your time.',
             'Please take your time, we have many choices to pick from.'])
#Donell
#Tofty
shoeSize = ['9', '10', '10W', '11', '12']

neptune4 = (['We will be happy to find your shoe size.', 
             'The shoe size you want is readily available.',
             'We are more than happy to find you your required shoe size.'])
#Tofty
#Shrikar
response = 'yes'
while 'no' not in response:
    response = (input('\nWhat are you looking for? ')).lower()
    if 'everything' in response:
        print(random.choice(neptune3))
        time.sleep(1)
        i = 1
        for shoe, cost in shoes_price.items():
            print(str(i)+'. ', shoe+ ': ' +str(cost))
            i = i + 1
#Shrikar
#Lei        
    if 'boots' in response:
        print(random.choice(neptune3))
        time.sleep(1)
        i = 1
        for boots, cost in boots_price.items():
            print(str(i)+'. ', boots+ ': ' +str(cost))
            i = i + 1
        
    if 'flip flops' in response:
        print(random.choice(neptune3))
        time.sleep(1)
        i = 7
        for flip_flops, cost in flip_flops_price.items():
            print(str(i)+'. ', flip_flops+ ': ' +str(cost))
            i = i + 1
        
    if 'loafers' in response:
        print(random.choice(neptune3))
        time.sleep(1)
        i = 13
        for loafers, cost in loafers_price.items():
            print(str(i)+'. ', loafers+ ': ' +str(cost))
            i = i + 1
        
    if 'oxfords' in response:
        print(random.choice(neptune3))
        time.sleep(1)
        i = 15
        for oxfords, cost in oxfords_price.items():
            print(str(i)+'. ', oxfords+ ': ' +str(cost))
            i = i + 1
        
    if 'trainers' in response:
        print(random.choice(neptune3))
        time.sleep(1)
        i = 17
        for trainers, cost in trainers_price.items():
            print(str(i)+'. ', trainers+ ': ' +str(cost))
            i = i + 1 
#Lei
    response = (input('\nWould you like to check anything else?: ')).lower()
    response.lower()
    if response == 'no':
        print('Please take your time to select your size')

#Tofty
time.sleep(1)
       
for shoeSize in range(0, 1):
    size = input('\nPlease let me know your shoe size: ')
    print('Your shoe size is ' +size)
    time.sleep(1)
    print(random.choice(neptune4))
    
#Tofty

#Shrikar
time.sleep(1)

option = 'yes'
total_cost, total = 0, 0

while 'no' not in option:
    option = int(input('\nWhich pair would you like to purchase?: '))
    if option <= 2: 
        no = int(input('\nHow many would you like? '))
        total = no * 55.00
    if option == 3 or option == 4 : 
        no = int(input('\nHow many would you like? '))
        total = no * 65.00
    if option == 5 or option == 6: 
        no = int(input('\nHow many would you like? '))
        total = no * 45.00
    if option >= 7 and option <= 9: 
        no = int(input('\nHow many would you like? '))
        total = no * 20.00
    if option >= 10 and option <= 12: 
        no = int(input('\nHow many would you like? '))
        total = no * 25.00
    if option == 13 or option == 14: 
        no = int(input('\nHow many would you like? '))
        total = no * 30.00
    if option == 15 or option == 16: 
        no = int(input('\nHow many would you like? '))
        total = no * 35.00
    if option == 17 or option == 18: 
        no = int(input('\nHow many would you like? '))
        total = no * 50.00
    if option >= 19 and option <= 23: 
        no = int(input('\nHow many would you like? '))
        total = no * 45.00
    if option >= 24 and option <= 28: 
        no = int(input('\nHow many would you like? '))
        total = no * 55.00
    if option >= 29 and option <= 33: 
        no = int(input('\nHow many would you like? '))
        total = no * 40.00
    if option >= 34 and option <= 38: 
        no = int(input('\nHow many would you like? '))
        total = no * 60.00
    print(total)

    total_cost += total

    option = (input('\nWould you like another item?: ')).lower()
time.sleep(1)
print('The total price of your basket is: ', total_cost)

cashier = float(input('\nSo, that will be £' +str(total_cost)+ ': '))
if cashier == total_cost:
    print("Thank you")
elif cashier > total_cost:
    print("Here is your change of £" +str(cashier - total_cost))
#Shrikar

#Donell
neptune5 = (['Thank you for your review',
             'Thank you for leting us know what you think. We hope you will be happy next time',
             'Sorry for any inconviniences, we will make sure it goes well next time',
             'We are sorry for your experiences if it was bad, you will see more changes next time'])

review = input('\nWould you like to give us a review?: ')
if 'yes' in review:
    response2 = input('Please type your review: ')
print(random.choice(neptune5))
time.sleep(1)
#Donell

#Shrikar
neptune6 = (['Thank you for shopping with Neptune Shoes',
             'We hope to see you again soon',
             'I hope you enjoyed shopping here today',
             'Make sure to come again soon',
             'I hope you are happy today'])

print(random.choice(neptune6))
#Shrikar
