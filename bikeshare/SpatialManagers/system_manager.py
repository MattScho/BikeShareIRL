from bikeshare.SpatialManagers.bike_manager import BikeManager
from bikeshare.SpatialManagers.user_manager import UserManager

class SystemManager:
    """

    """
    def __init__(self, systemSize:int=10, budget=180, userLayout=None, bikeLayout=None):
        '''
        High level maintenance
        '''

        self.systemSize = systemSize
        self.budget = budget
        self.users = userLayout
        self.bikeManager = BikeManager(self.systemSize, bikeLayout)
        self.userManager = UserManager(self.systemSize)


    def getLayout(self):
        return self.bikeManager.getLayout()

    def getCounts(self):
        return self.bikeManager.getCounts()

    def runWithIncentive(self, incentives, minutesToRun:int, turn:int):
        unservice = 0
        noOp = 0
        for user in self.users[turn-1]:

            closestBikes = self.bikeManager.closestBikesFromUser(user)
            rightBike = closestBikes[0]
            leftBike = closestBikes[1]

            closestBike = None

            if rightBike is None:
                if leftBike is None:
                    unservice += 1
                else:
                    closestBike = leftBike
            elif leftBike is None:
                if rightBike is None:
                    unservice += 1
                else:
                    closestBike = rightBike
            else:
                if user.distanceToSpatialEntity(leftBike) >= user.distanceToSpatialEntity(rightBike):
                    closestBike = rightBike
                else:
                    closestBike = leftBike

            if closestBike is not None:
                if user.distanceToSpatialEntity(closestBike) < 1.0:
                    self.bikeManager.moveBike(closestBike, user.getDestination())
                else:
                    if 0 <= user.utilityToGoToEntityWithIncentive(closestBike, incentives[int(closestBike.getLocationX())]) and self.budget >= incentives[int(closestBike.getLocationX())]:
                        self.bikeManager.moveBike(closestBike, user.getDestination())
                        self.budget -= incentives[int(closestBike.getLocationX())]
                        noOp += 1
                    else:
                        unservice += 1


        self.bikeManager.passTime(minutesToRun)

        return unservice / 30, (unservice + noOp) / 30