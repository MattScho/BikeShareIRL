import string
import random
import pickle as pkl

class EnvironmentDefinition:

    def __init__(self, title:str, systemSize:int, budget:int, users, bikeLayout):
        self.systemSize = systemSize
        self.budget = budget
        self.users = users
        self.bikeLayout = bikeLayout

        letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
        self.code = ''.join(random.choice(letters) for i in range(10))
        self.title = title

    def getSystemSize(self)->int:
        return self.systemSize

    def getBudget(self)-> int:
        return self.budget

    def getUsers(self)->list:
        return self.users.copy()

    def getBikeLayout(self) -> list:
        return self.bikeLayout.copy()

    def getCode(self):
        return self.code

    def getTitle(self):
        return self.title

    def dumpToFile(self):
        file = "Experiment_{title}_{code}.bikeshare".format(
            title=self.title, code=self.code
        )
        fileHandle = open(file, "wb+")
        pkl.dump(self, fileHandle)
        fileHandle.close()
