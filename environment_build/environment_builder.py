from environment_build.environment_definition import EnvironmentDefinition
from bikeshare.SpatialEntities.bike import Bike
from bikeshare.SpatialEntities.user import User
from bikeshare.utils.distributions.betavariate_distribution import BetaVariateDistribution


for systemSize in [5,10,15]:
    for numberOfBikes in [50,100,150]:
        for budget in [0, 100, 200, 300]:
            for i in [["1", .5, .5], ["2", 5, 1], ["3", 1, 3], ["4", 2, 2], ["5", 2, 5]]:
                for j in [["1", .5, .5], ["2", 5, 1], ["3", 1, 3], ["4", 2, 2], ["5", 2, 5]]:
                    beta1 = BetaVariateDistribution(min=0, max=systemSize, alpha=i[1], beta=i[2])
                    beta2 = BetaVariateDistribution(min=0, max=systemSize, alpha=j[1], beta=j[2])
                    users = []
                    for hour in range(24):
                        hourly = []
                        for _ in range(30):
                            hourly.append(User(beta1.generate(), beta2.generate()))
                        users.append(hourly)

                    for k in [["1", .5, .5], ["2", 5, 1], ["3", 1, 3], ["4", 2, 2], ["5", 2, 5]]:
                        beta = BetaVariateDistribution(min=0, max=systemSize, alpha=k[1], beta=k[2])
                        bikeLayout = []
                        for _ in range(numberOfBikes):
                            bikeLayout.append(Bike(beta.generate()))
                        title = "Daily_Size{size}_NumberOfBikes{numberOfBikes}_budget{budget}_userBetaDept{userBetaDept}" \
                                "_userBetaArriv{userBetaArriv}_bikeBeta{bikes}".format(
                            size=systemSize,
                            numberOfBikes=numberOfBikes,
                            budget=budget,
                            userBetaDept=i[0],
                            userBetaArriv=j[0],
                            bikes=k[0]
                        )
                        print(title)
                        environmentDefinition = EnvironmentDefinition(title=title, systemSize=systemSize, budget=budget, users=users, bikeLayout=bikeLayout)
                        environmentDefinition.dumpToFile()