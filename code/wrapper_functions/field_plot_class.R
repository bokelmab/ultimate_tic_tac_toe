field_representation <- function(p_sub_games_row){
  
  field_representation_env <- environment()
  sub_games_row <- p_sub_games_row
  crosses <- NULL
  circles <- NULL
  
  output <- list(
    
    add_symbols = function(p_crosses, p_circles){
      
      assign('crosses', p_crosses, field_representation_env)
      assign('circles', p_circles, field_representation_env)
    },
    
    plot_field = function(){
      
      ## specify range of field
      max_range <- sub_games_row
      plot(x = c(0.33, 0.33), y = c(0, 1), type = 'l', xlim = c(0, max_range), ylim = c(0, max_range), 
           xlab = '', ylab = '', xaxt='n', yaxt='n', xaxs = "i", yaxs = "i")
      #box(lty = 1, lwd = 3)
      
      ## draw lines
      for(i_sub_game in 0:(get('sub_games_row', field_representation_env)-1)){
        
        ## lines within field
        abline(h = 0.33 + i_sub_game, lwd = 2)
        abline(v = 0.33 + i_sub_game, lwd = 2)
        abline(h = 0.66 + i_sub_game, lwd = 2)
        abline(v = 0.66 + i_sub_game, lwd = 2)
        
        ## lines around field
        abline(h = i_sub_game, lwd = 3)
        abline(v = i_sub_game, lwd = 3)
        
      }
      
      ## draw symbols
      points(get('crosses', field_representation_env), pch = 4, cex = 10 / get('sub_games_row', field_representation_env), lwd = 5)
      points(get('circles', field_representation_env), col = 'red', cex = 10 / get('sub_games_row', field_representation_env), lwd = 5)
      
    }
    
  )
  
}