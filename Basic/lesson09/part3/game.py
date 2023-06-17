import os
import getch
import random



def generate_map(rows, cols):
  map = [['-']*cols for i in range(rows)]  
  map[0][0] = 'P' 
  return map  

def generate_object(map, rows, cols, obj_char):
  while True: 
    r_K = random.randint(0, rows-1) 
    c_K = random.randint(0, cols-1)  
    if map[r_K][c_K] == '-':   
      map[r_K][c_K] = obj_char
      break                    

def print_map(map, rows, cols):
  print()
  for r in range(rows):
    for c in range(cols):
      print(map[r][c], end=' ')
    print()

def move(map, rows, cols, ch, r_P, c_P):

  r_P_new = r_P  
  c_P_new = c_P
  if ch == 'W':   
    r_P_new = max(0, r_P-1)
  elif ch == 'S':  
    r_P_new = min(rows-1, r_P+1)
  elif ch == 'A': 
    c_P_new = max(0, c_P-1)
  elif ch == 'D':
    c_P_new = min(cols-1, c_P+1)
  
  value = map[r_P_new][c_P_new]  
  map[r_P][c_P] = '-'           
  map[r_P_new][c_P_new] = 'P'   

  return r_P_new, c_P_new, value


ROWS = 5 
COLS = 10 
map = generate_map(ROWS, COLS)
generate_object(map, ROWS, COLS, 'K')
generate_object(map, ROWS, COLS, 'D')

r_P = 0 
c_P = 0 
found_key = False 

os.system('clear') 
print_map(map, ROWS, COLS)
print('\n== THE ESCAPE GAME ==')
print('Use W A S D to move (P)layer.')
print('Find (K)ey first then exit through the (D)oor.')

count_key = 0
while True:

  ch = getch.getch().decode('utf-8').upper()

  r_P, c_P, value = move(map, ROWS, COLS, ch, r_P, c_P)
  
  if value == 'K': 
    found_key = True
    count_key += 1

  elif value == 'D': 

    os.system('clear')
    print_map(map, ROWS, COLS)

    if found_key: 
      print('YOU WON!!!')
    else:         
      print('YOU LOSE.')
      print('Maybe find the Key first?')
    break 

  os.system('clear')

  print_map(map, ROWS, COLS)