import random

def get_numbers_ticket(min, max, quantity):

    lottery_numbers = []

    if type(min) != int or type(max) != int or type(quantity) != int: #check if args are int 
        return lottery_numbers
    
    if min < 1 or max > 1000:
        print ("The numbers should be in 1 - 1000 range")
        return lottery_numbers

    lottery_numbers =  random.sample(range(min, max), quantity)
    lottery_numbers.sort()                                            #sort the lottery_numbers list

    return lottery_numbers


#print (get_numbers_ticket("-11", 44, 4))                             
