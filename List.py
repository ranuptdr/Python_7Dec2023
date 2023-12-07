fruits = ['apple',"banana",'''pinepple''','apple'] # this is list to store multiple student in one variable

print('Before change')
for fruit in fruits:
    print(f'I Like {fruit}')

print('After change')
fruits[0] = "kiwi"  # change the value of list
for fruit in fruits:
    print(f'I Like {fruit}')