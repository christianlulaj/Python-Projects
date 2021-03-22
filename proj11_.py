########################################################################
# CSE 231 Project 11
# Escapade game where user inputs directions to navigate a series of 
# classrooms, acquiring and discarding items in each room,
# with final goal of entering CSE231 classroom with specific inventory
# of items
########################################################################

#DO NOT DELETE THESE LINES
MAP = {"U":"Up","D":"Down","L":"Left","R":"Right"}

class Student(object):
    ''' Contains methods for student to check room ID and add or remove items 
    to/from inventory '''
    def __init__(self, item_list=None, classroom_id=-1):
        '''Initializes yourself, with an empty backpack by default. The default position of the student is room -1.'''

        if item_list == None:
            self.backpack = []
        else:
            self.backpack = item_list
        self.classroom_id = classroom_id

    def __repr__(self):
        '''Returns a string representation of the student.'''

        return self.__str__()

    def __str__(self):
        '''Returns a string representing the student's inventory.'''
        
        s = "Backpack: "
        if len(self.backpack) == 0:
            s += "Empty"
        else:
            for item in self.backpack:
                s += item + ", "
            else:
                s = s[:-2] # remove trailing comma and space
        return s

    def __eq__( self, S ):
        ''' Returns true if students classroom id and backpack are equal to 
        the classroom id and backpack of S, returns false otherwise '''
        
        if ((self.classroom_id == S.classroom_id) and (self.backpack == S.backpack)):
            return True
        else:
            return False
     
    def place(self, classroom_id):
        ''' Places student in classroom '''
        
        # set students classroom id equal to given classroom id
        self.classroom_id = classroom_id
    
    def add_item(self, item):
        ''' Adds item to students inventory, unless students inventory is 
        6 items '''
        
        # check if backpack has 6 items in list, adding item if less than 6
        if len(self.backpack) == 6:
            print("Backpack is full.")
        else:
            self.backpack.append(item)

    def remove_item(self, item):
        ''' Removes item from students inventory, unless the item specified
        does not exist in the backpack at that time '''
        
        if item not in self.backpack:
            print("Failed to remove item from backpack.")
        else:
            self.backpack.remove(item)

class Classroom(object):
    ''' Represents a single classroom at a time, associated with an int classroom id
    and a string course such as "CSE231" (with no spaces). It may have have one
    or more directions to other rooms and one or more items '''
    
    def __init__(self, text_desc="0 empty"):
        '''Initialzes a classroom. By default it has id 0 and is a "empty" room with no inventory or exits.'''
        description = text_desc.split()

        self.id = int(description[0])
        self.course = description[1]

        # Initialize a dictionary of potential exits as empty
        self.exits = {}

        # Initialize a "backpack" of items as empty list
        self.backpack = []
        
        #loop through description from word 2 onwards
        for word in description[2:]:
            # if first letter of word is lowercase, immediately append to backpack
            if word[0].islower():
                self.backpack.append(word)
            # otherwise, split 
            else:
                direct = word[0]
                ID = int(word[1:])
                self.exits[direct] = ID
        
    def __repr__(self):
        '''Returns a string representation of the classroom.'''
        classroom_repr = '''Classroom("''' + repr(self.id) + " " + self.course

        for direction in self.exits:
            classroom_repr += " {}".format(direction) + repr(self.exits[direction])

        for item in self.backpack:
            classroom_repr += " " + item

        classroom_repr += '''")'''

        return classroom_repr

    def __str__(self):
        '''Returns a string representing the room in a nice conversational style.'''

        # Basic classroom description
        classroom_str = "You see a " + self.course + " classroom."

        # List the things in the classroom
        if len(self.backpack) == 1:
            classroom_str += " On the desk you see a " + \
                             self.backpack[0] + "."
        if len(self.backpack) == 2:
            classroom_str += " On the desk you see a " + \
                             self.backpack[0] + \
                             " and a " + self.backpack[1] + "."
        elif len(self.backpack) > 2:
            classroom_str += " On the desk you see "
            for item in self.backpack[:-1]:
                classroom_str += "a " + item + ", "
            classroom_str += "and a " + self.backpack[-1] + "."

        # List the exits
        if len(self.exits) == 0:
            classroom_str += " Run through the classroom grab what you need (if possible). Exit and run to the exam!"
        elif len(self.exits) == 1:
            classroom_str += " Run through the classroom grab what you need (if possible). Now, run into the hallway and go " + \
                             MAP[list(self.exits.keys())[0]] + "."
        elif len(self.exits) == 2:
            classroom_str += " Run through the classroom grab what you need (if possible). Now, run into the hallway and go " + \
                             MAP[list(self.exits.keys())[0]] + " or " + MAP[list(self.exits.keys())[1]] + "."
        elif len(self.exits) > 2:
            classroom_str += " Run through the classroom grab what you need (if possible). Now, run into the hallway and go "
            for direction in list(self.exits.keys())[:-1]:
                classroom_str += MAP[direction] + ", "
            classroom_str += "or " + MAP[list(self.exits.keys())[-1]] + "."

        return classroom_str
    
    def __eq__( self, C ):
        ''' If classroom id, backpack, course, and exits are equivalent to C id,
        backpack, course, and exits, return True, and return False if not '''
        if ((self.id == C.id) and (self.backpack == C.backpack) and (self.course == C.course) and (self.exits == C.exits)):
            return True
        else:
            return False
        
    def add_item(self, item):
        ''' Adds item to classroom backpack '''
        self.backpack.append(item)

    def remove_item(self, item):
        ''' Removes item from classroom backpack, printing an error statement
        if that item does not exist in classroom backpack '''
        
        if item in self.backpack:
            self.backpack.remove(item)
            return True
        else:
            print("Failure to find the item in the classroom.")

    def get_room(self, direction):
        ''' If given direction is a key in exits dictionary, return the room
        ID that is being accessed '''
        
        if direction in self.exits:
            return self.exits[direction]
        else:
            return False
    
