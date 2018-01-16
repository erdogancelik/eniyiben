""" A 3-Dimensional Valet Service"""

# 2D list of lists
# - index cars by row, spot

lot_2d = [['Toyota', 'Audi', 'BMW'],
          ['Lexus', 'Jeep'],
          ['Honda', 'Kia', 'Mazda']]

# 3D list of lists of lists
# - index cars by floor, row, spot

lot_3d = [[['Tesla', 'Fiat', 'BMW'],
           ['Honda', 'Jeep'],
           ['Saab', 'Kia', 'Ford'],
          [['Subaru', 'Nissan'],
            ['Volvo', ]],
          [['Mazda', 'Chevy'],
            [],
            ['Volkswagen']]]]

print(lot_2d)
print(lot_2d[2])
print(lot_2d[2][1])
print(lot_3d[0][2][1])

for floor in lot_3d:
    for row in floor:
        for car in row:
            print(car)