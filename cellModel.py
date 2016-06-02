'''
Steps in a cell:
    1/ refresh skills:
        - hungry(feeds)
        - mutability(feeds)
        - reproductibility(feeds, time)
        - mortality (feeds, time)
    2/ check reproduction:
            True: create cell with actual mutability skill, use feeds
            False: pass
    3/ check food:
            check hungry:
                True: calculate distance with smell:
                    distance = 0: eat(feeds)
                    distance > 0: move (x, y time) use feeds
    4/ check dead(feeds, time):
            True: dead
            False: pass

'''

import map
import nature
import goverment


'''------------------------'''

class MotherCell:
    def __init__(self,ID,position, agility, instinct, mutability, feeds):
        self.ID = ID
        self.time = 0
        self.position = position
        #Skills
        self.agility = agility
        self.instinct = instinct
        #states
        self.hungry = 0
        self.mutability = mutability
        self.reproductibility = 0
        self.mortality = 0

        self.feeds = feeds #[0, 0, 0, 0, 0]


    '''------------------------'''
    def live(self):
        self.refershSkills()
        self.reproduction(self.mutability, self.feeds)
        self.food(self.feeds, self.instinct)
        self.dead(self.mortality, self.ID)

    '''------------------------'''
    def refershSkills(self):
        #time, feeds, hungry, mutability, reproductibility, mortality
        pass
    def reproduction(self):
        #mutability, feeds
        pass
    def food(self):
        #feeds, instinct
        pass
    def dead(self):
        #mortality
        if self.mortality < 10:
            goverment.retirePopulation(self.ID)

    '''------------------------'''
    def smell(self, instinct, position):
        return 0
    def eat(self, feeds):
        return 0
    def move (self, agility, x, y):
        return 0


