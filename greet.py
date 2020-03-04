def greet(name):
    """
    Create a function called 'greet' with one 'name' argument, the string will add after 'Hello'
    """
    print('Hello,', name)
    
    
def name_input():
    """
    Create another name_input function that you type your own input to replace the 'name' argumment of 'greet' function
    """
    your_name = input('Enter your name: ')
    greet(your_name)

name_input()
