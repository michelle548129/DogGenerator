from application import db

class results(db.Model):
    __tablename__= 'results'
    id = db.Column(db.Integer, primary_key = True)
    breed = db.Column(db.String(255))
    name = db.Column(db.String(255))
    colour = db.Column(db.String(255))
    def __str__(self):
        return f"{self.breed} called {self.name} is {self.colour}"