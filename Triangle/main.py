import sys

STRING = '*'

def examination():
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("\
        請設計一個函數，輸入為數字，輸出則為*符號為輸入數字邊長的空心正三角形。\n\
        輸入: 3\n\
        輸出：\n\
                *\n\
               * *\n\
              * * *"
    )   
    print("------------------------------------------------------------------------------------------------------------------------------")


def keyInCheck():
    length = input("Input EquilateralTriangle Side Length : ")
    lengthCheck = str.isdigit(length)

    if lengthCheck:
        if int(length) == 0:
            sys.exit("Side length can't be zero")
        else:
            return int(length)
    else:
        sys.exit("Input error, not a positive integer.")


def printEquilateralTriangle(length):
    print("EquilateralTriangle length is", length)
    print("Print geometric design of", STRING,"...")
    flagSpace = False

    for numClass in range (length):
        for numSymbol in range (length*2-1):
            if (numClass+numSymbol == length-1 or numSymbol-numClass == length-1):
                print(STRING, end='')
            elif numClass == length-1:
                if flagSpace:
                    print(STRING, end='')
                    flagSpace = False
                elif not flagSpace:
                    flagSpace = True
                    print(' ', end='')
            else:
                print(' ', end='')
        print('')
    print("Complete printing")


def main():
    examination()
    value = keyInCheck()
    printEquilateralTriangle(value)

if __name__ == '__main__':
    main()
