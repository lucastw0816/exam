import sys

def examination():
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("\
        國泰國中的老師出了一道題目給同學們練習，同學們自己設定一串奇偶混和地亂數，並將數字依照” 奇數都在偶數前面”，\n\
        且”偶數升冪排序”，”奇數降冪排序”。例如 ‘417324689435’ 將會變成 ‘975331244468’。然而，班上有50位學生，\n\
        每一個同學給出的數字長度不一，老師希望能用一段小程式來幫助他驗證答案，請你寫一個函數幫幫老師吧!\n\
        輸入: ‘417324689435’\n\
        輸出: ‘975331244468’"
    )
    print("------------------------------------------------------------------------------------------------------------------------------")


def keyInCheck():
    numberSequence = input("Input number sequence : ")
    numberCheck = str.isdigit(numberSequence)

    if numberCheck:
        return numberSequence
    else:
        sys.exit("Input error, not a positive integer or zero.")


def remainderNumberSequence(num):
    tempEven = []
    tempOdd = []
    temp = []

    for item in range (len(num)):
        remainder = num[item]
        if int(remainder) % 2 == 0:
            tempEven.append(remainder) 
        else:
            tempOdd.append(remainder) 

    tempOdd.sort(reverse=True)
    tempEven.sort()
    temp = tempOdd + tempEven

    result = "".join(temp)
    print ("Output remainder number sequence : ", result)

def main():
    examination()
    value = keyInCheck()
    remainderNumberSequence(value)

if __name__ == '__main__':
    main()