''' Your header goes here '''

#DO NOT DELETE THESE LINES
import cards, random
random.seed(100) #random number generator will always generate 
                 #the same random number (needed to replicate tests)


def initialize():
    '''
        WRITE DOCSTRING HERE!
    '''
    my_deck= cards.Deck()
    my_deck.shuffle()
    table= [[],[],[],[]]
    for row in table:
        for i in range(13):
            row.append(my_deck.deal())           
    return table
    
    
   
    
def display(tableau):
    '''
        This function displays the current state of the game.
        It display four rows of 13 cards with row and column labels.
        Ace is displayed with a blank.
        
        parameters: 
            tableau: data structure representing the tableau 
        
        Returns: None
    '''

    print("{:3s} ".format(' '), end = '')
    for col in range(1,14):
        print("{:3d} ".format(col), end = '')
    print()
        
    for r,row_list in enumerate(tableau):
        print("{:3d}:".format(r+1), end = '')
        for c in row_list:
            if c.rank() == 1:
                print("  {}{}".format(' ',' '), end = '')
            else:
                print("{:>4s}".format(str(c)),end = '')
        print()

def validate_move(tableau,source_row,source_col,dest_row,dest_col):
    one = tableau[dest_row][dest_col].rank()==1
    two = dest_col ==0 and tableau[source_row][source_col].rank()==2
    left = tableau[dest_row][dest_col - 1]
    s_card = tableau[source_row][source_col]
    three = dest_col > 0 and (s_card.rank() - left.rank()) ==1 and s_card.suit()== left.suit()
    return one and (two or three)

#THE THREE RULES ARE:
#1if the destination is empty (contains an ace)
#2 if the empty destination is the leftmost column and the source card has rank 2
#3if the empty destination is not the leftmost column and the card to the left is the same suit
#as the source card and has a rank that is one less than the source card’s rank.
    
            
    

def move(tableau,source_row,source_col,dest_row,dest_col):
    #Literally exactly like the validate move except you add If the move is valid,
    #the function will update the tableau and return True; otherwise, it will do nothing to it and return False
    if validate_move(tableau,source_row,source_col,dest_row,dest_col):
        s_card = tableau[source_row][source_col]
        d_card = tableau[dest_row][dest_col]
        tableau[source_row][source_col] = d_card
        tableau[dest_row][dest_col]= s_card
        return True
    else:   
        return False
          
        
    
  
def shuffle_tableau(tableau): 
    shuff = []
    Acelistt= []
    for j, row in enumerate(tableau): 
        i = 0
        while i< len(row):
            card= row[i]
            if i>0:
                prev=row[i-1]
            if (i== 0 and card.rank()==2) or (i>0 and card.rank()-1 == prev.rank() and prev.suit() == card.suit()):
                i+=1
                continue
            else:
                shuff.extend(row[i:])
                tableau[j]= row[:i]
                break    
   
    random.shuffle(shuff)
    for card in shuff:
        if card.rank() == 1:
            Acelistt.append(card)       
    for ace in Acelistt:
        shuff.remove(ace)
        
      
    for row_idx, row in enumerate(tableau):
        ace = Acelistt[0]
        row.append(ace)
        Acelistt.remove(ace)
        while len(row) < 13:
            next_card = shuff[0]
            row.append(next_card)
            shuff.remove(next_card)
            
# you iterate through the tableau
 #for each row:
#you first add an ace from the Acelist and then remove it from the Acelist.
#you add from the shuff list the amount of cards needed to fill the row 
#(Hint: find how many cards do you need for the row knowing that the maximum should be 13). Do not forget to remove those cards from the shuff list
        
        
        
 # you iterate through the tableau
#for each row
#you first add an ace from the Acelist and then remove it from the Acelist.
#you add from the shuff list the amount of cards needed to fill the row 
#(Hint: find how many cards do you need for the row knowing that the maximum should be 13).
# Do not forget to remove those cards from the shuff list
        
                
                    

def check_win(tableau):
    answer = True
    for x in tableau:
        r1 = x[0].rank()==2
        r2= True
        r3= True
        r4=x[12].rank()==1
        for i, card in enumerate(x):
            if i == 0 or i ==12:
                continue
            else:
                left = x[i-1]
                r2 &= (card.rank()- left.rank())==1
                r3 &= card.suit()==left.suit()
        answer &= r1 and r2 and r3 and r4
    return answer
             
def main():
#a) Your program should start by initializing the tableau.
#b) Display the tableau.
#c) Ask to input an option and check the validity of the input.
#d) If ‘Q’, quit the game
#e) If ‘S’, shuffle the tableau and display the tableau
#f) If ‘Sr Sc Dr Dc’, move card from Tableau (Sr, Sc) to empty Tableau (Dr, Dc). g) If none of these options, the program should display an error message.
#h) The program should repeat until the user won or quit the game.
#i) Then ask if the user wants another game
#j) Display a goodbye message.
    
    while True:
        print("Montana Solitaire.")
        tableau = initialize()
        display(tableau)
        shuff=0
        choice = input("Enter choice:\n (q)uit, (s)huffle, or space-separated: source_row,source_col,dest_row,dest_col: ")
        while choice.lower()!= "q":
            line = choice.split()
            if len(line)== 4:
                try:
                    i0= int(line[0])-1
                    i1= int(line[1])-1
                    i2= int(line[2])-1
                    i3= int(line[3])-1
                    if not (0<= i0<=3 and 0<=i1<=12 and 0<=i2<=3 and 0<=i3<=12):
                        print("Error: row and/or column out of range. Please Try again.")
                        choice = input("Enter choice:\n (q)uit, (s)huffle, or space-separated: source_row,source_col,dest_row,dest_col: ")
                        continue

                except ValueError:
                    print("Error: invalid input.  Please try again.")
                    choice = input("Enter choice:\n (q)uit, (s)huffle, or space-separated: source_row,source_col,dest_row,dest_col: ")
                    continue
                value= move(tableau, i0, i1, i2, i3)
                if value==True:
                    display(tableau)
                    check = check_win(tableau)
                    if check== True:
                        print("You won!")
                        choice = 'q'
                        continue
                else:
                    print("Error: invalid move.  Please try again.")
                
            elif choice.lower()== "s":
    
                if shuff<=1:
                    shuffle_tableau(tableau)
                    display(tableau)
                else:
                    print("No more shuffles remain.")
                shuff+=1
            else:
                print("Error: invalid input.  Please try again.")
            choice = input("Enter choice:\n (q)uit, (s)huffle, or space-separated: source_row,source_col,dest_row,dest_col: ")
        if choice.lower()== "q":
            answer= input("Do you want to play again (y/n)?")
            shuff=0
            if answer.lower()== "n":
                print("Thank you for playing.")
                break
                        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
if __name__ == "__main__":
    main()  
