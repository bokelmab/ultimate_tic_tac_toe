library(reticulate)
use_python('C:/Users/Bjoern/anaconda3/python.exe', required = T)
source_python("python_code/create_ultimate_python_environment.py")
source('code/wrapper_functions/input_translation_class.R')
input_translation <- input_translation(3)
symbole_coordinates <- input_translation$boxes2coordinates(game$boxes)


a <- train_ai()

game <- tic_tac_toe()
get_ai_move(game, ruediger)
field.number <- ruediger$make_move(game$boxes, game$get_allowed_moves(ruediger$symbole), T)
