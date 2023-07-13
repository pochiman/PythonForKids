class Things:
    pass

class Inanimate(Things):
    pass

class Animate(Things):
    pass

class Animals(Animate):
    def breathe(self):
        print('breathing')
    def move(self):
        print('moving')
    def eat_food(self):
        print('eating food')

class Mammals(Animals):
    def feed_young_with_milk(self):
        print('feeding young')

class Giraffes(Mammals):
    def find_food(self):
        self.move()
        print('I\'ve found leaves!')
        self.eat_food()
    def eat_leaves_from_trees(self):
        print('tear leaves from branches')
        self.eat_food()
    def dance_a_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()

reginald = Giraffes()
reginald.dance_a_jig()

reginald.find_food()