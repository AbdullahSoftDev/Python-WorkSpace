class Person:
    # Class variable
    species = "Human"
    
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Instance method
    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old"
    
    # Class method
    @classmethod
    def from_birth_year(cls, name, birth_year):
        import datetime
        age = datetime.datetime.now().year - birth_year
        return cls(name, age)
    
    # Static method
    @staticmethod
    def is_adult(age):
        return age >= 18
    
    # Property
    @property
    def is_minor(self):
        return self.age < 18
    
    # Setter
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value