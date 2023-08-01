foods=['pizza', 'duck', 'pig','chicken']

print("The frist three items in the list are:")
for food in foods[:3]:
    print(food)

length=int(len(foods)/2)
#print(length)
print("\nThe middle three items in the list are:")
for food in foods[length-1:length+2]:
    print(food)

print("\nThe last three items in the list are:")
for food in foods[-3:]:
    print(food)

#page 66 to 56???
pizzas=["potato pizza", "bacon pizza", "pineapple pizza"]
for pizza in pizzas:
    #print(pizza.title())
    print(f"I like {pizza}")
print("I love pizza!")

friends_pizzas=pizzas[:]
pizzas.append("duck pizza")
friends_pizzas.append("bitcoin pizza")

print("My pizza list is")
for pizza in pizzas:
    print(pizza)

print("My friends pizza list is ")
for pizza in friends_pizzas:
    print(pizza)

my_food=['pizza', 'falafel', 'carrot cake']
friends_food=my_food[:]
#friends_food=my_food t
my_food.append("ori gogi")
friends_food.append("pig gogi")

print("\nMy favorite foods are:")
for food in foods:
    print(food)
print("\nMy friend's favorite foods are:")
for food in friends_food:
    print(food)