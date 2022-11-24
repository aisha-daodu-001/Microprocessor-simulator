def noop(*args):
    """
    This function takes no argument
    It does nothing and print an empty line
    """
    return ""
    
def add(*num):
    """
    This function takes just 2 arguments of type int.
    It calculates the sum of the 2 arguments.
    Returns:
        _type_: integer
    """
    num1,num2= tuple(num)
    return num1 + num2
    

def mul(*num):
    """
    Takes just 2 arguments of type int and calculate their product
    Returns:
        _type_: integer
    """
    num1,num2= tuple(num)
    return num1 * num2

def logical_or(*num):
    """
    Takes just 2 argument of type int and find the logical OR of 
    the 2 arguments
    Returns:
        1 if any of the numbers is True(number > 0)
        0 if both numbers are False(0)
    """
    num1,num2= tuple(num)
    if num1 == 0 and num2 == 0:
        return 0
    else:
        return 1

def nand(*num):
    """
    Takes just 2 arguments of type int and find the 
    logical NAND(NOT AND) of the 2 arguments.
    Returns:
        1 if the logical NAND of the 2 arguments is True
        0 if the logical NAND of the 2 arguments is False
    """
    num1,num2= tuple(num)
    if not(num1 and num2) == False:
        return 0
    else:
        return 1

def gt(*num):
    """
    Takes just 2 arguments of type int and check if the 
    first argument is greater than the second 
    argument
    Returns:
        1 if num1 > num2
        0 if num1 < num2
    """
    num1,num2= tuple(num)
    if num1 > num2:
        return 1
    else:
        return 0
    
def shift(*num):
    """
    Accepts just 2 arguments of type int.
    Shift argument 1 to the left by the 
    number of bits of argument 2. 
    Only accepts positive integers.
    Prints invalid for any negative or zero value.
    Returns:
        _type_: int
    """
    num1,num2= tuple(num)
    if num1 <= 0 or num2 <= 0:
        return invalid("shift", *num)
    else:
        return num1 << num2

def min_val(*num):
    """
    Accepts two or more arguments of type int and 
    returns the minimum value of the arguments
    Returns:
        _type_: int
    """
    return min(num)  

def invalid(ops, *nums):
    """
    This function is called when the processor
    sees any non-valid operation. It prints out 
    a message to show that the operation is invalid 
    and stop the processors simulation process.
    """
    number = []
    for i in nums:
        number.append(str(i))
    numbers = " ".join(number)
    return f"invalid operation {ops} {numbers}"



def Check_lengthOfArgument(*num):
    """
    check the length of the argument passed if it is exactly 2
    Returns:
        _type_: Bool(True or False)
    """
    if len(num) != 2:
        return False
    else:
        return True

def check_type(*args):
    """
    Takes in arguments to check if their datatypes
    correspond to integer. Returns False if there exist
    any other datatype apart from integer in the arguments and 
    True if all arguments are of type int.
    Returns:
        _type_: Bool(True or False)
    """
    data_type = []
    for i in args:
        if type(i) != int:
            data_type.append("invalid")
        else:
            data_type.append("valid")
    if "invalid" in data_type:
        return False
    else:
        True
