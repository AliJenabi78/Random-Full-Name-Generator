# Import the random, string, and names-dataset modules
import random
import string
from names_dataset import NameDataset

# Initialize the name dataset object
nd = NameDataset()

# Define a function to check if the input is a letter
def is_letter(input):
  # Return True if the input is a single letter, False otherwise
  return len(input) == 1 and input.isalpha()

# Define a function to get a letter from the user
def get_letter():
  # Ask the user to enter a letter
  letter = input("Enter a letter: ")
  # Convert the input to uppercase
  letter = letter.upper()
  # Check if the input is valid
  while not is_letter(letter):
    # Print an error message
    print("Invalid input. Please enter a letter only.")
    # Ask the user to enter a letter again
    letter = input("Enter a letter: ")
    # Convert the input to uppercase
    letter = letter.upper()
  # Return the letter
  return letter

# Store all the first names and all the last names in two separate variables
first_names = nd.first_names
last_names = nd.last_names

# Define a function to choose a random name
def choose_name(letter, name_type):
  # Get the list of names that start with the letter and match the name type
  names = [name for name in name_type if name.startswith(letter)]
  # Choose a random name from the list
  name = random.choice(names)
  # Return the name
  return name

# Define a function to generate a random name
def generate_name():
  # Get the first letter from the user
  first_letter = get_letter()
  # Get the second letter from the user
  second_letter = get_letter()
  # Choose a random first name that starts with the first letter
  first = choose_name(first_letter, first_names)
  # Choose a random last name that starts with the second letter
  last = choose_name(second_letter, last_names)
  # Return the full name
  return first + " " + last

# Generate and print a name
name = generate_name()
print("Your name is: " + name)
