from random import randint

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

def checkstate(state):
    for i in state:
        if i==["X","X","X"]:
            return 1
        if i==["O","O","O"]:
            return 2
    for i in range(3):
        b=[]
        for j in range(3):
            b.append(state[j][i])
        if b==["X","X","X"]:
            return 1
        if b==["O","O","O"]:
            return 2
    c=[]
    d=[]
    for i in range(3):
        c.append(state[i][i])
        d.append(state[i][2-i])
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
    for i in state:
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
    
def turn(player,inv):
    x,y=input("Player "+str(player)+", its your turn: ").strip().split(" ")
    x=int(x)
    y=int(y)
    temp=" XO"
    while(True):
        if ((x>=0 and x<3) and (y>=0 and y<3)):
            if(inv):
                if a[x][y]==" ":
                    break
            else:    
                if a[y][x]==" ":
                    break
        x,y=input("Nope, you cant go there. It's still your turn: ").strip().split(" ")
        x=int(x)
        y=int(y)
    if inv:
        a[x][y]=temp[player]
    else:   
        a[y][x]=temp[player]
    
def init():
    global a
    inverted=False
    a=[[" "," "," "] for i in range(3)]
        
def AIturn(player):
    blanks=[]
    opposite=[0,2,1]
    temp=" XO"
    for i in range(3):
        for j in range(3):
            if(a[i][j]==" "):
                blanks.append((i,j))
    choos=0
    mx=-1
    for i in range(len(blanks)):
        #a[blanks[i][0]][blanks[i][1]]=temp[opposite[player]]
        cpy=[]
        for j in a:
            cpy.append(j[:])
        cpy[blanks[i][0]][blanks[i][1]]=temp[player]
        k=minimax(cpy,0,False,-999,999,player);
        if k>mx:
            choos=i
            mx=k
        #print(k)
        #a[blanks[i][0]][blanks[i][1]]=" "
    """for i in range(len(blanks)):
        a[blanks[i][0]][blanks[i][1]]=temp[player]
        if check()==player:
            choos=i
        a[blanks[i][0]][blanks[i][1]]=" " """
    a[blanks[choos][0]][blanks[choos][1]]=temp[player]
    print("The (slightly more intelligent) AI has made a move :)")

def minimax(state,depth,alpha,beta,turn,aiturn):
    if checkstate(state)!=0:
        if (checkstate(state)==aiturn):
            #print("!",state[0],"\n",state[1],"\n",state[2],"\n")
            return 10
        elif (checkstate(state)==3):
            #print(state[0],"\n",state[1],"\n",state[2],"\n")
            return 4
        else:
            #print(state[0],"\n",state[1],"\n",state[2],":(\n")
            return -10
        return -99999
    #print(state[0],"\n",state[1],"\n",state[2],"\n")
    blanks=[]
    for i in range(3):
        for j in range(3):
            if(state[i][j]==" "):
                blanks.append((i,j))
    mx=-99999
    mn=9999
    temp=" XO"
    opp=" OX"
    sym=""
    if(turn):
        sym=temp[aiturn]
    else:
        sym=opp[aiturn]
    for i in range(len(blanks)):
        cpy=[]
        for j in state:
            cpy.append(j[:])
        cpy[blanks[i][0]][blanks[i][1]]=sym
        k=minimax(cpy,depth+1,not turn,alpha,beta,aiturn)
        mx=max(mx,k)
        mn=min(mn,k)
        if turn:
            alpha=max(alpha,mx)
            if beta<=alpha:
                break
        else:
            beta=min(beta,mn)
            if beta<=alpha:
                break
    if(turn):
        return mx
    return mn
        
def game(t,inv):
    show()
    cnt=0
    while(check()==0):
        if cnt==t:
            AIturn(cnt+1)
        else:
            turn(cnt+1,inv)
        cnt+=1
        cnt%=2
        show()
    win=["Secret win message. Will never be accessed","Player 1 (X) wins","Player 2 (O) wins","It's a tie"]
    print(win[check()])

def startgame():
    init()
    print("Welcome to tic tac toe\nCo ordinates are from the top right (so the top left would be (2,0))\n")
    mode=int(input("Input 0 if you want the AI to go first, 1 if you want it to go second, 2 if you have enough friends to play together: ").strip())
    while not (mode in range(3)):
        mode=int(input("Not valid game mode. Try again: ").strip())
    inv=input("Input Y if you want the coordinates to be inverted. N otherwise: ").strip()
    while not (inv.lower() in ["y","n"]):
        inv=input("Not valid game input. Try again: ").strip()
    print()
    if(inv.lower()=="y"):
        game(mode,True)
        return
    game(mode,False)
    
if __name__=="__main__":
    startgame()
