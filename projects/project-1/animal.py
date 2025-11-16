"""
Project 1 - Favorite Animal

A simple introductory Python program that asks the user for their faorite animal and prints a message in response.

Originally written in January 2022 for OSU CS161 and later refactored for readability and structure.
"""

def main() -> None:
    """Prompt the user for their favorite animal and print a message"""
    favorite_animal = input("Please enter your favorite animal: ")
    print(f"Your favorite animal is the {favorite_animal}.")


if __name__ == "__main__":
    main()

