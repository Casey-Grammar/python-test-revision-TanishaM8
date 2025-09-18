import re

def main():
    inputMessage = input("Enter line: ")

    # Match 'bear' as a whole word or prefix (e.g., 'bearish'), but not 'bears'
    if re.search(r'\bbear(?!s)\w*\b', inputMessage):
        print("There's a bear in there.")
    else:
        print("No bears here.")

if __name__ == '__main__':
    main()
