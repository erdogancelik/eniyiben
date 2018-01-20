""" Loading the Dishwasher """

# dirty dishes in the sink

sink =['bowl', 'plate', 'cup']

# create the copy of list while removing item on the list
for dish in list(sink):
    print('Putting {} in the dishwasher'.format(dish))
    sink.remove(dish)

print(sink)