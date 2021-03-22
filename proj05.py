''' Insert heading comments here.'''

def open_file():
    while True:      
        fn = input("Input a file name: ")
        try:
           f= open(fn ,"r")
           return f
        except FileNotFoundError:
            print("Error: file not found. Please try again.")

            
def get_us_value(fp):
    fp.seek(0)
    fp.readline()
    fp.readline()
    for line in fp:
        state=line[:25].strip()
        try:              
            per =float(line[25:29]) 
        except ValueError:
            continue
        if state == "United States":
            return per
    
def get_min_value_and_state(fp):
    fp.seek(0)
    fp.readline()
    fp.readline()
    mini=101
    for line in fp:
        try:              
            per =float(line[25:29]) 
        except ValueError:
            continue
        state=line[:25].strip()
        if per< mini:
            mini=per
            mstate=state
    return (mstate, mini)
        


def get_max_value_and_state(fp):
    fp.seek(0)
    fp.readline()
    fp.readline()
    maxi=0
    for line in fp:
        try:              
            per =float(line[25:29]) 
        except ValueError:
            continue
        state=line[:25].strip()
        if per> maxi:
            maxi=per
            mstate=state
    return (mstate, maxi)
    
  
def display_herd_immunity(fp):
    
    fp.seek(0)
    fp.readline()
    fp.readline()
    s=90
    print("\nStates with insufficient Measles herd immunity.")
    print("{:<25s}{:>5s}".format("State","Percent"))
    for line in fp:
        try: 
           per =float(line[25:29]) 
        except ValueError:
            continue
        state=line[:25].strip()
        if per=="NA":
            continue
            per =float(line[25:29]) 
        if per<s:
            print("{:<25s}{:>5.1f}%".format(state, per))
        
             
         
    


def write_herd_immunity(fp):
    file =open("herd.txt", "w")
    fp.seek(0)
    fp.readline()
    fp.readline()
    s=90
    print("\nStates with insufficient Measles herd immunity.", file=file)
    print("{:<25s}{:>5s}".format("State","Percent"), file=file)
    for line in fp:
         try:              
            per =float(line[25:29]) 
         except ValueError:
            continue
         state=line[:25].strip()      
         if "NA" in line:
             continue
         if per<s:
             print("{:<25s}{:>5.1f}%".format(state, per), file=file)
    file.close()
             

def main():  
    fp= open_file()
    print()
    x= fp.readline()
    print(x)
    print()
    a= get_us_value(fp)
    b=get_min_value_and_state(fp)
    c= get_max_value_and_state(fp)
    print("Overall US MMR coverage: {}%".format(a))
    print("State with minimal MMR coverage: {} {}%".format(b[0], b[1]))
    print("State with maximum MMR coverage: {} {}%".format(c[0], c[1]))
    display_herd_immunity(fp)
    write_herd_immunity(fp)
   
  
   
  

              
  
            
   

if __name__ == "__main__":
    main()    

      

    