import sys

if __name__ == "__main__":
    if "--arg" in sys.argv: # put in "arg" your argument
        print("arg!")
    else:
        print("else arg")

        # usage: python name.py --arg
