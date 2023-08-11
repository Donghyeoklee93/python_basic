

while True:
    x = int(input("[Enter the number]\n1.Start Game 2.See Ranking 3.Shut down >>>"))
    if x == 1:
        print("Start game")
    elif x == 2:
        print("Print real-time ranking")
    elif x == 3:
        print("Shut down the game")
        break
    else:
        print("Please enter number again")