import csv
import pylab
from operator import itemgetter
from collections import OrderedDict

def open_file():
    ''' Docstring goes here '''
    while True:      
        fn = input("Enter filename: ")
        try:
           f= open(fn ,encoding = 'utf-8')
           return f
        except FileNotFoundError:
            print("File not found! Please try again!")

def read_file(fp):
    reader = csv.reader(fp)
    next(reader, None)
    D1L, D2L, D3L= [], [], []
    D1, D2, D3 = dict(), dict(), dict()
    FinalD, FinalD2, FinalD3 = OrderedDict(),  OrderedDict(),  OrderedDict()
    for line in reader:
        if line[2] == 'N/A':
            continue
        name = line[0].strip().lower()
        platform = line[1].strip().lower()
        year = int(line[2])
        genre = line[3].strip().lower()
        publisher = line[4].strip().lower()
        na_sales = float(line[5]) * 1000000
        eur_sales = float(line[6]) * 1000000
        jpn_sales = float(line[7]) * 1000000
        other_sales = float(line[8]) * 1000000
        global_sales = na_sales +  eur_sales + jpn_sales + other_sales
        if name not in D1:
            D1[name] = []
        D1[name].append((name, platform, year, genre, publisher, global_sales))
        if genre not in D2:
            D2[genre] = []
        D2[genre].append((genre, year, na_sales, eur_sales, jpn_sales, other_sales, global_sales))
        if publisher not in D3:
            D3[publisher] = []
        D3[publisher].append((publisher, name, year, na_sales, eur_sales, jpn_sales, other_sales, global_sales))       
        for k,v in D1.items():
            D1L.append((k,v))           
        for k,v in D2.items():
            D2L.append((k,v))           
        for k,v in D3.items():
            D3L.append((k,v))
            
        def sort1(e):
            return e[0]
        def sort2(e):
            return e[-1]    
        D1L.sort(key = sort1)
        D2L.sort(key = sort1)
        D3L.sort(key = sort1)
        for x in sorted(D1L):
            x[1].sort(key=sort2, reverse = True)
            FinalD[x[0]]= x[1]
        for x in sorted(D2L):
            x[1].sort(key=sort2, reverse = True)
            FinalD2[x[0]]= x[1]
        for x in sorted(D3L):
            x[1].sort(key=sort2, reverse = True)
            FinalD3[x[0]]= x[1]
    return FinalD, FinalD2, FinalD3
            


    
def get_data_by_column(D1, indicator, c_value):
    year = []
    p_listt = []
    
    if indicator == "platform":
        for value in D1.values():
            for index in value:
                if index[1]== c_value:
                    p_listt.append(index)
        p_listt.sort(key = itemgetter(5), reverse = True)
        p_listt.sort(key = itemgetter(2), reverse = False)
        return p_listt
    
    elif indicator == "year":
        for value in D1.values():
            for index in value:
                if index[2]== c_value:
                    year.append(index)
        year.sort(key = itemgetter(5), reverse = True)
        year.sort(key= itemgetter(1), reverse = False)
        
        return year
    
        

   


def get_publisher_data(D3, publisher):
    p_lst = []
    for k in D3.values():
        for c in k:
            if c[0] == publisher:
                p_lst.append(c)
    p_lst.sort(key = itemgetter(1), reverse = False)
    p_lst.sort(key = itemgetter(7), reverse = True)
    return p_lst


def display_global_sales_data(L, indicator):
    '''
        WRITE DOCSTRING HERE!
    '''
    
    header1 = ['Name', 'Platform', 'Genre', 'Publisher', 'Global Sales']
    header2 = ['Name', 'Year', 'Genre', 'Publisher', 'Global Sales']
    
#    L = [('pokemon gold/pokemon silver', 'gb', 1999, 'role-playing', 'nintendo', 23090000.0), ('pokemon pinball', 'gb', 1999, 'misc', 'nintendo', 5310000.0), ('super mario bros.', 'gb', 1999, 'platform', 'nintendo', 5070000.0), ('super smash bros.', 'n64', 1999, 'fighting', 'nintendo', 5560000.0), ('pokemon stadium', 'n64', 1999, 'strategy', 'nintendo', 5450000.0), ('donkey kong 64', 'n64', 1999, 'platform', 'nintendo', 5270000.0), ('pokemon snap', 'n64', 1999, 'simulation', 'nintendo', 3630000.0)]




    

def get_genre_data(D2, year):
 
  genre_list=[]
  for genre, val in D2.items():
      count =0
      tot_na_sls=0
      tot_eur_sls=0
      tot_jpn_sls=0
      tot_other_sls=0
      tot_global_sls=0
      for c in val:
          if c[1] == year:
              count+=1
              tot_na_sls+= int(c[2])
              tot_eur_sls+= int(c[3])
              tot_jpn_sls+= int(c[4])
              tot_other_sls+= int(c[5])
              tot_global_sls+= int(c[6])
              the_tup =(genre, count, tot_na_sls, tot_eur_sls, tot_jpn_sls, tot_other_sls,  tot_global_sls)
      if count != 0:
          genre_list.append(the_tup)
    
  genre_list.sort(key = itemgetter(0), reverse = False)
  genre_list.sort(key = itemgetter(6), reverse = True)
  return(genre_list)
      
      
      
      
      
      
