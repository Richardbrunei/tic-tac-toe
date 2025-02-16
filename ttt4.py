from random import randint

def contains(aa,bb):
    for i in range(len(aa)-len(bb)+1):
        if aa[i:i+len(bb)]==bb:
            return True
    return False

def check():
    for i in a:
        if contains(i,["X","X","X","X"]):
            return 1
        if contains(i,["O","O","O","O"]):
            return 2
    for i in range(10):
        b=[]
        for j in range(10):
            b.append(a[j][i])
        if contains(b,["X","X","X","X"]):
            return 1
        if contains(b,["O","O","O","O"]):
            return 2
    c=[[] for i in range(19)]
    d=[[] for i in range(19)]
    e=[[None,None,None,None,None,None,None,None,None,None] for i in range(19)]
    cnt=0
    for i in range(10):
        for j in range(10):
            #print(i,j)
            if(i>0 and j>0):
                c[e[i-1][j-1]].append(a[i][j])
                e[i][j]=e[i-1][j-1]
            else:
                c[cnt].append(a[i][j])
                e[i][j]=cnt
                cnt+=1
    cnt=0
    e=[[None,None,None,None,None,None,None,None,None,None] for i in range(19)]
    for i in range(10):
        for j in range(10):
            if(i>0 and j<9):
                d[e[i-1][j+1]].append(a[i][j])
                e[i][j]=e[i-1][j+1]
            else:
                d[cnt].append(a[i][j])
                e[i][j]=cnt
                cnt+=1
    #for i in range(3):
    #    c.append(a[i][i])
    #    d.append(a[i][2-i])
    #print(c)
    #print(d)
    #print("C:")
    #for i in c:
    #    print(i)
    #print("D:")
    #for i in d:
    #    print(i)
    for i in range(19):
        if contains(c[i],["X","X","X","X"]):
            return 1
        if contains(c[i],["O","O","O","O"]):
            return 2
        if contains(d[i],["X","X","X","X"]):
            return 1
        if contains(d[i],["O","O","O","O"]):
            return 2
    for i in a:
        for j in i:
            if j==' ':
                return 0
    return 3

def show():
    k="\n  "
    for i in range(9):
        k+=str(i)+' '
    k+="9\n\n"
    for i in range(10):
        k+=str(i)+" "
        for j in range(9):
            k+=str(a[i][j])+"|"
        k+=str(a[i][9])+"\n"
        if i!=9:
            k+="  -------------------\n"
    k+="\n"
    print(k)
    
def turn(player,inv):
    k=input("Player "+str(player)+", its your turn: ").strip()
    if(len(k)==3):
        x,y=k.split(" ")
        x=int(x)
        y=int(y)
    else:
        x=99999;
        y=99999;
    temp=" XO"
    while(True):
        if ((x>=0 and x<10) and (y>=0 and y<10)):
            if(inv):
                if a[x][y]==" ":
                    break
            else:    
                if a[y][x]==" ":
                    break
        k=input("Nope, you cant go there. It's still your turn: ").strip()
        if(len(k)==3):
            x,y=k.split(" ")
            x=int(x)
            y=int(y)
        else:
            x=99999;
            y=99999;
    if inv:
        a[x][y]=temp[player]
    else:   
        a[y][x]=temp[player]
    
def init():
    global a
    inverted=False
    a=[[" "," "," "," "," "," "," "," "," "," "] for i in range(10)]

def checkdanger(opp):
    danger=0
    darr=[" ",opp,opp,opp," "]
    #print(darr)
    for i in a:
        if contains(i,darr):
            danger+=1
    for i in range(10):
        b=[]
        for j in range(10):
            b.append(a[j][i])
        if contains(b,darr):
            danger+=1
    c=[[] for i in range(19)]
    d=[[] for i in range(19)]
    e=[[None,None,None,None,None,None,None,None,None,None] for i in range(10)]
    cnt=0
    for i in range(10):
        for j in range(10):
            #print(i,j)
            if(i>0 and j>0):
                c[e[i-1][j-1]].append(a[i][j])
                e[i][j]=e[i-1][j-1]
            else:
                c[cnt].append(a[i][j])
                e[i][j]=cnt
                cnt+=1
    cnt=0
    e=[[None,None,None,None,None,None,None,None,None,None] for i in range(10)]
    for i in range(10):
        for j in range(10):
            if(i>0 and j<9):
                d[e[i-1][j+1]].append(a[i][j])
                e[i][j]=e[i-1][j+1]
            else:
                d[cnt].append(a[i][j])
                e[i][j]=cnt
                cnt+=1
    for i in range(19):
        if contains(c[i],darr):
            danger+=1
        if contains(d[i],darr):
            danger+=1
    return danger
        
def AIturn(player):
    mx=[0,0,-1,1,-1,1,-1,1];
    my=[1,-1,0,0,-1,1,1,-1];
    blanks=[]
    opposite=[0,2,1]
    temp=" XO"
    mindistmid=99999999
    middidx=0
    for i in range(10):
        for j in range(10):
            if(a[i][j]==" "):
                if((abs(i-5)+abs(j-5))<mindistmid):
                    mididx=len(blanks)
                    mindistmid=(abs(i-5)+abs(j-5))
                blanks.append((i,j))
    choos=0
    flag=True
    possible=[]
    for i in range(len(blanks)):
        for x in mx:
                for y in my:
                    if(blanks[i][0]+x in range(10)):
                        if(blanks[i][1]+y in range(10)):
                            if(a[blanks[i][0]+x][blanks[i][1]+y]==temp[opposite[player]]):
                                 flag=False
                                 possible.append(i)
    if(flag):
        possible.append(0)
    oldchoos=possible[randint(0,len(possible)-1)]
    maxdanger=0
    cnt=0
    for i in range(len(blanks)):
        a[blanks[i][0]][blanks[i][1]]=temp[opposite[player]]
        if(checkdanger(temp[opposite[player]])>=maxdanger):
            #print(i,mindanger,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            choos=i
            cnt+=1
            maxdanger=checkdanger(temp[opposite[player]])
        a[blanks[i][0]][blanks[i][1]]=" "
    if (cnt==len(blanks) and (flag)):
        choos=mididx
    elif(cnt==len(blanks)):
        choos=oldchoos
    for i in range(len(blanks)):
        a[blanks[i][0]][blanks[i][1]]=temp[opposite[player]]
        if check()==opposite[player]:
            choos=i
        a[blanks[i][0]][blanks[i][1]]=" "
    for i in range(len(blanks)):
        a[blanks[i][0]][blanks[i][1]]=temp[player]
        if check()==player:
            choos=i
        a[blanks[i][0]][blanks[i][1]]=" "
    a[blanks[choos][0]][blanks[choos][1]]=temp[player]
    print("The (slightly more intelligent) AI has made a move :)")
    
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
    print("Welcome to tic tac toe\nCo ordinates are from the top right (so the top left would be (9,0))\n")
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
