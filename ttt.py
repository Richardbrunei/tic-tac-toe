def check():
    for i in a:
        if i==["X","X","X"]:
            return 1
        if i==["O","O","O"]:
            return 2
    for i in range(3):
        b=[]
        for j in range(3):
            b.append(a[j][i])
        if b==["X","X","X"]:
            return 1
        if b==["O","O","O"]:
            return 2
    c=[]
    d=[]
    for i in range(3):
        c.append(a[i][i])
        d.append(a[i][2-i])
    #print(c)
    #print(d)
    if c==["X","X","X"]:
        return 1
    if c==["O","O","O"]:
        return 2
    if d==["X","X","X"]:
        return 1
    if d==["O","O","O"]:
        return 2
    for i in a:
        for j in i:
            if j==' ':
                return 0
    return 3
def show():
    for i in range(3):
        for j in range(2):
            print(a[i][j], end="|")
        print(a[i][2])
        if i!=2:
            print("-----")
    print()
def turn(player):
    x,y=input("Player "+str(player)+", its your turn: ").strip().split(" ")
    x=int(x)
    y=int(y)
    temp=" XO"
    while(a[y][x]!=" "):
        x,y=input("Nope, you cant go there. It's still your turn: ").strip().split(" ")
        x=int(x)
        y=int(y)
    a[y][x]=temp[player]
def init():
    global a
    a=[[" "," "," "] for i in range(3)]
def game():
    init()
    print("Welcome to tic tac toe\nCo ordinates are from the top left (so the top right would be (2,0))\n")
    show()
    cnt=0
    while(check()==0):
        turn(cnt+1)
        cnt+=1
        cnt%=2
        show()
    win=["","Player 1 wins","Player 2 wins","It's a tie"]
    print(win[check()])

if __name__=="__main__":
    game()
