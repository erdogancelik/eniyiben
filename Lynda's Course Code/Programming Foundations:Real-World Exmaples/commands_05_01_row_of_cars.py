row = ['Ford', 'Audi', 'BMW', 'Lexus']

# adds end of the list
row.append('Mercedes')
print(row)
print(row[4])

# retrieves the positional item
row[2]= 'Jeep'
print(row)

row.append('Honda')
print(row)

# adds the position passed
row.insert(0, 'Kia')
print(row)

# finds the first item on the list
in_the_row =row.index('Mercedes')
print(in_the_row)

# removes item on the position
row.pop(5)
print(row)

# removes spesified item on the list
row.remove('Lexus')
print(row)