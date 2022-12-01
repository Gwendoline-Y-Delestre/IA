# ==============================================================================
"""HUNTER : implement a version of Treasure Hunter with two players"""
# ==============================================================================
__author__  = "Gwendoline Delestre"
__author__  = "Mathilda Gaulard"
__version__ = "3.0"
__date__    = "2020-06-05"
# ------------------------------------------------------------------------------
from ezTK import *
from random import randrange as rr
from ezCLI import *
#------------------------------------------------------------------------------
def score_file():
  """display best score"""
  
  global win
  win.exit()
  win = Win(title='Best Score', bg='#FFF', op=2)
  frame = Frame(win)
  ini = read_ini('best_score.ini')
  Label(frame, text = ini, font = 'Arial 12', height = 2)
  win.loop(); main()
#-------------------------------------------------------------------------------        
def score():
  """save the score"""
  
  best_score = 0
  if win.score_a > win.score_b:
    best_score = win.score_a
    name = name_a
  else:
     best_score = win.score_b
     name = name_b
  config = f"{rows},{cols},{nb_treasures}"
  if config not in read_ini('best_score.ini'):
    ini = write_ini('best_score.ini',f"\n[{config}]", -1)
  scores = read_ini('best_score.ini')
  config = f"{rows},{cols},{nb_treasures}"; high = scores[config]
  high[name] = best_score
  write_ini('best_score.ini', scores)
  #Recherches pour l'affichage en ordre décroissant:
  #d1 = dict(high)
  #d2 = sorted(d1.items(), key=lambda x: x[1],reverse=True)
  #print(d2)
  
  
# ------------------------------------------------------------------------------

def winner(row, col):
  """reveals the color of all the boxes and save the score and the name
  of the winner"""
  
  found_treasures = win.found_treasure.count(1)  
  if found_treasures == nb_treasures:
    for row in range(rows):
      for col in range(cols):
        for i in range(len(win.treasure)) :
         irow, icol = win.treasure[i] 
         distance = abs(irow - row) + abs(icol - col)
         win.distance[i] = distance
         final_distance = min(win.distance)
  
         if final_distance >= 15 :
           win.grid[row][col].state = 1
         elif 10 <= final_distance <= 14 :
           win.grid[row][col].state = 2
         elif 6 <= final_distance <= 9 :
           win.grid[row][col].state = 3
         elif 3 <= final_distance <= 5 :
           win.grid[row][col].state = 4
         elif 1 <= final_distance <= 2 :
           win.grid[row][col].state = 5
         elif final_distance == 0 :
           win.grid[row][col].state = 6
          
         win.grid[row][col]['text'] = final_distance
    
    score()    
# ------------------------------------------------------------------------------
def calcul_distance(row, col):
  """calcul the distance between two box"""

  win.distance = [0 for i in range(nb_treasures)]
  
  for i in range(len(win.treasure)) :  
    irow, icol = win.treasure[i] 
    distance = abs(irow - row) + abs(icol - col)
    win.distance[i] = distance
    if distance == 0:
      win.found_treasure[i] = 1  

  final_distance = min(win.distance)
  if win.Label_A_B['text'] == 'A':
      score = win.score_a
  else:
      score = win.score_b     

  if final_distance >= 15 :
    win.grid[row][col].state = 1
    score = score + 1
  elif 10 <= final_distance <= 14 :
    win.grid[row][col].state = 2
    score = score + 4   
  elif 6 <= final_distance <= 9 :
    win.grid[row][col].state = 3
    score = score + 9  
  elif 3 <= final_distance <= 5 :
    win.grid[row][col].state = 4
    score = score + 16 
  elif 1 <= final_distance <= 2 :
    win.grid[row][col].state = 5
    score = score + 25
  elif final_distance == 0 :
    win.grid[row][col].state = 6
    score = score + 36

  if win.Label_A_B['text'] == 'A':
      win.score_a = score
  else:
      win.score_b = score  
  win.grid[row][col]['text'] = final_distance
  win.Label_a['text'] = f"{name_a}\n{win.score_a}"
  win.Label_b['text'] = f"{name_b}\n{win.score_b}"
  
  winner(row, col)
