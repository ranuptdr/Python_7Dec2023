fruits = ('apple',"banana",'''pinepple''','apple') # this is tuple to store multiple student in one variable

print('Before change')
for fruit in fruits:
    print(f'I Like {fruit}')

print('After change')
fruits[0] = "kiwi"  # we can't change the items in tuple
for fruit in fruits:
    print(f'I Like {fruit}')