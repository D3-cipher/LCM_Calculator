# Author: Timothy Hubbard
# Version 1.0
# Formula Written by: Danish Raza aquired from geeksforgeeks.org
# Formula Website: https://www.geeksforgeeks.org/program-to-find-lcm-of-two-numbers/


def welcome():
    print("Welcome to Finding the LCM Calculator\nVersion 1.0\nType exit to exit the program")
    start()


# Function to process the LCM of more than two numbers
def getlcmofthree(numarray):
    num1 = numarray[0]
    num2 = numarray[1]
    num3 = numarray[2]

    # Calculates the GCF
    def gcd(num1, num2):
            if num1 == 0:
                return num2
            return gcd(num2 % num1, num1)

    # Calculates the LCM after the GCF is found
    def lcm(num1, num2):
        return (num1 / gcd(num1, num2))* num2
    # Returns the LCM to the main function start()    
    return lcm(num1, lcm(num2, num3))


# Function to process the LCM of the input given in start()
def getlcmNums(numarray, greater): 
    
    num1 = numarray[0]
    num2 = numarray[1]

    # Filter to identify if there are two or three numbers
    if greater == True:

        return getlcmofthree(numarray)

    elif greater == False:

        def gcd(num1, num2):
            if num1 == 0:
                return num2
            return gcd(num2 % num1, num1)
        

        def lcm(num1, num2):
            return (num1 / gcd(num1, num2))* num2
        
        return lcm(num1, num2)


# Main Function where inputs are taken
def start():
    numbers = input("Enter Numbers >>> ")
    
    if numbers == "exit":
        exit

    else:
        # For Error Handling 
        try:

            numarray = [int(i) for i in numbers.split(' ')]
            length = len(numarray)

        except:
            
            print("Enter a number not a string.")
            print("Exit code 0")
            start()
        
        # Filter for figuring out how many numbers there are and where they go
        if length == 1:
            print("Enter more than one number.")
            start()
        elif length == 2:
            getlcmNums(numarray, greater = False)
            print("The LCM is", getlcmNums(numarray, greater = False))
            start()
        elif length == 3:
            getlcmNums(numarray, greater = True)
            print("The LCM is", getlcmNums(numarray, greater = True))
            start()
        elif length <= 4:
            print("Can only process 3 numbers at a time")
            start()


# Main Function Call
welcome()