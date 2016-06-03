import cellModel
import map
import nature


class Goverment:
    ''' manage population '''
    def __init__(self ):
        self.listID = []

    def createPopulation(self):
        IDx = len(goverment_i.listID)
        self.listID.append(cellModel.MotherCell(IDx, (5,5), 50, 50, 50, [50, 50, 50, 50, 50]))

    def retirePopulation (self, IDx):
        self.listID[IDx] = 0 #instancia cell no esta borrada creo



if __name__ == '__main__':
    goverment_i = Goverment()
    nature_i = nature.Nature(5)
    map_i = map.Map(100, nature_i.num_feeds)

    goverment_i.createPopulation()
    cell = goverment_i.listID[0]

    print "Iniciada la vida"

    goverment_i.retirePopulation(goverment_i.listID[0].ID)

    map_i.ploting()

