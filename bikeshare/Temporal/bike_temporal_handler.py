from bikeshare.SpatialEntities.bike import Bike

class BikeTemporalHandler:
    """
    Manage temporal management of moving bikes
    """

    def __init__(self):
        self.temporalList = []

    def addBike(self, bike:Bike, destination:float, ttlMinutes:int):
        '''
        Adds a bike to temporal management

        :param bike: Bike to add
        :param destination: target destination as float
        :param ttlMinutes: number of minutes (int) to travel
        '''
        self.temporalList.append(_BikeInMotion(bike, destination, ttlMinutes))

    def passTime(self, amountOfTimeMinutes:int) -> list:
        '''
        Pass an amount of time, the Bikes that arrive during that time are returned as a list

        :param amountOfTimeMinutes: time (int) to pass
        :return: list of Bikes that returned in that time
        '''
        arrived = []
        # Iterate through each bike
        for bikeInMotion in self.temporalList:
            finishedBike = bikeInMotion.passTime(amountOfTimeMinutes)
            # Bike has arrived, remove it from temporal list
            # add it to arrived list
            if finishedBike is not None:
                self.temporalList.remove(bikeInMotion)
                arrived.append(finishedBike)
        return arrived


class _BikeInMotion:
    """
    Wrapper class for a Bike traveling over some amount of time to a destination
    """

    def __init__(self, bike:Bike, destination:float, ttlMinutes:int):
        self.ttlMinute = ttlMinutes
        self.bike = bike
        self.destination = destination

    def getBike(self) -> Bike:
        '''
        Get underlying Bike from wrapper
        :return:
        '''
        return self.bike

    def getTTLMinutes(self) -> int:
        '''
        Accessor for TTL, remaining traveling time for Bike
        :return: Bike's travel TTL
        '''
        return self.ttlMinute

    def passTime(self, amount:int):
        '''
        Pass time for a Bike
        '''
        self.ttlMinute -= amount

        if self.ttlMinute <= 0:
            self.bike.setLocationX(self.destination)
            return self.bike
        else:
            return None
