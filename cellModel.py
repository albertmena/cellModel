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

import random

listID = []

def createPopulation():
    listID.append(1)
    return len(listID)
def retirePopulation (ID):
    listID[ID] = 0


'''------------------------'''

class motherCell:
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

        self.feeds = feeds #[0, 0, 0, 0, 0, 0]


    '''------------------------'''
    def live(self):
        self.refershSkills(self.time, self.feeds, self.hungry, self.mutability, self.reproductibility, self.mortality)
        self.reproduction(self.mutability, self.feeds)
        self.food(self.feeds, self.instinct)
        self.dead(self.mortality, self.ID)

    '''------------------------'''
    def refershSkills(self, time, feeds, hungry, mutability, reproductibility, mortality ):
        return 0
    def reproduction(self, mutability, feeds):
        return 0
    def food(self, feeds, instinct):
        return 0
    def dead(self, mortality, ID):
        return 0

    '''------------------------'''
    def smeel(self, instinct, position):
        return 0
    def eat(self, feeds):
        return 0
    def move (self, agility, x, y):
        return 0






if __name__ == '__main__':
    EVA = motherCell(createPopulation(), (0,0), 50, 50, 50, [50, 50, 50, 50, 50, 50])
    print "Iniciada la vida"
    print "Primera habitante:", EVA.ID, "Instinto:", EVA.instinct

    print listID
