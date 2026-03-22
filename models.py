from basemodel import BaseModel

class Fruit(BaseModel):
    name = ""

    def __str__(self):
        return self.name
    

class User(BaseModel):
    name = ""

    def __str__(self):
        return self.name