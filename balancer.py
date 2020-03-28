def splitAlpha(x):
    y = list()#y is a list of capital seperated components, splicing a string with a name was goiing to be way to complicated
    for i in range(len(x)):
        if x[i].isupper():
            y.append(i)
    if len(y) == 1:
        return x
    elif len(y) > 1:
        sections = list()
        for i in range(len(y)):
            if i < len(y) -1:
                sections.append(x[y[i]:y[i+1]])
            else:
                sections.append(x[y[-1]:])
        return sections

def findSyntax(x):
    y = int()
    z = int()
    count = 0
    a = list()
    hasSyntax = False
    for i in range(len(x)):
        if (x[i].isalpha() == False):
            if x[i] == "(":
                y = i
                count += 1
                hasSyntax = True
            elif x[i] == ")":
                z = i
                count -= 1
    if count != 0:
        print("Please make sure you have the right syntax")
        return []
    elif hasSyntax:
        a.append(y+1)
        a.append(z)
        return a
    else:
        return []

def eliminateSyntax(num1, num2, x):
    stringSwitchBefore = x[num1-1: num2+1]
    stringSwitchAfter = x[num1:num2]
    passes = 0
    if x[num2+1].isdigit():
        passes = int(x[num2+1])
        x = x[:num2+1] + x[num2+2:]
    x = x.replace(stringSwitchBefore, '')
    if passes > 0:
        for i in range(passes):
            x += stringSwitchAfter
    else:
        x += stringSwitchAfter
    return x

def countOccurences(x):
    newList = list()
    newList2 = list()
    for i in x:
        string = ''
        num = ''
        for j in range(len(i)):
            if i[j].isalpha():
                string += i[j]
            elif i[j].isdigit():
                num += i[j]
        if num != '':
            for k in range(int(num)):
                newList2.append(string)
        elif num == '':
            newList2.append(string)
    counted = []
    countedResults = {}
    for i in range(len(newList2)):
        if newList2[i] not in counted:
            counted.append(newList2[i])
            countedResults[newList2[i]] = newList2.count(newList2[i])
    return countedResults


def handleString(x):
    badChars = ['/', ',', '.', '-',' ','!','^']
    for i in range(len(x)):
        if x[i] in badChars:
            print("Please provide proper syntax")
            return ""
    test = findSyntax(x)
    if len(test) > 0:
        x = eliminateSyntax(test[0], test[1], x)
    x = splitAlpha(x)
    x = countOccurences(x) 
    return x

def mainMethod():
    print("Welcome, DISCLAIMER: Can only handle 1 set of parenthases per molecule")
    x = input("What is the first reactant: \n")
    y = handleString(x)
    print(y)
mainMethod()
