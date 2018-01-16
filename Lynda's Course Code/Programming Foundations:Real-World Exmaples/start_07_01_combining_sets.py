""" Creating and Combining Sets of Friends"""

college = {'Bill', 'Katy', 'Verne', 'Dillion', 'Bruce', 'Olivia', 'Richard', 'Jim'}

coworker = {'Aaron', 'Bill', 'Brandon', 'David', 'Frank', 'Connie', 'Kyle', 'Olivia'}

family = {'Garry', 'Landon', 'Larry', 'Mark', 'Olivia', 'Katy', 'Rae', 'Tom'}

print(len(college), len(coworker), len(family))

friends = college.union(coworker,family)

print(coworker.intersection(family))

print(college.difference(coworker))

print(family.symmetric_difference(college))


