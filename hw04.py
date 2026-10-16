# ------------------------------------------------------
#        Name: Malia Lockhart
#       Peers: (add any collaborators)
#  References: Textbook and lecture notes
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """Ask for a sentence until it contains the secret word, dog, or Dog."""
    while True:
        # Get a sentence from the user.
        text = input("Give me a sentence: ")

        # Check if the sentence contains the secret word.
        if secret_word in text:
            print("You used the secret word!")
            break
        else:
            # Check for dog or Dog if the secret word was not found.
            if "dog" in text or "Dog" in text:
                print("You used the word \"dog\" or the word \"Dog\"!")
                break
            else:
                # Repeat if neither condition is true.
                print("Try again")
    



# Task 2
def check_greater():
    """ Ask for 2 inteegers until they are not equal, then print which is greater. """
    while True:
        #Ask for 2 integers
        first = int(input("Give me a first integer: "))
        second = int(input("Give me a second integer: "))
        
        #Comparing the 2
        if first > second:
            print("First is Greater")
            break
        else:
            if second > first:
                print("Second is Greater")
                break
            else:
                #asking for new if they are equal
                print("Try again")



# Task 3
def get_special_numbers():
    """ Print odd numbers from 1 to 40 that are multiples of 3 but not 5. """
    #Loop through the numebrs
    for number in range (1, 41):
        #skip even numbers
        if number % 2 == 0:
            continue
        
        #Skip numbers not multiple of 3
        if number %3 !=0:
            continue
        
        #skip multiples of 5
        if number % 5 == 0:
            continue
        print(number)


# Task 4.a
def my_for_loop():
    """ Chack a short string and print whether each characteris a vowel or a consonant. """
    text = input("Give me a string: ")
    
    #returning if the string is too short/long
    if len(text) < 2 or len(text) > 5:
        return
    
    #Return if space
    if " " in text:
        return
    
    #checking vowels and consonants
    for letter in text:
        if letter.lower() in "aeiou":
            print(f"{letter} is a vowel")   
        else:
            print(f"{letter} is a consonant")

# Task 4.b
def my_while_loop():
    """Repeat a menu until the user chooses to return or exit."""
    while True:
        # Ask the user to choose an option.
        choice = input("Choose one option: a, b, or c: ")

        # If the user chooses a, repeat the menu.
        if choice == "a":
            continue
        else:
            # If the user chooses b, print Goodbye and return.
            if choice == "b":
                print("Goodbye")
                return
            else:
                # If the user chooses c, exit the program.
                if choice == "c":
                    sys.exit()
                else:
                    # Handle an invalid choice.
                    print("try again")

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