# ------------------------------------------------------------------------------
def treasures():
  """create treasures"""

  win.treasure = [(rr(rows),rr(cols)) for i in range(nb_treasures)]
  for i in range (nb_treasures):
    irow, icol = win.treasure[i] 
# ------------------------------------------------------------------------------
def on_click(widget, code, mods):
  """callback function for all mouse events"""

  if widget.master != win.grid:
    return 
  
  row, col = widget.index 
  win.clic += 1
  if win.clic == 1:
     win.clic = 1
  if win.clic == 3:
     win.clic = -1
  calcul_distance(row, col)
  player()
# ------------------------------------------------------------------------------
def player():
  """tell who play """
  
  if win.clic == 1:
    win.player ='B'
    win.Label_A_B['text'] = win.player
  if win.clic == -1:
    win.player ='A'
    win.Label_A_B['text'] = win.player
# ------------------------------------------------------------------------------
def grid():
  """create the grid window and pack the widgets"""
  
  global win, nb_treasures, rows, cols, name_a, name_b

  rows, cols, nb_treasures = win.rowscale.state, win.colscale.state, win.goalscale.state
  name_a , name_b = win.entr1.state, win.entr2.state 
  win.exit() 
  win = Win(title='Hunter', click = on_click, bg='#FFF', op=2, grow=True) 
  win.score_a, win.score_b, win.player, win.clic = 0, 0, 'A', 0
  colors = ('#FFF', 'lightgrey', 'cyan', 'lime', 'yellow', 'red', '#000')
#------------------------------
  frame = Frame(win, flow = 'E', op = 1, bg = "#000")
  win.Label_a = Label(frame, text = f"{name_a}\n {win.score_a}", bg='#FFF', fg = '#000',
                      font = 'Arial 14', width = 8, height = 2)
  win.Label_A_B = Label(frame, text =f"{win.player}", fg = '#FFF', bg = '#000',
                        width = 2, height = 1,font = 'Arial 22 bold')
  win.Label_b = Label(frame, text = f"{name_b}\n {win.score_b}", bg='#FFF', fg = '#000',
                      font = 'Arial 14', width = 8, height = 2)
#------------------------------
  win.grid = Frame(win, fold=cols)
  for loop in range(rows*cols):
    Label(win.grid, height=1, width=2, bg=colors, border = 1)

  win.found_treasure = [0 for i in range(nb_treasures)]

  treasures()
# ----------------------------------------------------------------------------
  win.loop(); main() # relaunch 'config' when grid window is closed
# ------------------------------------------------------------------------------
def main():
  """create the main window and pack the widgets"""

  global win
  
  win = Win(title='Hunter', op=3)
  frame = Frame(win)
  Label(frame, text = 'CONFIGURATION', bg='#000', fg = '#FFF',
        font = 'Arial 18 bold', height = 2)
#------------------------------ 
  text = ''
  
  fr1 = Frame(win, flow='E')
  txt1 = Label(fr1, text = 'Name of player A :', anchor = 'W')
  win.entr1 = Entry(fr1, width = 15)
  win.label1 = Label(fr1, text=text)

  fr2 = Frame(win, flow='E')
  txt2 = Label(fr2, text = 'Name of player B :', anchor = 'W')
  win.entr2 = Entry(fr2, width = 15)
  win.label2 = Label(fr2, text=text) 
#------------------------------ 
  fr_principal = Frame(win, op=0, flow = 'S')
  fr3 = Frame(fr_principal, flow ='E')
  Label(fr3, text='Number of rows :', anchor='SW', width = 15)
  win.rowscale = Scale(fr3, scale=(12,24), state=12)
  
  fr4 = Frame(fr_principal, flow ='E')
  Label(fr4, text='Number of cols :', anchor='SW', width = 15)
  win.colscale = Scale(fr4, scale=(12,36), state=12)
  
  fr5 = Frame(fr_principal, flow ='E')
  Label(fr5, text='Number of goals :', anchor='SW', width = 15)
  win.goalscale = Scale(fr5, scale=(1,12), state=1)

  Button(win, text='START', command = grid, font = 'Arial 18 bold',
         bg = '#000', fg = '#FFF')
  Button(win, text='Best Score', command = score_file,
         font = 'Arial 18 bold', bg = '#000', fg = '#FFF')
  
  win.loop()
#------------------------------------------------------------------------------
if __name__ == '__main__':
  main()
