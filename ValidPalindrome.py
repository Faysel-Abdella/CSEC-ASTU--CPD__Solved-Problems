def isPalindrome(text):
    plainText = ""
    for i in range(len(text)):
        if (text[i].isalnum()):
            plainText += text[i]  
    toLower = plainText.lower()
    toBack = toLower[::-1]

    return toLower == toBack

inputText = input()
print(isPalindrome(inputText))