"""
Project 1 - Favorite Animal

A simple introductory Python program that asks the user for their favorite animal and
prints a message in response.

Originally written in January 2022 for OSU CS161 and later refactored for readability
and structure.
"""

def make_message(animal: str) -> str:
    """Return the message printed by the program."""
    return f"Your favorite animal is the {animal}."

def main() -> None:
    """Prompt the user for their favorite animal and print the message."""
    favorite = input("Please enter your favorite animal: ")
    print(make_message(favorite))


if __name__ == "__main__":
    main()

