## define path
import sys
sys.path.append('C:/R_Projects/tic_tac_toe_R_Python/python_code/game')
sys.path.append('C:/R_Projects/tic_tac_toe_R_Python/python_code/player')

## required classes
from simple_tic_tac_toe import * 
from player_class_interface import *
from player_class import *
from Reinforcement_learner_class import *
from reinforcement_inherit1_class import *
from random_player_class import *

game = simple_tic_tac_toe()


