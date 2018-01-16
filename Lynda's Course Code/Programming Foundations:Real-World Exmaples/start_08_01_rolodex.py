""" A Rolodex Full of Friends """

# dictionary of name/number pairs
rolodex = {'Aaron': 5556069,
           'Bill': 5559824,
           'Kuangwei': 5552603,
           'David': 5558331}

print(rolodex['Aaron'])

# adding new item to dictionary
rolodex['Amanda'] = 5559754

print(rolodex['Amanda'])

# update existing item which can only have one same key
rolodex['David'] = 5556969

print(rolodex['David'])

# tuple can be nested on the dictionary
rolodex['Erdogan'] = (5551223, 'QA', 'Colorado')

print(rolodex)
