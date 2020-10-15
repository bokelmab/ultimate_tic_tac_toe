
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
source('../wrapper_functions/field_plot_class.R')
source('../ai_objects/ki_rl.R')
source('../game_implementation/game.R')

## create ruediger
use_python('C:/Users/Bjoern/anaconda3/python.exe', required = T)
source_python("../../python_code/create_python_environment.py")
source_python("../../python_code/python_functions.py")

## environment
myenv = environment()
circles <- NULL ## coordinates of circles
crosses <- NULL ## coordinates of crosses
number_training_games <- 1000
field_representation <- field_representation(1)

chosen.symbole <- 'empty'

shinyServer(function(input, output, session) {
  
  server.env <- environment() ## get environment name
  
  observeEvent(input$circle,{
    if(input$circle & chosen.symbole == 'empty'){
      assign('chosen.symbole', 'circle', myenv)
      assign('ai_player', train_ai('cross', number_training_games), myenv)
      output$board <- renderPlot({
        
        field.number <- get_ai_move(game, ai_player)
        make_move_on_game(field.number, 'cross')
        crosses %<>% rbind(field2coordinate(field.number))
        assign('crosses', crosses, server.env)
        
        get('field_representation', myenv)$add_symbols(crosses, circles)
        get('field_representation', myenv)$plot_field()
      })
    }
    
  })
  observeEvent(input$cross,{
    if(input$cross & chosen.symbole == 'empty'){
      assign('ai_player', train_ai('circle', number_training_games), myenv)
      assign('chosen.symbole', 'cross', myenv)
    }
  })
  
  ## create board before first click
  output$board <- renderPlot({
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
        mouse.x <- translate.coordinates(mouse$x) ## mid point of chosen box
        mouse.y <- translate.coordinates(mouse$y) ## mid point of chosen box
        
        ## add new symbole to game
        make_move_on_game(coordinate2field(mouse.x, mouse.y), chosen.symbole)
        if(chosen.symbole == 'cross'){
          crosses %<>% rbind(c(mouse.x, mouse.y)) ## add mouse coordinates to cross coordinates
        }
        if(chosen.symbole == 'circle'){
          circles %<>% rbind(c(mouse.x, mouse.y)) ## add mouse coordinates to circle coordinates
        }
      }
      
      ## check whether cross has won
      if(!game$finished){
        
        ## add new circle to field
        field.number <- get_ai_move(game, ai_player)
        make_move_on_game(field.number, ifelse(chosen.symbole == 'circle', 'cross', 'circle'))
        if(chosen.symbole == 'circle'){
          crosses %<>% rbind(field2coordinate(field.number))
        }else{
          circles %<>% rbind(field2coordinate(field.number))
        }
        
        ## check whether circle has won
        if(!game$winner %in% c('tie', chosen.symbole)){
          output$request <- renderText({'Sorry, Ruediger beat you!'})
        }
      }else{
        if(game$winner == chosen.symbole){
          output$request <- renderText({'Congratulation, you won!'})
        }
      }
      
      assign('crosses', crosses, server.env)
      assign('circles', circles, server.env)
    }
    
    ## plot board with symbols ------------------------------------------------
    output$board <- renderPlot({
      get('field_representation', myenv)$add_symbols(crosses, circles)
      get('field_representation', myenv)$plot_field()
    })
    
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
