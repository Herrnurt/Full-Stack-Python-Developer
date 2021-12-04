# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 23:30:44 2021

@author: Oladipo Bolaji
"""


# This lesson has two parts. In the first part, involves writing a Pants class. 
# This class is similar to the shirt class with a couple of changes. 
# Then you'll practice instantiating Pants objects

# In the second part, involves writing another class called SalesPerson. 
# You'll also instantiate objects for the SalesPerson.



# Write a Pants class with the following characteristics:
# the class name should be Pants
# the class attributes should include
# color,waist_size,length,price
# the class should have an init function that initializes all of the attributes
# the class should have two methods
# change_price() a method to change the price attribute
# discount() to calculate a discount

class Pants:
    def __init__(self, color, waist_size, length, price):
        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price
        
        
    def  change_price(self,new_price):
        self.price = new_price
        
    def discount(self, percentage):
         return self.price * (1-percentage)
    
    
pants=Pants('red', 35, 36, 15.12)   

# print the price of the pants using the price attribute
print(pants.price)

# use the change_price method to change the price of the pants to 10
pants.change_price(10)
print(pants.price)

# use the discount method to print the price of the pants with a 12% discount
print(pants.discount(.1))
    


# Write a SalesPerson class with the following characteristics:

# the class name should be SalesPerson
# the class attributes should include
# first_name, last_name, employee_id,salary, pants_sold,total_sales
# the class should have an init function that initializes all of the attributes
# the class should have four methods
# sell_pants() a method to change the price attribute
# calculate_sales() a method to calculate the sales
# display_sales() a method to print out all the pants sold with nice formatting
# calculate_commission() a method to calculate the salesperson commission based on total sales and a percentage


class SalesPerson:
    def __init__(self, first_name, last_name, employee_id, salary):
        
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary  = salary
        
        # initialize pants_sold as an empty list
        self.pants_sold = []
    
        # initialize total_sales to zero.
        self.total_sales = 0
  
    # list pants that the salesperson has sold        
    def sell_pants(self, pants_object):
      # The sell_pants method appends a pants object to the pants_sold attribute  
      self.pants_sold.append(pants_object)
      
      
      
    # This method has no input or outputs. When this method 
    # is called, the code iterates through the pants_sold list
    # and prints out the characteristics of each pair of pants line by line.
    # the print out should look something like this
    # color: blue, waist_size: 34, length: 34, price: 10
    # color: red, waist_size: 36, length: 30, price: 14.15
    
    def display_sales(self):
        for pants in self.pants_sold:
            print( 'color:{}, waist_size:{}, length:{}, price:{}'\
                  .format(pants.color, pants.waist_size, pants.length, pants.price))
    
   
    
    # sum of sales of pants sold   
    def calculate_sales(self):
        
        
        total = 0
        for pants in self.pants_sold:
            total += total.price
            
            
        self.total_sales = total
        return total
   
    def calculate_commission(self, percentage):
        
        
        sales_total = self.calculate_sales()
        return sales_total * percentage



pants_one = Pants('red', 35, 36, 15.12)
pants_two = Pants('blue', 40, 38, 24.12)
pants_three = Pants('tan', 28, 30, 8.12)

salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)

salesperson.sell_pants(pants_one)    
salesperson.sell_pants(pants_two)
salesperson.sell_pants(pants_three)

salesperson.display_sales()