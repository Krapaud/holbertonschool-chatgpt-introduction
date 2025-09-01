#!/usr/bin/python3
"""Script to print command line arguments (excluding script name)."""
import sys


def main():
    """Main function to handle argument printing."""
    if len(sys.argv) == 1:
        print("No arguments provided.")
        print("Usage: python3 print_arguments.py <arg1> <arg2> ...")
        sys.exit(0)

    for argument in sys.argv[1:]:
        print(argument)


if __name__ == "__main__":
    main()
