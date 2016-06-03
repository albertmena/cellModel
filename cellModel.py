'''
Steps in a cell:
    1/ update skills:
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
    def updateSkills(self):
        #time, feeds, mutability, reproductibility, mortality
        self.food()#hungry

    def reproduction(self):
        #mutability, feeds
        pass

    def food(self):
        #feeds, instinct
        if sum(self.feeds[:-2])/(len(self.feeds) - 1) < 50:
            self.smell()
        else:
            pass
    def dead(self):
        #mortality
        if self.mortality < 10:
            goverment.retirePopulation(self.ID)

    '''------------------------'''
    def smell(self):
        position_smell = self.position + (4,4)
        self.move(position_smell)

    def eat(self, feeds):
        return 0
    def move (self, position_smell):
        #manage agility
        goverment.map_i.move(position_smell)


