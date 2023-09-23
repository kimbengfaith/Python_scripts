#! /usr/bin/python3

print("""

This is a project that calculates the total cost of a customers shopping
basket, including shipping.
  
  - If a customer spend over $100, they get free shipping.
  - If the customer spends less than $100, then shipping cost is $1.20 per kg of the baskets weight.
 
""")

customer_basket_cost = int(input('Enter your basket cost: '))
customer_basket_weight = int(input('Enter the weight of the basket: '))

if customer_basket_cost < 100:
  shipping_cost = customer_basket_weight * 1.20

else:
  shipping_cost = 0

total_cost = shipping_cost + customer_basket_cost

print(total_cost)
