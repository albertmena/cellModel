import cellModel

import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
class Goverment:
    ''' manage population '''
    def __init__(self ):
        self.listID = []
        self.listCells = []

    def createPopulation(self, position):
        IDx = len(goverment_i.listID)
        self.listID.append(IDx)
        self.listCells.append(cellModel.MotherCell(IDx, position, 50, 50, 50, [50, 50, 50, 50, 50]))

    def retirePopulation (self, IDx):
        self.listID[IDx] = 0 #instancia cell no esta borrada creo

    def readCell(self, ID):
        return self.listID[ID]


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
        elif self.map[row][col][0] == 1:
            return False
        else:
            return True

    def move(self, actual_position, position):
        if self.available(position):
            self.map_cells[position[0]][position[1]] = 1
            self.map_cells[actual_position[0]][actual_position[1]] = 0
            print "holalaaa"
        else:
            return False

    def ploting(self):

        plt.axis([0, self.size, 0, self.size])
        plt.ion() #in order to enable interactive plotting
        for i in range(50):
            plt.matshow(self.map_cells, fignum=1, cmap=plt.cm.gray)
            plt.pause(0.5)


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


if __name__ == '__main__':
    goverment_i = Goverment()
    nature_i = Nature(5)
    map_i = Map(10, nature_i.num_feeds)
    goverment_i.createPopulation((2,2))
    print "Iniciada la vida"
    goverment_i.listCells[0].smell()
    goverment_i.listCells[0].position
    map_i.ploting()

    goverment_i.retirePopulation(goverment_i.listID[0].ID)

