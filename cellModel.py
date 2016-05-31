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


class goverment:
    ''' manage population '''
    def __init__(self, ):
        self.listID = []

    def createPopulation(self):
        IDx = len(goverment.listID)
        goverment.listID.append(motherCell(IDx, (0,0), 50, 50, 50, [50, 50, 50, 50, 50]))

    def retirePopulation (self, IDx):
        goverment.listID[IDx] = 0 #instancia cell no esta borrada creo


class map:
    '''manage map(x,y); collision, edges, plot... '''
    def __init__(self,  size ):
        self.size
        self.matrix

    def collision(self, position):
        #return True if abailable
        pass




class nature:
    '''manage feed seeds, delete feeds (eat by cells)'''
    def __init__(self, feeds, matrix, abundance):
        self.abundance = abundance

    def initialSeed(selfself):
        pass

    def deleteFeed(self, position, feeds):
        pass

    def createFeed(self):
        pass


if __name__ == '__main__':
    goverment = goverment()
    goverment.createPopulation()
    print "Iniciada la vida"
    goverment.retirePopulation(goverment.listID[0].ID)

