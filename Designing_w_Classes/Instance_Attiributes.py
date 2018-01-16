class Name:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


def system_giver(Y):
    for x in Y.__dict__:
        if not x.startswith('__'):
            print(x, Y.__dict__[x])


def dict_opener(diction):
    for a in diction.items():
        print(a)


X = Name('Jalpo', 'Celik')

dictionary = {'name': 'Erdogan', 'last_name': 'Celik'}
system_giver(X)
dict_opener(dictionary)

print(dir(X))
