# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 18:29:41 2020

@author: Björn
"""

## define path
import sys
sys.path.append('C:/R_Projects/ultimate_tic_tac_toe/python_code/game')
sys.path.append('C:/R_Projects/ultimate_tic_tac_toe/python_code/player')
sys.path.append('C:/R_Projects/ultimate_tic_tac_toe/python_code')

## required classes
from simple_tic_tac_toe import * 
from player_class_interface import *
from player_class import *
from Reinforcement_learner_class import *
from reinforcement_inherit1_class import *
from random_player_class import *
from python_functions import *
from ultimate_tic_tac_toe_class import *
from ultimate_player import *

ultimate_game = ultimate_tic_tac_toe()
ruediger = train_ai('cross', 1000)
ultimate_player = ultimate_player('ruediger', ruediger)
ultimate_game.print_boxes()
ultimate_game.move(ultimate_player.make_move(ultimate_game), 'cross')
ultimate_game.print_boxes()
ultimate_game.move((1,8), 'circle')
ultimate_game.print_boxes()
ultimate_game.move(ultimate_player.make_move(ultimate_game), 'cross')
ultimate_game.print_boxes()
ultimate_game.move((6,8), 'circle')
ultimate_game.print_boxes()
ultimate_game.move(ultimate_player.make_move(ultimate_game), 'cross')
ultimate_game.print_boxes()


ultimate_game.move((8,8), 'circle')
ultimate_game.print_boxes()
ultimate_game.boxes[8].print_boxes()

#a = train_ai('cross', 100)

game = simple_tic_tac_toe()


game.print_boxes()
game.move(1)
game.print_boxes()
game.move(2)
game.print_boxes()
game.move(4)
game.print_boxes()
game.move(5)
game.print_boxes()
game.winner
game.move(7)
game.winner




game.winner
ruediger.make_move(game.boxes, game)



ultimate_game.move((0,0), 'cross')
ultimate_game.print_boxes()
ultimate_game.move((0,3), 'circle')
ultimate_game.print_boxes()
ultimate_game.move((0,1), 'cross')
ultimate_game.move((0,4), 'circle')
ultimate_game.move((0,2), 'cross')
ultimate_game.boxes[0].winner
ultimate_game.winner
game = tic_tac_toe()


ruediger.symbole

