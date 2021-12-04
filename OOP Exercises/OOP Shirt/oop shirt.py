# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 22:30:15 2021

@author: Oladipo Bolaji
"""

class shirt:
    def __init__(self,shirt_color,shirt_size,shirt_style,shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price
        
    def change_price(self,new_price):
        self.price = new_price
        
    def discount(self,discount):
        return self.price * (1-discount)
    
    
# insantiate a shirt object with the following characteristics:
# color red, size S, style long-sleeve, and price 25    
shirt_one = shirt('red', 'S', 'long-sleeve', 25)

# print the price of the shirt using the price attribute
print(shirt_one.price)

# use the change_price method to change the price of the shirt to 10
shirt_one.change_price(10)
print(shirt_one.price)

# use the discount method to print the price of the shirt with a 12% discount
print(shirt_one.discount(.12))


# instantiate another object with the following characteristics:
# color orange, size L, style short-sleeve, and price 10
shirt_two = shirt('orange', 'L', 'short-sleeve', 10)

print(shirt_two.price)

total = shirt_one.price + shirt_two.price
print(total)

total_discount = shirt_one.discount(.14)+ shirt_one.discount(.06)
print(total_discount)
