import csv
import matplotlib.pyplot as plt
plt.style.use("ggplot")
from operator import itemgetter


def open_file():
    # WE ARE OPENING A FILE AND IF THE FILE IS BLANK RUN THE PROGRAM
    while True:      
        fn = input("Data file: ")
        if fn == "":
            return open("ncov.csv")
        try:
           f= open(fn ,"r")
           return f
        except FileNotFoundError:
            print("Error. Try again.")
            


def build_dictionary(fp):
    #This function iterates over the CSV reader and within each iteration, extracts the needed data and then creates
    #a dictionary that holds all of the data
    #LINE 29-34 are given in the pdf
    dictt = {}
    fp.readline()
    csvreader = csv.reader(fp, delimiter=',')
    for row in csvreader:
        country = row[2]
        area = row[1]
        last_update = row[3]
        cases = int(row[4])
        deaths = int(row[5])
        recovered = int(row[6])
        if area.strip() == "": 
            area = "N/A"
        if country not in dictt:
            dictt[country] = []
        dictt[country].append({area:(last_update, cases, deaths, recovered)})
    return dictt
    

def top_affected_by_spread(master_dict):
    #This function returns the top 10 countries most affected
    # IN DESCENDING ORDER
    listt=[]
    for k, v in master_dict.items():
        tup = (k, len(v))
        listt.append(tup)
    listt.sort()
    list_=sorted(listt, key = itemgetter(1), reverse = True)
    return list_[:10]
    
    


def top_affected_by_numbers(master_dict):
    #This function returns the top 10 countries most total people affected
    # IN DESCENDING ORDER, Key is the country value is the number.
    affected = []
    for key,val in master_dict.items():
        ppl = 0
        for dicts in val:
            for k,v in dicts.items():
                ppl += int(v[1])
        affected.append((key,ppl))
    affected.sort()
    top_affected_by_nums = sorted(affected, key = itemgetter(1), reverse = True)
    return(top_affected_by_nums[:10])


def is_affected(master_dict, country):
    #Returns true or false depending on whether the country is affected by nCoV
    return country.title() in master_dict 

def plot_by_numbers(list_of_countries, list_of_numbers):
    '''
        This function plots the number of areas/people inffected by country.
        
        parameters: 
            list_of_countries: list of countries
            list_of_numbers: list of the number of areas/people inffected
            
        Returns: None
    '''
    fig, ax = plt.subplots()
    
    x_pos = [i for i, _ in enumerate(list_of_countries)]
    
    ax.barh(x_pos, list_of_numbers, align='center', color='red')
    ax.set_yticks(x_pos)
    ax.set_yticklabels(list_of_countries)
    ax.invert_yaxis()
    ax.set_xlabel('Count')
    ax.set_title('Novel Coronavirus statistics')
    
    plt.show()


def affected_states_in_country(master_dict, country):
    #This function takes in the data dictionary and the name of a country (string)
    #and returns a set of affected areas within a country
    states= []
    for x in master_dict.keys():
        if country.upper() ==x.upper():
            for affected in master_dict[x]:
                states.append(list(affected.keys())[0])
    return set(states)
        

def main():
   
  
    BANNER = '''
.__   __.   ______   ______   ____    ____
|  \ |  |  /      | /  __  \  \   \  /   /
|   \|  | |  ,----'|  |  |  |  \   \/   / 
|  . `  | |  |     |  |  |  |   \      /  
|  |\   | |  `----.|  `--'  |    \    /   
|__| \__|  \______| \______/      \__/  
    '''
    print(BANNER)
    MENU = ''' 
[1] Countries with most areas infected
[2] Countries with most people affected
[3] Affected areas in a country
[4] Check if a country is affected
[5] Exit'''
    fp = open_file()
    mydict = build_dictionary(fp) 
    print(MENU)
    choice = input("Choice: ")
    while choice:
        if choice =='1':
            x = top_affected_by_spread(mydict)
            print("{:<20s}{:>5s}".format("Country", " Areas affected "))
            print("-"*40)
            for tup in x:
                print( "{:<20s} {:5d}".format(tup[0], tup[1]))
            a= input('Plot? (y/n) ')
            if a =="y":
                list_of_countries, list_of_numbers = [],[]
                for i in range(5):
                    list_of_countries.append(x[i][0])
                    list_of_numbers.append(x[i][1])
                plot_by_numbers(list_of_countries, list_of_numbers)
        elif choice == '2':
             y= top_affected_by_numbers(mydict)
             print("{:<20s}{:>5s}".format("Country", " People affected "))
             print("-"*40)
             for tup in y:
                 print( "{:<20s} {:5d}".format(tup[0], tup[1]))
             a= input('Plot? (y/n) ')

        elif choice == '3':
             country = input("Country name: ")
             z= affected_states_in_country(mydict, country)
             if country.title() in mydict or country.upper() == "US":
                  print("-"*30)
                  print("{:<30s}".format("Affected area"))
                  print("-"*30)
                  for i, areas in enumerate(sorted(z)):
                     print( "[{:02d}] {:<30s}".format(i+1, areas))
             else:
                 print("-"*30)
                 print("Error. Country not found. ")
                 
       
        elif choice == '4':
            country = input("Country name: ")
            g= is_affected(mydict, country)
            if g == True: 
                print("-"*30)
                print("{} is affected.".format(country))
            else :
                print("-"*30)
                print("{} is not affected.".format(country))
                
            
        elif choice == '5':
            print("Stay at home. Protect your community against COVID-19")
            break
        else:
            print("Error. Try again.")
        print(MENU)
        choice = input("\nChoice: ")
                 
            
            
            

    
if __name__ == "__main__":    
    main()