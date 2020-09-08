from bikeshare.SpatialEntities.bike import Bike
from bikeshare.SpatialEntityGenerators.spatial_entity_generator import SpatialEntityGenerator
from bikeshare.utils.distributions.distribution import Distribution

class BikeGenerator(SpatialEntityGenerator):
    '''
    Implements Spatial Entity Generator

    Handles generating bikes
    '''

    def __init__(self, systemSize:int, distribution:Distribution):
        '''
        Initialiase bike generator

        '''
        super().__init__(systemSize)
        self.distribution = distribution

    def generateSpatialEntity(self) -> Bike:
        '''
        Generate a single bike

        :return: generated bike
        '''
        xLocation = self.distribution.generate()
        return Bike(xLocation)


