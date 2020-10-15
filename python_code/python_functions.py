# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 13:59:48 2020

@author: Björn
"""

## required packages
# import sys
# 
# 
# ## append path
# sys.path.append('C:/R_Projects/tic_tac_toe_Python/learner_classes')
# sys.path.append('C:/R_Projects/tic_tac_toe_Python')

## required classes
# from tic_tac_toe_class import * 
# from player_class import *
# from Reinforcement_learner_class import *
# from reinforcement_inherit1_class import *
# from random_player_class import *
# 
# game = tic_tac_toe()

from Reinforcement_learner_class import *
from random_player_class import *

def get_ai_move(p_game, p_ai):
  field_number = p_ai.make_move(p_game.boxes, p_game, p_exploit = True)
  return field_number

def make_move_on_game(p_field_number, p_symbole):
  game.move(int(p_field_number), str(p_symbole))
  
def train_ai(p_symbole, p_number_games):
  
  print('Start training of ai player')
  p_number_games = int(p_number_games)
  
  ## Creation of player objects depending on choice of symbole
  if(p_symbole == 'cross'):
    player_cross = reinforcement_learner('player_cross', 'cross')
    player_circle = random_player()
  else:
    player_circle = reinforcement_learner('player_circle', 'circle')
    player_cross = random_player()
    
  ## training
  for i_game in range(1, p_number_games + 1):
    
    game = simple_tic_tac_toe() ## define game
    while game.finished == False:
        game.move(player_cross.make_move(game.boxes, game), 'cross')
        
        if(game.finished == False):
            game.move(player_circle.make_move(game.boxes, game), 'circle')
    
    if(game.winner == 'cross'):
        player_cross.update_value_function(1)
        player_circle.update_value_function(0)
    if(game.winner == 'circle'):
        player_cross.update_value_function(0)
        player_circle.update_value_function(1)
    if(game.winner == 'tie'):
        player_cross.update_value_function(1/2)
        player_circle.update_value_function(1/2)
  
        
  ## output
  print('Finished training ai player. Let us begin!' )
  if(p_symbole == 'cross'):
    return player_cross
  else:
    return player_circle
    

  
 

