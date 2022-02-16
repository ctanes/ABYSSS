from skin_model import *
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer


def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": "red",
                 "r": 0.2}
    return portrayal

grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)
server = ModularServer(Skin,
                       [grid],
                       "Skin Infection Model",
                       {"N_bacteria":5, "width":10, "height":10})
server.port = 8521 # The default
server.launch()