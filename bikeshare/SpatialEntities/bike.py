from bikeshare.SpatialEntities.spatialentity import SpatialEntity

class Bike(SpatialEntity):
    '''
    Bike object in BikeShare simulations
    '''
    idInc = 0

    def __init__(self, locationX:float, available:bool=True):
        '''
        Init bike object with a location

        :param locationX: location X to start
        :param available: can the bike be used
        '''
        super().__init__(locationX)

        # Set identifier of bike and increment it
        self.identifier = Bike.idInc
        Bike.idInc += 1

        # Is the bike available for use
        self.available = available


    def isAvailable(self) -> bool:
        '''
        :return: Is the bike available?
        '''
        return self.available

    '''
    I chose two distinct setters as it is a boolean variable
    and I feel that it adds clarity if this is an issue use:
    
    def setAvailability(self, available:bool):
        self.available = available
    '''
    def setNotAvailable(self):
        '''
        Make the bike unavailable for use
        '''
        self.available = False

    def setAvailable(self):
        '''
        Make the bike available for use
        '''
        self.available = True
