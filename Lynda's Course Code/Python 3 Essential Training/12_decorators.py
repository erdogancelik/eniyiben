class Material():

    def __init__(self, **kwargs):
        self.variables = kwargs

    def get_variables(self, key):
        return self.variables.get(key, None)

    def set_variables(self, key, value):
        self.variables[key] = value

    def get_properties(self):
        return self.variables

    @property
    def age(self):
        return self.variables.get('age', 0)

    @age.setter
    def age(self, age):
        self.variables['age'] = age

    @age.deleter
    def age(self):
        del self.variables['age']


    @property
    def name(self):
        return self.variables.get('name', 'No name has been attached yet')

    @name.setter
    def name (self, n):
        self.variables['name'] = n

    @name.deleter
    def name(self):
        del self.variables['name']

Home = Material()
Home.name = 'Tatloshy'
Home.age = 1
print(Home.name, Home.age)