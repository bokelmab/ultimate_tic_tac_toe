## define path
import sys
sys.path.append('C:/R_Projects/ultimate_tic_tac_toe/python_code/game')
sys.path.append('C:/R_Projects/ultimate_tic_tac_toe/python_code/player')

## required classes
from ultimate_tic_tac_toe_class import * 
from player_class_interface import *
from player_class import *
from Reinforcement_learner_class import *
from reinforcement_inherit1_class import *
from random_player_class import *
from ultimate_learner import *

game = ultimate_tic_tac_toe()