class Rush(object):
    ''' The class that governs the escapade, responsible for interactions between
    the user, the character, and the rooms '''

    def __init__(self, filename="rushing.txt"):
        '''Initializes the student rushing to class.  The student starts in the classroom with the lowest id.'''

        # First make a student start with an empty inventory
        self.student = Student()

        # Create classrooms are an empty dictionary
        self.classrooms = {}
        
        # Now read the file to get the classroom lines
        rf = open(filename)
        rf = rf.readlines()
        
        #iterate through each line and turn into a list
        for line in rf:
            line_list = line.split()
            key = int(line_list[0])
            self.classrooms[key] = Classroom(line)
            
        # Place the student in the room with lowest id
        self.student.place(min(self.classrooms.keys()))
        

    def __repr__(self):
        '''Returns a string representation.'''

        return self.__str__()

    def __str__(self):
        '''Returns a string representing the journey to the class, simply giving the number of rooms.'''
        search_str = "You are searched in "
        if len(self.classrooms) == 0:
            search_str += "no classrooms at all, you are in the hallway. You are late run in a random class and get items from the desks."
        elif len(self.classrooms) == 1:
            search_str += "a classroom."
        else:
            search_str += "a set of " + str(len(self.classrooms)) + \
                          " classrooms."

        return search_str

    def intro(self):
        '''Prints an introduction to the search for items because you are late
        This prompt includes the commands.'''
        print("\nAHHHH! I'm late for class\n")
        print("*runs out the house to catch the bus with an empty backpack*")

        print("\nYou're popular and have friends in many classes. Find and collect any items you find useful for your exam.")
        print("You are already late, and have a CSE231 Final Exam in 10 mins.\n")
        self.print_help()


    def print_help(self):
        '''Prints the valid commands.'''
        print("Use your instincts: ")
        print("*thinks*.. *thinks*.. what to do?!?!?!?!")
        print("*running*")
        print("S or search -- prints a description of the classroom you ran into")
        print("B or backpack - prints a list of items in your backpack")
        print("P pencil or pickup pencil - *mental* instruction to pick up an item called pencil")
        print("DR pencil or drop pencil - *mental* instruction to drop off an item called pencil")
        print("U or up - *mental* instruction to up the hallway to find another classroom")
        print("D or down - *mental* instruction to down the hallway to find another classroom")
        print("R or right - *mental* instruction to right in the hallway to find another classroom")
        print("L or left - *mental* instruction to left in the hallway to find another classroom")
        print("G or giveup - I have no more time, I need to get to class!!!")
        print("H or help - prints this list of options again")
        print()
        print("Remember that uppercase and lowercase SHOULD NOT matter. ")
        print("JUST GRAB WHAT YOU NEED AND GET TO CLASS TO START YOUR FINAL EXAM!!! HURRYYYY!!!")
        print()

    def prompt(self):
        '''Prompts for input and handles it, whether by error message or handling a valid command.
        Returns True as long as the user has not chosen to quit, False if they have.'''

        print("In room {} with course {}".format(self.student.classroom_id,self.classrooms[self.student.classroom_id].course))
        print(self.student)
        user_input = input("Enter a command (H for help): ")
        print()

        # Handle input: split for pickup/drop, capitalization unimportant for commands
        input_list = user_input.split()

        if len(input_list) == 0:
            user_input = "?"  # No command is not a valid command
            return False
        else:
            try:
                command = input_list[0].upper()  # The command
                if len(input_list) > 1:
                    item = input_list[1]
                if command == 'S':
                    self.search()
                elif command == 'B':
                    self.backpack()
                elif command == 'P':
                    self.pickup(item)
                elif command == 'DR':
                    self.drop(item)
                elif command in "UDLR":
                    self.move(command)
                elif command == 'G':
                    print("I have no more time, I need to get to class!!!")
                    return False
                elif command == 'H':
                     self.print_help() 
                else:
                    print("Unfortunately, that's not a valid option.")
                    return False
            except:
                print("Problem with the option or the item.")
                return False
        if self.win():
            return "win"
        return True

    def search(self):
        '''Prints the description of the current room.'''
        current_classroom = self.classrooms[self.student.classroom_id]
        print(current_classroom)

    def backpack(self):
        ''' Prints the student's current backpack '''
        student_backpack = self.student.backpack
        print(student_backpack)

    def pickup(self, item):
        ''' Checks if item is inside of current classroom, and adds to student's
        backpack if it is not full. Deletes item from classroom and does not add
        to student's backpack if full. '''
        current_classroom = self.classrooms[self.student.classroom_id]
        student_backpack = self.student.backpack
        
        if current_classroom.remove_item(item) == True:
            if len(student_backpack) < 6:
                student_backpack.append(item)
            else:
                print("Backpack is full.")
        
    def drop(self, item):
        ''' Removes an item from students backpack and adds to the classroom 
        backpack, printing an error if the item does not exist in the student
        backpack '''
        current_classroom = self.classrooms[self.student.classroom_id]
        student_backpack = self.student.backpack
        
        if item in student_backpack:
            current_classroom.add_item(item)
            student_backpack.remove(item)
        else:
            print("Failed to remove item from backpack.")
            

    def move(self, direction):
        ''' Moves the student in the specified direction if that direction and
        classroom exists, printing an error message if the move is invalid '''
        errMsg = "Unfortunately, you went " + MAP[direction] + " and there was no classroom."
        current_classroom = self.classrooms[self.student.classroom_id]
        
        if current_classroom.get_room(direction):
            self.student.place(current_classroom.get_room(direction))
            print("You went " + MAP[direction] + " and found a new classroom.")
        else:
            print(errMsg)

    def win(self):
        ''' Check that user has entered the classroom with course CSE231 and has
        the required backpack for success, returning True if both are true '''
        current_classroom = self.classrooms[self.student.classroom_id]
        course = current_classroom.course
        student_backpack = sorted(self.student.backpack)
        winning_backpack = ['cheatsheet', 'eraser', 'paper', 'pencil']
        
        if course == "CSE231" and student_backpack == winning_backpack:
            return True
        else:
            return False
            
def main():
    '''
    Prompts the user for a file, then plays that file until the user chooses to give up.
    Does not check formatting of input file.
    '''

    while True:
        try:
            filename = input("Enter a text filename: ")
            escapade = Rush(filename)
            break
        except IOError:
            print("Cannot open file:{}. Please try again.".format(filename))
            continue
    
    escapade.intro()
    escapade.__str__()
    escapade.search()
    
    keep_going = True
    while keep_going:
        keep_going = escapade.prompt()
        if keep_going == 'win':
            break
    if keep_going == 'win':
        print("You succeeded!")
    else:
        print("Thank you for playing")

if __name__ == "__main__":    
    main()