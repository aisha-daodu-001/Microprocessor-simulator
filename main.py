# Microprocessor simulation
# supports a small set of simulated operations
# prints the output for each operation
import sys
#import the function.py helper function
from operations import *


# You need to update the process function to actually handle the operations. To
# start, it just prints out each line of the input.
def process(line):
    #split line into list
    split_line = line.split(" ")
    #loop through each list from the second element in the list 
    operations = [eval(operation) for operation in split_line[1:]]
    #check if the first element in the list is min
    if split_line[0] == 'min':
        #check the length of the arguments
        if len(operations) < 2 or check_type(*operations) == False:
            print(invalid(split_line[0], *operations))
        else:
            print(min_val(*operations))

    #check if the first element is noop
    elif split_line[0] == "noop":
        if len(operations) == 0:
            print(noop())
        else:
            print(invalid(split_line[0], *operations))
    # if the first element is not noop and not min
    else:
        #check the length of the arguments passed
        if Check_lengthOfArgument(*operations) == False:
            print(invalid(split_line[0], *operations))
        else:
            #check the type of arguments passed in
            if check_type(*operations) == False:
                print(invalid(split_line[0], *operations))
            else:
                # if the first element in the list is the or statement
                if split_line[0] == "or":
                    print(logical_or(*operations))
                #if the first element in the list is some other statement
                else:
                    ops = eval(split_line[0])
                    print(ops(*operations))


    
# The run function is provided, you don't need to change it.
# It reads all the lines from a file, then calls the process function
#   for each line 
def run(filename):
    with open(filename, 'r') as file:
        for operation in file.readlines():
            process(operation.strip())

# This code will call the run function with a filename, if it's provided on the 
# command line. It would pass samples/sample2.txt with this invocation:
# python3 main.py samples/sample2.txt
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python main.py [path/to/sample]")
    else:
        run(sys.argv[1])
