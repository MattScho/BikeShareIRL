import random
from abc import ABC
import abc

class SpatialEntityGenerator(ABC):
    '''
    Abstract class for a spatial entity generator
    Generates lists of spatial entities
    '''

    def __init__(self, systemSize:int):
        '''
        Initialize spatial entity generator base data

        :param xMin: minimum x location
        :param xMax: maximum x location
        :param distribution: generation distribution
        '''
        self.systemSize = systemSize

    def generateNSpatialEntities(self, numberOfSpatialEntities:int) -> list:
        '''
        Generate N spatial entities and return a list

        :param numberOfSpatialEntities: number of spatial entities to generate
        :return: list of generated spatial entities
        '''
        # Populate spatial entity layout
        return [self.generateSpatialEntity() for _ in range(numberOfSpatialEntities)]

    @abc.abstractmethod
    def generateSpatialEntity(self):
        '''
        Generate a single spatial entity

        :return: A single generated spatial entity
        '''
        return
