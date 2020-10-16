input_translation <- function(p_sub_games_row){
  
  input_translation_env <- environment()
  sub_games_row <- p_sub_games_row
  
  output <- list(
    
    translate_coordinates = function(p_coordinate){
      
      game_number <- floor(p_coordinate)
      
      coord_round <- floor((p_coordinate - game_number) * 3)
      
      return(1/6 + coord_round/3 + game_number)
    
    },
    
    coordinate2field = function(p_xcoord, p_ycoord){
      
      ## get valid field coordinates
      xcoord <- output$translate_coordinates(p_xcoord)
      ycoord <- output$translate_coordinates(p_ycoord)
      
      ## sub game number
      x_game <- floor(xcoord)
      y_game <- floor(ycoord)
      game_Python <- x_game + 3 * (2 - y_game)
      
      ## get field number
      x_box <- xcoord - x_game
      y_box <- ycoord - y_game
      x_box <- (6 * x_box) %/% 2 + 1
      y_box <- (6 * y_box) %/% 2 + 1
      
      y_box <- 4 - y_box
      
      field_R <- x_box + 3 * (y_box-1)
      field_Python <- field_R - 1 ## conversion to python index
      
      ## output according to game type
      if(get('sub_games_row', input_translation_env) > 1){
        return(c(game_Python, field_Python))
      }else{
        return(field_Python)
      }
      
    },
    
    field2coordinate = function(p_field){
      
      if(length(p_field) == 2){ ## ultimate game
        field_first <- p_field[[1]]
        field_last <- p_field[[2]]
      }else{                    ## simple game
        field_first <- 0
        field_last <- p_field
      }
      
      field_last <- field_last + 1 ## conversion to R index
      x.coord <- field_last %% 3
      if(x.coord == 0){
        x.coord <- 3
      }
      y.coord <- (field_last - x.coord) %/% 3 + 1
      y.coord <- 4 - y.coord
      
      x.coord <- (1 + 2 * (x.coord - 1)) / 6
      y.coord <- (1 + 2 * (y.coord - 1)) / 6
      
      ## adjust coordinates by number of sub game
      x.coord <- x.coord + (field_first %% 3)
      y.coord <- y.coord + get('sub_games_row', input_translation_env) - 1 - (field_first %/% 3)
      
      
      return(c(x.coord, y.coord))
    },
    
    boxes2coordinates = function(p_boxes){
      
      crosses <- NULL
      circles <- NULL
      for(i_box in 1:length(p_boxes)){
        
        if(typeof(p_boxes[i_box]) %in% c('double', 'integer')){ ## simple tic tac toe
          if(p_boxes[i_box] == 1){ ## cross in box
            crosses %<>% rbind(output$field2coordinate(i_box - 1)) ## python index
          }
          if(p_boxes[i_box] == 2){ ## circle in box
            circles %<>% rbind(output$field2coordinate(i_box - 1)) ## python index
          }
        }else{ ## ultimate tic tac toe
          for(i_field in 1:length(p_boxes[[i_box]]$boxes)){
            if(p_boxes[[i_box]]$boxes[i_field] == 1){ ## cross in box
              crosses %<>% rbind(output$field2coordinate(c(i_box - 1, i_field - 1))) ## python index
            }
            if(p_boxes[[i_box]]$boxes[i_field] == 2){ ## circle in box
              circles %<>% rbind(output$field2coordinate(c(i_box - 1, i_field - 1))) ## python index
            }
          }
        }
        
      }
      return(list(crosses = crosses, circles = circles))
    }
  )
  
}