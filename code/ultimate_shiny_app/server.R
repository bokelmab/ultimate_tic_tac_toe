
# This is the server logic for a Shiny web application.
# You can find out more about building applications with Shiny here:
#
# http://shiny.rstudio.com
#
## libraries
library(shiny)
library(xtable)
library(magrittr)
library(reticulate)

## source files
source('../wrapper_functions/wrapper_functions_shiny.R')
source('../wrapper_functions/wrapper_functions_game.R')
source('../ai_objects/ki_rl.R')
source('../game_implementation/game.R')
source('../wrapper_functions/field_plot_class.R')
source('../wrapper_functions/input_translation_class.R')

## create ruediger
use_python('C:/Users/Bjoern/anaconda3/python.exe', required = T)
source_python("../../python_code/create_ultimate_python_environment.py")
source_python("../../python_code/python_functions.py")

## environment
myenv = environment()
number_training_games <- 1000

chosen.symbole <- 'empty'
games_per_row <- 3
field_representation <- field_representation(games_per_row)
input_translation <- input_translation(games_per_row)

shinyServer(function(input, output, session) {
  
  server.env <- environment() ## get environment name
  
  observeEvent(input$circle,{
    if(input$circle & chosen.symbole == 'empty'){
      assign('chosen.symbole', 'circle', myenv)
      assign('ai_player', train_ultimate_ai('cross', number_training_games), myenv)
      output$board <- renderPlot({
        
        field.number <- get_ultimate_ai_move(game, ai_player)
        make_move_on_ultimate_game(field.number[[1]], field.number[[2]], 'cross')
        
        symbole_coordinates <- input_translation$boxes2coordinates(game$boxes)
        get('field_representation', myenv)$add_symbols(symbole_coordinates$crosses, symbole_coordinates$circles)
        get('field_representation', myenv)$plot_field()
      })
    }
    
  })
  observeEvent(input$cross,{
    if(input$cross & chosen.symbole == 'empty'){
      assign('ai_player', train_ultimate_ai('circle', number_training_games), myenv)
      assign('chosen.symbole', 'cross', myenv)
    }
  })
  
  ## create board before first click
  output$board <- renderPlot({
    symbole_coordinates <- input_translation$boxes2coordinates(game$boxes)
    get('field_representation', myenv)$add_symbols(symbole_coordinates$crosses, symbole_coordinates$circles)
    get('field_representation', myenv)$plot_field()
  })
  
  ### interactive part of game (player makes moves) --------------------
  observeEvent(input$plot_click, {
    
    ## check whether symbol was choosen
    if(xor(input$cross, input$circle )){
      
      ## check whether circle has won
      if(!game$finished){
        
        ### add new coordinates --------------------------------------------
        mouse <- input$plot_click
        
        ## add new symbole to game
        mouse_x <- input_translation$translate_coordinates(mouse$x)
        mouse_y <- input_translation$translate_coordinates(mouse$y)
        field.number <- input_translation$coordinate2field(mouse_x, mouse_y)
        make_move_on_ultimate_game(field.number[1], field.number[2], chosen.symbole)
      }
      
      ## check whether cross has won
      if(!game$finished){
        
        ## add new circle to field
        field.number <- get_ultimate_ai_move(game, ai_player)
        make_move_on_ultimate_game(field.number[[1]], field.number[[2]], ifelse(chosen.symbole == 'circle', 'cross', 'circle'))
        
        ## check whether circle has won
        if(!game$winner %in% c('tie', chosen.symbole)){
          output$request <- renderText({'Sorry, Ruediger beat you!'})
        }
      }else{
        if(game$winner == chosen.symbole){
          output$request <- renderText({'Congratulation, you won!'})
        }
      }
    }
    
    ## plot board with symbols ------------------------------------------------
    output$board <- renderPlot({
      symbole_coordinates <- input_translation$boxes2coordinates(game$boxes)
      get('field_representation', myenv)$add_symbols(symbole_coordinates$crosses, symbole_coordinates$circles)
      get('field_representation', myenv)$plot_field()
    })
    game$print_boxes()
    print(field.number)
    
})
    
  #rsconnect::deployApp('C:/Users/Björn/Documents/Tennis/Hallentraining/Organisation_public')
  observeEvent(input$cross,{
    if(!(input$cross | input$circle) & !game$finished){
      output$request <- renderText({
        'Choose a symbole!'
      })
    }else if(!game$finished){
      output$request <- renderText({''})
    }
    })
  observeEvent(input$circle,{
    if(!(input$cross | input$circle) & !game$finished){
      output$request <- renderText({
        'Choose a symbole!'
      })
    }else if(!game$finished){
      output$request <- renderText({''})
    }
  })


})
