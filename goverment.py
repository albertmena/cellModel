import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading

'''------------GOVERMENT'''
class Goverment:
    ''' manage population '''
    def __init__(self ):
        self.listID = []
        self.listCells = []

    def createPopulation(self, position):
        IDx = len(goverment_i.listID)
        self.listID.append(IDx)
        self.listCells.append(MotherCell(IDx, position, 50, 50, 50, [50, 50, 50, 50, 50]))

    def retirePopulation (self, IDx):
        self.listID[IDx] = 0 #instancia cell no esta borrada creo

    def readCell(self, ID):
        return self.listID[ID]


'''------------MAP'''
class Map:
    '''manage map(x,y); collision, edges, plot...
     map as 3dim matrix, (row, col, feeds (numfeeds + 1/0 if cell in position)
     cell in position: [N][[N][pos, feed1, feed2, feed3, feed4, feed5]
     '''
    def __init__(self,  size, numFeeds):
        self.size = size
        self.numFeeds = numFeeds
        self.map_feeds = np.zeros((self.size,  self.size))#incluye recusros de celda
        self.map_cells = np.zeros((self.size,  self.size)) #ncluye posicion celula

    def available(self, position):
        #position as row/col
        #return True if occupy
        row = position[0]
        col = position[1]
        if row < 0 or row > (self.size - 1) or col < 0 or col > (self.size - 1):
            return False
        elif self.map_cells[row, col] == 1:
            return False
        else:
            return True

    def moveInMap(self, actual_position, position):
        if self.available(position):
            self.map_cells[position[0]][position[1]] = 1
            self.map_cells[actual_position[0]][actual_position[1]] = 0
            return True
        else:
            return False

    def ploting(self):

        plt.axis([0, self.size, 0, self.size])
        plt.ion() #in order to enable interactive plotting
        for i in range(20):
            plt.matshow(self.map_cells, fignum=1, cmap=plt.cm.gray)
            plt.pause(1)


'''------------NATURE'''
class Nature:
    '''manage feed seeds, delete feeds (eat by cells)'''
    def __init__(self, abundance):
        self.abundance = abundance
        self.num_feeds = 5
        self.feeds = 0

    def initialSeed(selfself):
        pass

    def deleteFeed(self, position, feeds):
        pass

    def createFeed(self):
        pass


'''------------CELLS'''
class MotherCell:
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
            goverment_i.retirePopulation(self.ID)

    '''------------------------'''
    def smell(self):
        position_smell = (self.position[0] + 2, self.position[0] + 2)
        self.move(position_smell)
        print "smell"

    def eat(self, feeds):
        return 0

    def move(self, position_smell):
        #manage agility
        if map_i.moveInMap(self.position, position_smell):
            self.position = position_smell


'''-----------MAIN'''
if __name__ == '__main__':
    goverment_i = Goverment()
    nature_i = Nature(5)
    map_i = Map(100, nature_i.num_feeds)
    goverment_i.createPopulation((2,2))
    t = threading.Thread(target=map_i.ploting)
    print "Iniciada la vida"
    print "Cell position: ", goverment_i.listCells[0].position
    t.start()
    time.sleep(1)
    goverment_i.listCells[0].smell()
    print "Cell position: ", goverment_i.listCells[0].position
    time.sleep(1)
    goverment_i.listCells[0].smell()
    print "Cell position: ", goverment_i.listCells[0].position
    time.sleep(1)
    goverment_i.listCells[0].smell()
    print "Cell position: ", goverment_i.listCells[0].position
    time.sleep(1)
    goverment_i.listCells[0].smell()
    print "Cell position: ", goverment_i.listCells[0].position
    goverment_i.retirePopulation(goverment_i.listID[0].ID)
