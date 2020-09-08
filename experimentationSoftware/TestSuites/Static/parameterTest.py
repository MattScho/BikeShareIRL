from experimentationSoftware.utilities.fileIO import dumpObject
from experimentationSoftware.Agents.experiment import Experiment

from bikeshare.BikeShareController import BikeShareController

from stable_baselines import PPO1, PPO2, ACKTR, TRPO
from stable_baselines.common.policies import MlpPolicy
from stable_baselines import results_plotter
from stable_baselines.bench import Monitor
import pickle as pkl
import time
import matplotlib.pyplot as plt
import os
import glob

experimentFiles = glob.glob("../../../environments/*")
# Only use a few for testing the system, use all experiments on a powerful system
experimentFiles = experimentFiles[:10]
experiments = []

for experimentFile in experimentFiles:
    for alg in ["PPO2", "ACKTR", "TRPO"]:
        experiment = pkl.load(open(experimentFile, 'rb'))
        title = alg + "_" + experiment.getTitle()
        if not os.path.isdir("monitorFiles/" + title+"/"):
            os.makedirs("monitorFiles/" + title+"/")
        if alg == "PPO2":
            experiments.append(Experiment(title, PPO2(MlpPolicy, Monitor(BikeShareController(experiment), "monitorFiles/" + title+"/"))))
        elif alg == "ACKTR":
            experiments.append(Experiment(title, ACKTR(MlpPolicy, Monitor(BikeShareController(experiment), "monitorFiles/" + title+"/"))))
        elif alg == "TRPO":
            experiments.append(Experiment(title, TRPO(MlpPolicy, Monitor(BikeShareController(experiment), "monitorFiles/" + title+"/"))))

results = {}
for experiment in experiments:
    timeSteps = 240000
    start = time.time()
    print(str(experiment))
    results[str(experiment)] = experiment.run(30, timeSteps)
    print(time.time() - start)
    results_plotter.plot_results(["monitorFiles/" + experiment.title+"/"], timeSteps, results_plotter.X_TIMESTEPS, experiment.title)

    plt.savefig("charts/" + experiment.title + ".png")
    dumpObject(results, "results/resultsBudget.pkl")