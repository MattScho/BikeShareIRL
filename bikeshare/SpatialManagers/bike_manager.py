from bikeshare.SpatialEntities.user import User
from bikeshare.Temporal.bike_temporal_handler import BikeTemporalHandler

class BikeManager:

    def __init__(self,systemSize:int, bikeLayout):
        '''
        Managers the Bikes in the simulation

        :param systemMin: system minimum boundary
        :param systemMax: system maximum boundary
        :param bikeLayout: initial layout of bike system
        '''
        # Manages bikes in transit
        self.bikeTemporalHandler = BikeTemporalHandler()

        self.systemSize = systemSize
        self.layout = bikeLayout

    def getLayout(self) -> list:
        '''
        Getter for current layout of the Bikes in the system
        :return:
        '''
        return self.layout

    def getCounts(self) -> list:
        '''
        Counts the number of Bikes per region
        :return: a list of the number of bikes per region
        '''
        # Initialize list with 0s
        counts = [0 for _ in range(self.systemSize)]

        # Count number of bikes per region
        for bike in self.getLayout():
            counts[int(bike.getLocationX())] += 1

        return counts

    def closestBikesFromUser(self, user:User) -> list:
        '''
        Find the closest bikes to a user

        :param user: User to find closest bikes to
        :return: [left closest Bike, right closest Bike]
        '''
        xLocation = user.getLocationX()
        return self.closestBikesFromLocation(xLocation)

    def closestBikesFromLocation(self, xLocation:float) -> list:
        '''
        Find closest Bikes to a given location
        If no Bike is found in a direction, that directions closest Bike will be returned as None

        :param xLocation: float location to find closest to
        :return: [left closest Bike, right closest Bike]
        '''
        # Initialize as None
        leftBike = None
        rightBike = None

        # Initialize at a distance larger than possible in the simulation
        leftBikeDist = 9999999
        rightBikeDist = 9999999

        for bike in self.layout:
            xLocationOfBike = bike.getLocationX()
            d = abs(xLocationOfBike - xLocation)

            # Is left
            if xLocationOfBike < xLocation:
                if d < leftBikeDist:
                    leftBikeDist = d
                    leftBike = bike
            # Is right
            elif xLocationOfBike >= xLocation:
                if d < rightBikeDist:
                    rightBikeDist = d
                    rightBike = bike
        return [leftBike, rightBike]

    def moveBike(self, bike, destination, speedMpS=7.0):
        '''

        :param bike:
        :param destination:
        :param speedMpS:
        :return:
        '''
        self.layout.remove(bike)

        distanceToTravel_km = abs(bike.getLocationX() - destination)
        distanceToTravel_m = distanceToTravel_km * 1000

        timeToTravel_seconds = distanceToTravel_m / speedMpS
        timeToTravel_minutes = timeToTravel_seconds / 60

        self.bikeTemporalHandler.addBike(bike, destination, timeToTravel_minutes)

    def passTime(self, minutesToPass:int):
        '''
        Handle the passage of time

        :param secondsToPass: number of seconds to pass in the simulation
        '''
        # Pass time, retrieve any returned bikes
        arrived = self.bikeTemporalHandler.passTime(minutesToPass)
        # Add those returned bikes to the layout
        self.layout.extend(arrived)
