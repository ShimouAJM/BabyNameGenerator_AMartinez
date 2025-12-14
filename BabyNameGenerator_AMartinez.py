# Import the 'random' module so we can use its functions to make random selections
import random


def generate_name(name_type):
    """
    This function allows the user to choose an option (which is '1', '2', or '3')
    for a baby name.
    """
    
    # List of boys names
    boys_names = [
        "Andrew", "Ben", "Chandler", "Dan", "Evan", "Fernando", "Gerald", 
        "Hector", "ivan", "James", "Kevin", "Joel"
    ]
    # List of girls names
    girls_names = [
        "Avery", "Bella", "Candice", "Dahlia", "Eva", "Garnet", 
        "Hailey", "Julia", "Kaylyn", "Lina"
    ]
    # List of neutral names
    neutral_names = [
        "Alex", "Charlie", "Drew", "Frankie", "Morgan", "Parker",
        "Peyton", "Ryan", 
    ]

    # Check the user's choice 
    if name_type == '1':
        # random.choice() selects one item randomly from the list provided
        return random.choice(boys_names)
    elif name_type == '2':
        return random.choice(girls_names)
    elif name_type == '3':
        return random.choice(neutral_names)
    else:
        # If the input was something not expected, return this message
        return "Error in selection"


def main_menu():
    """
    This function keeps the program running.
    """
    print("Welcome to My Final Project, The Baby Name Generator!")
    
    # Start an infinite loop that keeps the program running until the user chooses to exit
    while True:
        
        print("\n -> Choose Name Type <- ")
        print("1. Boys Names")
        print("2. Girls Names")
        print("3. Neutral Names")
        print("4. Exit Program")
        
        # Get input from the user (input() always returns a string)
        choice = input("Enter baby name choice (1, 2, 3, or 4): ")
        
        # Check if the user wants to exit
        if choice == '4':
            print("Thank you for trying the Name Generator!")
            # stops the while loop and ends the program
            break
        # Check if the user made a name choice (1, 2, or 3)
        elif choice in ['1', '2', '3']:
            # Call the 'generate_name' function using the user's choice as input
            generated_name = generate_name(choice)
            # Print the result in a nice format (f-string) 
            print(f"\n Congradulations! Your randomly generated name is: !* {generated_name} *!")
        # Handle cases where the user types something invalid
        else:
            print("\nError: Please enter options (1, 2, 3, or 4).")



# This is where the program actually starts when the file is run.
if __name__ == "__main__":
    # Call the main menu function to start the user interaction
    main_menu()
