library(reticulate)
use_python('C:/Users/Bjoern/anaconda3/python.exe', required = T)
source_python("main.py")
a <- train_ai()

game <- tic_tac_toe()
get_ai_move(game, ruediger)
field.number <- ruediger$make_move(game$boxes, game$get_allowed_moves(ruediger$symbole), T)
