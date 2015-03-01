#Script that simulates the game fizzbuzz
#Expects one optional command line parameter as the upper limit to count
#If not provided, then the script will count up to 100

import sys


def fail(message):
    '''Function to raise exception
    @param {string} message - Message to show with exception
    '''
    raise Exception(message)


def is_divisble(divisor,divident):
    '''Function to check whether a number is divisble by another number
    Throws exception if divident is 0 or if one of the parameters cannot be cast to int
    @param {int} divisor - The divisor
    @param {int} divident - The divident
    @return {boolean} Returns true if divisble, false if not
    '''
    try:
        divisor=int(divisor)
        dividient=int(divident)
    except:
        fail("Both parameters needs to be numbers")
    if divident == 0:
        fail("Division by zero not allowed")
    if divisor % divident == 0:
        return True
    else:
        return False
    
#Some constants
UPPER_LIMIT = 100

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        try:
            UPPER_LIMIT = int(sys.argv[1])
        except:
            fail("Command line parameter needs to be castable to int")
            
    for a in range(1,UPPER_LIMIT):
        if is_divisble(a,3) and is_divisble(a,5):
            print "fizz buzz "
        elif is_divisble(a,3):
            print "fizz "
        elif is_divisble(a,5):
            print "buzz "
        else:
            print str(a) + " "