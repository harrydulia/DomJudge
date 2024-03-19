player1,player2 = map (str,input().split())
#[Y]剪刀[O]石頭[X]布和玩家2出的拳：[Y]剪刀[O]石頭[X]布

if player1 == player2:
    print("0")
    exit() 

if (player1 == 'Y' and player2 == 'X') or (player1 == 'O' and player2 == 'Y') or (player1 == 'X' and player2 == 'O'):
    print("1")
else:
    print("2")