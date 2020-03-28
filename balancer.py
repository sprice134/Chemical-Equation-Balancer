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

def countOccurences(x):
    counted = list()
    countedResults = dict()
    newList = list()
    for i in range(len(x)):
        if x[i] not in counted:
            counted.append(x[i])
            countedResults[x[i]] = x.count(x[i])
    for i in countedResults:
        for j in range(countedResults[i]):
            newList.append(i)
        
    print(countedResults)
    print(newList)

def handleString(x):
    badChars = ['/', ',', '.', '-',' ','!','^']
    for i in range(len(x)):
        if x[i] in badChars:
            print("Please provide proper syntax")
            return ""
    test = findSyntax(x)
    if len(test) > 0:
        stringSwitchBefore = x[test[0]-1: test[1]+1]
        stringSwitchAfter = x[test[0]:test[1]]
        passes = 0
        if x[test[1]+1].isdigit():
            passes = int(x[test[1]+1])
            x = x[:test[1]+1] + x[test[1]+2:]
        x = x.replace(stringSwitchBefore, '')
        if passes > 0:
            for i in range(passes):
                x += stringSwitchAfter
        else:
            x += stringSwitchAfter
    print(x)
    x = splitAlpha(x)
    print(x) 
    '''length = len(x)
    for i in range(length):
        alphaValues = ''
        numValues = 0
        current = x[i]
        if len(current) > 1:
            for j in range(len(current)):
                if current[j].isdigit():
                    numValues += int(current[j])
                elif current[j].isalpha():
                    alphaValues += current[j]
        x[i] = alphaValues
        for i in range(numValues):
            x.append(alphaValues)'''
    return x

def mainMethod():
    print("Welcome, DISCLAIMER: Can only handle 1 set of parenthases per molecule")
    x = input("What is the first reactant: \n")
    y = handleString(x)
    countOccurences(y)
mainMethod()
