''' Insert heading comments here.'''

import csv

def open_file():
    '''Insert docstring here.'''
    while True:      
        fn = input("Enter filename: ")
        try:
           f= open(fn ,"r")
           return f
        except FileNotFoundError:
            print("File not found! Please try again!")
    

def read_file(fp):
    reader = csv.reader(fp)
    next(reader,None)
    mlist=[]
    
    for line_list in reader:
        mlist.append(line_list)
    return mlist
        
    
    
def shoots_left_right(master_list):
    left=0
    right=0
    for line in master_list:
        i = line[1]
        if i == "R":
            right+=1
        elif i == "L":
            left+=1
    return left,right
    


def position(master_list):
    r= 0 
    l=0
    c=0
    d=0
    for line in master_list:
        i = line[2]
        if i == "R":
            r+=1
        elif i == "L":
            l+=1
        elif i == "C":
            c+=1
        elif i == "D":
            d+=1
    return l, r, c, d
    
    

def off_side_shooter(master_list):
    lr= 0 
    rl=0
    for line in master_list:
        i = line[1]
        p = line[2]
        if i == "R" and p == "L":
            rl+=1
        elif i == "L" and p == "R":
            lr+=1
        else:
            continue
    return rl, lr

def points_per_game(master_list):
        lst= []
        for line in master_list:
            points = line[18]
            try:              
                points =float(line[18]) 
            except ValueError:
                continue
            player = line[0]
            pos = line[2]
            tup= (points, player, pos)
            lst.append(tup)
        lst.sort(reverse= True)
        return lst[0:10]
            

def games_played(master_list):
    lst= []
    for line in master_list:
        gp = line[3]
        if "," in line[3]:
            gp = line[3].replace(",","")
        g = int(gp)
        player=line[0]
        tup = (g, player)
        lst.append(tup)
    lst.sort(reverse= True)
    return lst[0:10]
           
       

def shots_taken(master_list):
    lst= []
    for line in master_list:
        s= line[9]
        player=line[0]
        if "-- " == line[9]:
            continue
        elif "," in line[9]:
            s = line[9].replace(",","")  
        else: 
            continue
        st = int(s)
        tup = (st, player)
        lst.append(tup)
    lst.sort(reverse= True)
    return lst[0:10]
        
    
def main():
    '''Insert docstring here.'''
    fp= open_file()
#    fp.readline() 
    master_list= read_file(fp)
    left,right =shoots_left_right(master_list)
    l, r, c, d= position(master_list)
    rl, lr= off_side_shooter(master_list)
    e= points_per_game(master_list)
    f= games_played(master_list)
    g= shots_taken(master_list)
    print()
    print("\n{:^10s}".format("Shooting"))
    print("left:  {:4d}".format(left))
    print("right: {:4d}".format(right))
    print()
    print("{:^12s}".format("Position"))
    print("left:    {:4d}".format(l))
    print("right:   {:4d}".format(r))
    print("center:  {:4d}".format(c))
    print("defense: {:4d}".format(d))
    print()
    print("{:^24s}".format("Off-side Shooter"))
    print("left-wing shooting right: {:4d}".format(rl))
    print("right-wing shooting left: {:4d}".format(lr))
    print()
    print("{:^36s}".format("Top Ten Points-Per-Game"))
    print("{:<20s}{:>8s}{:>16s}".format('Player','Position','Points Per Game'))  
    for line in e:   
        print("{:<20s}{:>8s}{:>16.2f}".format(line[1],line[2],line[0]))
    print("\n{:^36s}".format("Top Ten Games-Played"))
    print("{:<20s}{:>16s}".format('Player', 'Games Played'))
    for line in f:
        print("{:<20s}{:>16,d}".format(line[1], line[0]))
    print("\n{:^36s}".format("Top Ten Shots-Taken"))
    print("{:<20s}{:>16s}".format('Player', 'Shots Taken'))
    for line in g:
        print("{:<20s}{:>16,d}".format(line[1], line[0]))
        
        
 
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
     