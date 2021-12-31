from random import randint
decorators = [
    ' Store',
    ' Closet',
    ' Fashion',
    ' Moda',
    ' Shirt'
]

def randomDecorator():
    value = randint(0,4)
    return decorators[value]

with open('nouns.txt') as f: 
    contents = [line.rstrip() for line in f]
    
for c in contents:
    index = c.find(';')
    c = c[:index].capitalize()
    if c.startswith('M'):
        print(c + randomDecorator())
    