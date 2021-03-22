''' Insert heading comments here.'''

import math
EPSILON = 1.0e-7

def display_options():
    ''' This function displays the menu of options'''

    MENU = '''\nPlease choose one of the options below:
             A. Display the sum of squares of the first N natural numbers.
             B. Display the approximate value of Pi.
             C. Display the approximate value of the sine of X.
             D. Display the approximate value of the cosine of X.
             M. Display the menu of options.
             X. Exit from the program.'''
    print(MENU)
    
def sum_natural_squares(N):
    sm = 0
    if N.isdigit()and int(N)>0:
        for i in range(int(N)+1): 
            sm = sm + (i * i) 
        return sm 
    else:
        return None
        
            
   
    

def approximate_pi():
    sm=0
    n=0
    term=((-1)**n)/(2*n+1)
    while abs(term)>EPSILON:
        sm+=term
        n+=1
        term=((-1)**n)/(2*n+1)
          
    return round(4*sm,10)
       
    
    
def approximate_sin(x):
    try:
        x=float(x)
        sm=0
        n=0 
        term=((-1)**n)*(x**(2*n+1))/math.factorial(2*n+1)
        while abs(term)>EPSILON:
            sm+=term
            n+=1
            term=((-1)**n)*(x**(2*n+1))/math.factorial(2*n+1)            
        return round(sm,10)
    except ValueError:
        return None
    
    
    
           
def approximate_cos(x):
    try:
        x=float(x)
        sm=0
        n=0
        term=((-1)**n)*(x**(2*n))/math.factorial(2*n)
        while abs(term)>EPSILON:
            n+=1
            sm+=term
            term=((-1)**n)*(x**(2*n))/math.factorial(2*n)
        return round(sm,10)
    except ValueError:
        return None
    

def main():
   choice = ''
   display_options()
  
   while choice.upper() != 'X':
       choice = input("\n\tEnter option: ")
      
       if choice.upper() == 'A':
           
           
               N=input("\nEnter N: ")
               result = sum_natural_squares(N)
               if result != None:                   
                   print("\n\tThe sum: {}".format(result))  
               else:
                   print("\n\tError: N was not a valid natural number. [{}]".format(N))
       elif choice.upper() == 'B':
           result = approximate_pi()
           print("\n\tApproximation: {:.10f}".format(result))
           actual = math.pi
           diff = abs(actual - result)
           print("\tMath module:   {:.10f}".format(actual))
           print("\tdifference:    {:.10f}".format(diff))
          
       elif choice.upper() == 'C':
          
           x = input("\n\tEnter X: ")
           result = approximate_sin(x)
          
           if result != None:
               print("\n\tApproximation: {:.10f}".format(result))
               actual = math.sin(float(x))
               diff = abs(actual - result)
               print("\tMath module:   {:.10f}".format(actual))
               print("\tdifference:    {:.10f}".format(diff))
           else:
               print("\n\tError: X was not a valid float. [{}]".format(x))
              
       elif choice.upper() == 'D':
           x = input("\n\tEnter X: ")
           result = approximate_cos(x)
          
           if result != None:
               print("\n\tApproximation: {:.10f}".format(result))
               actual = math.cos(float(x))
               diff = abs(actual - result)
               print("\tMath module:   {:.10f}".format(actual))
               print("\tdifference:    {:.10f}".format(diff))
           else:
               print("\n\tError: X was not a valid float. [{}]".format(x))
              
       elif choice.upper() == 'M':
           display_options()
       elif choice.upper() == 'X':
           print('Hope to see you again.')
           break
       else:
           print("\nError:  unrecognized option [{}]".format(choice.upper()))
           display_options()
          
if __name__ == "__main__": 
    main()        






