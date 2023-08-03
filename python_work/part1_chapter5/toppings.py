requested_topping=['mushrooms']

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

requested_topping.append('onions')
requested_topping.append('pineapple')
print('mushrooms' in requested_topping)
print('pepperoni' in requested_topping)