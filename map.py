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
        self.map = np.zeros((self.size,  self.size, self.numFeeds))#incluye posicion celula y recusros de celda

    def available(self, position):
        #position as row/col
        #return True if occupy
        row = position[0]
        col = position[1]
        if row < 0 or row > (self.size - 1) or col < 0 or col > (self.size - 1):
            return True
        elif self.map[row][col][0] == 1:
            return True
        else:
            return False

    def ploting(self):

        plt.axis([0, 10, 0, 1])
        plt.ion() #in order to enable interactive plotting

        for i in range(10):
            y = np.random.random()
            plt.scatter(i, y)
            plt.pause(0.05)
