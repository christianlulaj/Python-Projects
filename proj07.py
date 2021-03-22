''' Your header goes here '''
import csv
import math
from operator import itemgetter

def open_file():
    ''' Docstring goes here '''
    while True:      
        fn = input("Enter filename: ")
        try:
           f= open(fn ,"r")
           return f
        except FileNotFoundError:
            print("File not found! Please try again!")

def calc_multipliers():
    ''' Docstring goes here '''
    cm=[]
    for i in range(2,61):
        r= (1/(math.sqrt(i*(i-1))))
        cm.append(r)
    return cm
    
def calc_priorities(s,p,m):
    ''' Docstring goes here '''
    cp= []
    for x in m:
        calculation= x*p
        cp.append((int(calculation), s))
    cp.sort(key=itemgetter(1), reverse= True)
    return cp

def read_file_make_priorities(fp,multipliers): 
    ''' Docstring goes here '''
    reader= csv.reader(fp)
    next(reader, None)
    counter=[]
    prior=[]
    for line in reader:
        state = line[1].replace('"','').strip()
        if state == 'District of Columbia' or state == 'Puerto Rico':
            continue
        population= int(line[2])
        counter.append([state,1])
        priorities = calc_priorities(state, population, multipliers)
        prior+= priorities
    counter.sort(key=itemgetter(0), reverse = False)
    prior.sort(key=itemgetter(0), reverse = True)
    return counter, prior[:385]

def add_to_state(state,states):
    ''' Docstring goes here '''
    for line  in states:
        if line[0]== state:
            line[1] += 1
        

def display(states):
    print("{:<15s}{:>4s}".format('State','Representatives'))
    for i in states:
        print("{:<15s}{:>4d}".format(i[0],i[1]))

        
def main():
    fp=open_file()
    multipliers=calc_multipliers()
    read_file= read_file_make_priorities(fp,multipliers)
    prior= read_file[1]
    state= read_file[0]
    
    for line in prior:
        add_to_state(line[1], state)
    display(state)
    
    

if __name__ == "__main__":
    main()