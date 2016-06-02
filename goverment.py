import cellModel
import map
import nature


class Goverment:
    ''' manage population '''
    def __init__(self ):
        self.listID = []

    def createPopulation(self):
        IDx = len(goverment.listID)
        self.listID.append(cellModel.MotherCell(IDx, (0,0), 50, 50, 50, [50, 50, 50, 50, 50]))

    def retirePopulation (self, IDx):
        self.listID[IDx] = 0 #instancia cell no esta borrada creo



if __name__ == '__main__':
    goverment = Goverment()
    nature = nature.Nature(5)
    map = map.Map(100, nature.num_feeds)

    goverment.createPopulation()
    print "Iniciada la vida"
    goverment .retirePopulation(goverment .listID[0].ID)

    map.ploting()
