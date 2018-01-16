""" A Functional Breakfast"""

def mix_and_cook():
    print('Mixing the ingredients')
    print('Greasing the pan')
    print('Pouring the mixture into a frying pan')
    print('Cooking the first side')
    print('Flipping it!')
    print('Cooking the other side')


def make_omellette(ingredient):
    mix_and_cook()
    omelette= 'a {} omelette'.format(ingredient)
    return omelette

def make_pancake():
    mix_and_cook()
    pancake= 'a delicious pancake'
    return pancake

def make_fancy_omelette(*args):
    mix_and_cook()
    fancy_omelette = 'a fancy omellete have {} ingredients'.format(len(args))
    return fancy_omelette

omelette = make_omellette('bacon')
pancake = make_pancake()
fancy_omellette = make_fancy_omelette('sausage', 'onion', 'pepper', 'spinach', 'mushroom', 'tomato')

print(omelette)
print(pancake)
print(fancy_omellette)