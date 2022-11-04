# Helaman Chan
# CSE 210 W01 Prove Assignment: Tic Tac Toe Game


def main():
  player = 0
  while empty and victory():    
    board()
    player_input(player)
    player = int(not player)
  if not empty:
    print("It's a tie!")

square=['0','1','2','3','4','5','6','7','8','9']
empty = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def board():
  print(square[1]+'|'+square[2]+'|'+square[3])
  print('-+-+-')
  print(square[4]+'|'+square[5]+'|'+square[6])
  print('-+-+-')
  print(square[7]+'|'+square[8]+'|'+square[9])
  print()


def player_input(player):
  player_symbol = ['x','o']
  correct_input = True
  while True:
    try:
        position = int(input("{symbol}'s turn to choose a square(1-9): ".format(symbol = player_symbol[player])))
    except IndexError:
        print()
        print("Please enter a number within the board")
        print()
        continue
    except ValueError:
        print()
        print("Please enter a number")
        print()
        continue
    else:
        print()
    if square[position] == 'x' or square[position] == 'o':
        correct_input = False
    
    if not correct_input:
        print("Spot taken. Choose another square.")
        print()
        player_input(player)
    else:
        empty.remove(position)
        square[position] = player_symbol[player] 
        return 1

def victory():
  player_symbol = ['x','o']
  victory_conditions = [[1,2,3],[4,5,6],[7,8,9], #Horzontal
                        [1,4,7],[2,5,8],[3,6,9], #Vertical
                        [1,5,9],[3,5,7]] #Cross

  for check in victory_conditions:
    first_symbol = square[check[1]]
    if first_symbol != ' ':
      win = True
      for point in check:
        if square[point] !=  first_symbol:
          win = False
          break
      if win:
        board()
        if first_symbol == player_symbol[0]:
          print('x wins')
        else:
          print('o wins')
        print("Good game. Thank you for playing!")
        break
    else:
      win = False

  if win:
    return 0
  else:
    return 1


if __name__ == '__main__':
  main()