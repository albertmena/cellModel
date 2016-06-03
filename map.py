import cellModel
import nature
import goverment
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


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

    def move(self, position):
        if self.available(position):
            self.map_cells[position[0]][position[1]] = 1
        else:
            return False

    def ploting(self):

        plt.axis([0, self.size, 0, self.size])
        plt.ion() #in order to enable interactive plotting
        self.map_cells[2][2] = 2
        for i in range(1):
            plt.matshow(self.map_cells, fignum=1, cmap=plt.cm.gray)
            plt.pause(3)

