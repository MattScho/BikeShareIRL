from bikeshare.SpatialEntities.user import User
from bikeshare.SpatialEntityGenerators.spatial_entity_generator import SpatialEntityGenerator
from bikeshare.utils.distributions.betavariate_distribution import BetaVariateDistribution
from bikeshare.utils.distributions.distribution import Distribution
import pickle as pkl

class UserGenerator(SpatialEntityGenerator):
    '''
    Implements Spatial Entity Generator

    Handles generating users
    '''

    def __init__(self, systemSize:int, departureDistribution:Distribution, arrivalDistribution:Distribution):
        '''
        Initialiase user generator

        :param systemSize: size of the system
        :param departureDistribution: distribution to generate departure intentions
        :param arrivalDistribution: distribution to generate arrival intentions
        '''
        super().__init__(systemSize)
        self.arrivalDistribution = arrivalDistribution
        self.departureDistribution = departureDistribution

    def generateSpatialEntity(self) -> User:
        '''
        Generate a single bike

        :return: generated bike
        '''
        xLocation = self.departureDistribution.generate()
        xDestination = self.arrivalDistribution.generate()
        return User(xLocation, xDestination)
