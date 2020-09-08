import math

class SpatialEntity:
    '''
    abstract Spatial Entity class for bike share environment
    '''

    def __init__(self, locationX:float):
        '''
        Initialize a Spatial Entity

        :param locationX: X location of spatial entity
        '''
        self.locationX = locationX

    def getLocationX(self) -> float:
        '''
        Get location X of the entity

        :return: X location
        '''
        return self.locationX

    def setLocationX(self, newLocationX:float):
        '''
        Set location X of the entity

        :param newLocationX: new location X of the entity
        '''
        self.locationX = newLocationX

    def distanceToLocation(self, otherX:float) -> float:
        '''
        Uses root square distance calculation for extendability in the future

        :param otherX: other X location to find distance to
        :return: distance to other X
        '''
        return math.sqrt((self.locationX - otherX) ** 2)


    def distanceToSpatialEntity(self, otherEntity) -> float:
        '''
        Finds the distance from another spatial entity

        :param otherEntity: other spatial entity to compare to
        :return: distance from another spatial entity
        '''
        return self.distanceToLocation(otherEntity.getLocationX())



