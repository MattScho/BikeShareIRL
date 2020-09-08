from bikeshare.SpatialEntities.spatialentity import SpatialEntity

class User(SpatialEntity):
    '''
    User object in BikeShare simulations
    '''

    def __init__(self, locationX:float, destinationX:float):
        '''
        Init user object with a location

        :param locationX: location X to start
        :param destinationX: intended destination
        '''
        super().__init__(locationX)

        # The user's target destination
        self.destinationX = destinationX

    def getDestination(self) -> float:
        '''
        Getter for destination

        :return: get intended destination
        '''
        return self.destinationX

    def setDestination(self, newDestinationX:float):
        '''
        Setter for destination

        :param newDestinationX: the new intended destination
        '''
        self.destinationX = newDestinationX

    def getDistanceFromDestination(self) -> float:
        '''
        Calculate the distance from intended destination

        :return: distance from intended destination
        '''
        return self.distanceToLocation(self.destinationX)

    def isEntityTowardsDestination(self, spatialEntity:SpatialEntity) -> bool:
        '''
        Check if a spatial entity is closer to the user's destination than the user currently is?

        :param spatialEntity: spatial entity to check
        :return: Is the spatial entity closer to the destination than the user currently is?
        '''
        return self.getDistanceFromDestination() > spatialEntity.distanceToLocation(self.destinationX)

    def costToMoveToLocation(self, otherLocationX:float) -> float:
        '''
        Calculate the cost to move to a location X

        :param locationX: location to find cost to move to
        :return: the distance to the location
        '''
        if abs(self.locationX - otherLocationX) >= 2.0:
            return 999.9
        else:
            return self.distanceToLocation(otherLocationX) ** 2

    def costToMoveToEntity(self, spatialEntity:SpatialEntity) -> float:
        '''
        Calculate the cost to move to an entity

        :param entity: entity to find the cost to move to
        :return: the cost to move to the entity
        '''
        return self.costToMoveToLocation(spatialEntity.getLocationX())

    def utilityToGoToEntityWithIncentive(self, spatialEntity:SpatialEntity, incentive:float) -> float:
        '''
        The user's utility cost to move to a spatial entity

        :param spatialEntity: spatial entity to move to
        :param incentive: incentive to move to the spatial entity
        :return: utility to move
        '''
        return incentive - self.costToMoveToEntity(spatialEntity)
