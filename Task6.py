import re

def main():
    inputMessage = input("Enter line: ")

    # Use regex to match the whole word 'bear'
    if re.search(r'\bbear\b', inputMessage):
        print("There's a bear in there.")
    else:
        print("No bears here.")

if __name__ == '__main__':
    main()
