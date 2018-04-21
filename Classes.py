class Animal():
    name = 'Amy'
    noise = "Grunt"
    size = "Large"
    color = "Brown"
    hair = 'Covers body'
    def get_color(self):
        return self.color
    def make_noise(self):
        return self.noise


dog = Animal()
dog.make_noise()
dog.size = "small"
dog.color = "black"
dog.hair = "Hairless"


class Dog(Animal):
    name = "Jon"
    size = "small"
    color = "black"
    age = 19
        
Jon = Dog()
Jon.color = 'white'
Jon.name = 'Jon Snow'
    
    