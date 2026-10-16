# ------------------------------------------------------
#        Name: (put your name here)
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ Ask for a sentence until it contrains the secret word, dog, or Dog. """
    while True:
        #Get a sentence from the user.
        text = input("Give me a sentence: ")
        
        #check if the sentence contains the secret word
        if secret_word in text:
            print("You used the secret word!")
            break
        else:
            #check for dog or Dog if the secret word was not found
            if "dog" in text or "Dog" in text:
                print("You used the work \"dog\" or the word \"Dog\" !")
                break
            
            else:
                #Repeat if neither condition is true
                print("Try again")
    pass



# Task 2
def check_greater():
    """ Add your docstring """
    pass



# Task 3
def get_special_numbers():
    """ Add your docstring """
    pass


# Task 4.a
def my_for_loop():
    """ Add your docstring """
    pass

# Task 4.b
def my_while_loop():
    """ Add your docstring """
    pass

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