#def display_genre_data(genre_list):
#    '''
#        WRITE DOCSTRING HERE!
#    '''
#    print("{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}".format('Genre', 'North America', 'Europe', 'Japan', 'Other', 'Global'))
#    for i in genre_list:
#        genre = i[0]
#        na = i[2]    
#        eu = i[3] 
#        jpn = i[4] 
#        other = i[5] 
#        glob = i[6] 
#        total_glob = 0
#        print("{:15s}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}".format(genre, na, eu, jpn, other, glob, total_glob))
#    print("\n{:75s}{:<15,.02f}".format("Total Global Sales", total_glob))
#    pass

#def display_publisher_data(pub_list):
#    '''
#        WRITE DOCSTRING HERE!
#    '''
#    print("{:30s}{:15s}{:15s}{:15s}{:15s}{:15s}".format('Title', 'North America', 'Europe', 'Japan', 'Other', 'Global'))
#    for i in pub_list:
#        name = i[1][:25]
#        na = float(i[3])
#        eu = float(i[4])
#        jpn = float(i[5])
#        other = float(i[6])
#        glob = float(i[7])
#        print("{:30s}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}".format(name, na, eu, jpn, other, glob))
#    pass
    
 

def get_totals(L, indicator):
    L1 = []
    L2= []
    results = dict()
    for item in L:
        platform = item[1]
        year = item[2]
        gbSales = item[5]
        if indicator == "year":
            if platform not in results:
                results[platform] =0
            results[platform] += gbSales
        elif indicator == "platform":
            if year not in results:
                results[year] =0
            results[year] += gbSales
    for key, val in results.items():
        L1.append(key)
        L2.append(val)
        L1= sorted(L1)
        L2= L2
    return(L1, L2)
        

def prepare_pie(genres_list):
    
    Ltups=[]
    Lstring=[]
    Lnums=[]
    for item in genres_list:
        strings = item[0]
        gbsales = item[6]
        Ltups.append((strings, gbsales))
    Ltups.sort(key = itemgetter(1), reverse = True)
    for item in Ltups:
        Lstring.append(item[0])
        Lnums.append(item[1])
    return Lstring, Lnums

def plot_global_sales(x,y,indicator, value):
    '''
        This function plots the global sales per year or platform.
        
        parameters: 
            x: list of publishers or year sorted in ascending order
            y: list of global sales that corresponds to x
            indicator: "publisher" or "year"
            value: the publisher name (str) or year (int)
        
        Returns: None
    '''
    
    if indicator == 'year':    
        pylab.title("Video Game Global Sales in {}".format(value))
        pylab.xlabel("Platform")
    elif indicator == 'platform':    
        pylab.title("Video Game Global Sales for {}".format(value))
        pylab.xlabel("Year")
    
    pylab.ylabel("Total copies sold (millions)")
    
    pylab.bar(x, y)
    pylab.show()

def plot_genre_pie(genre, values, year):
    '''
        This function plots the global sales per genre in a year.
        
        parameters: 
            genre: list of genres that corresponds to y order
            values: list of global sales sorted in descending order 
            year: the year of the genre data (int)
        
        Returns: None
    '''
            
    pylab.pie(values, labels=genre,autopct='%1.1f%%')
    pylab.title("Video Games Sales per Genre in {}".format(year))
    pylab.show()
    
def main():
    fp = open_file()
    read = read_file(fp)
    print(read)
    D1, indicator, c_value = read_file(fp)
    year = get_data_by_column(D1, indicator, c_value)
    print(year)
    
    
   
    
    
##    Menu options for the program
#    MENU = '''Menu options
#    
#    1) View data by year
#    2) View data by platform
#    3) View yearly regional sales by genre
#    4) View sales by publisher
#    5) Quit
#    
#    Enter choice: '''
#                   
#    while choice != '5':
#        
#        #Option 1: Display all platforms for a single year
#            
#            try:
#                
#                #if the list of platforms for a single year is empty, show an error message    
#                pass
#            
#            except ValueError:
#                print("Invalid year.")
#                
#        
#                
#        #Option 4: Display publisher data
#            
#                # Enter keyword for the publisher name
#                
#                # search all publisher with the keyword
#                match = []
#                
#                # print the number of matches found with the keywords
#                if len(match) > 1:    
#                    print("There are {} publisher(s) with the requested keyword!".format(len(match)))
#                    for i,t in enumerate(match):
#                        print("{:<4d}{}".format(i,t[0]))
#                    
#                    # PROMPT USER FOR INDEX
#                    
#                else:
#                    index = 0
#                
#        choice = input(MENU)
#    
#    print("\nThanks for using the program!")
#    print("I'll leave you with this: \"All your base are belong to us!\"")

if __name__ == "__main__":
    main()
