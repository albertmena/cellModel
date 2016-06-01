import cellModel
import map
import nature


class goverment:
    ''' manage population '''
    def __init__(self ):
        self.listID = []

    def createPopulation(self):
        IDx = len(goverment.listID)
        goverment.listID.append(cellModel.motherCell(IDx, (0,0), 50, 50, 50, [50, 50, 50, 50, 50]))

    def retirePopulation (self, IDx):
        goverment.listID[IDx] = 0 #instancia cell no esta borrada creo



if __name__ == '__main__':
    goverment = goverment()
    map = map.map(1000)
    nature = nature.nature(map, 50)
    goverment.createPopulation()
    print "Iniciada la vida"
    goverment.retirePopulation(goverment.listID[0].ID)

