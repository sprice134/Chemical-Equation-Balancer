import copy
def splitAlpha(x):
    y = list()#y is a list of capital seperated components, splicing a string with a name was goiing to be way to complicated
    for i in range(len(x)):
        if x[i].isupper():
            y.append(i)
    if len(y) == 1:
        z = list()
        z.append(x)
        return z
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

def convertMolecule(x):
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

def combineDicts(x):
    total = list()
    for i in range(len(x)):
        for j in x[i]:
            for k in range((x[i])[j]):
                total.append(j)
    return countOccurences(total)

def multipyMolecule(x, num):
    for i in x:
        x[i] *= num
    return x

def basicUI():
    print("Welcome, DISCLAIMER: Can only handle 1 set of parenthases per molecule")
    r = int(input("How many reactants\n"))
    p = int(input("How many products\n"))
    reactants = list()
    products = list()
    re = list()
    pr = list()
    for i in range(r):
        x = input("What is reactant #" + str(i+1) + ":\n")
        reactants.append(convertMolecule(x))
        re.append(x)
    for i in range(p):
        x = input("What is product #" + str(i+1) + ":\n")
        products.append(convertMolecule(x))
        pr.append(x)
    reactantsCombined = combineDicts(reactants)
    productsCombined = combineDicts(products)
    count = 0
    if reactantsCombined == productsCombined:
        print("Already Balanced")
        return
    else:
        if r == 2 and p == 2:
            x = loopPossibilities22(reactants, products)
            count = 1
        elif r == 1 and p == 2:
            x = loopPossibilities12(reactants, products)
            count = 2
        elif r == 2 and p == 1:
            x = loopPossibilities21(reactants, products)
            count = 3
        elif r == 1 and p == 3:
            x = loopPossibilities13(reactants, products)
            count = 4
        elif r == 3 and p == 1:
            x = loopPossibilities31(reactants, products)
            count = 5
        if x == '':
            print("Not possible within this margin")
        else:
            if count == 1:
                print(str(x[0]) + re[0] + " + " + str(x[1]) + re[1] + " -> " + str(x[2]) + pr[0] + ' + ' + str(x[3]) + pr[1])
            elif count == 2:
                print(str(x[0]) + re[0] + " -> " + str(x[1]) + pr[0] + ' + ' + str(x[2]) + pr[1])
            elif count == 3:
                print(str(x[0]) + re[0] + ' + ' + str(x[1]) + re[1] + " -> " + str(x[2]) + pr[0])
            elif count == 4:
                print(str(x[0]) + re[0] + " -> " + str(x[1]) + pr[0] + " + " + str(x[2]) + pr[1]  + ' + ' + str(x[3]) + pr[2])
            elif count == 5:
                print(str(x[0]) + re[0] + " + " + str(x[1]) + re[1] + " + " + str(x[2]) + re[2]  +  " -> "+ str(x[3]) + pr[0])
            elif count == 0:
                print(':(')

 
def loopPossibilities22(r, p):
    for x in range(2,8):
        for i in range(1,x):
            for j in range(1,x):
                for k in range(1, x):
                    for l in range(1,x):
                        r1 = copy.deepcopy(r[0])
                        r2 = copy.deepcopy(r[1])
                        p1 = copy.deepcopy(p[0])
                        p2 = copy.deepcopy(p[1])
                        reactants = [multipyMolecule(r1, i), multipyMolecule(r2, j)]
                        products = [multipyMolecule(p1, k), multipyMolecule(p2, l)]
                        reactantsCombined = combineDicts(reactants)
                        productsCombined = combineDicts(products)
                        if reactantsCombined == productsCombined:
                            return [i,j,k,l]
    return ''
def loopPossibilities12(r, p):
    for x in range(2,8):
        for i in range(1,x):
            for j in range(1,x):
                for k in range(1, x):
                    r1 = copy.deepcopy(r[0])
                    p1 = copy.deepcopy(p[0])
                    p2 = copy.deepcopy(p[1])
                    reactants = [multipyMolecule(r1, i)]
                    products = [multipyMolecule(p1, j), multipyMolecule(p2, k)]
                    reactantsCombined = combineDicts(reactants)
                    productsCombined = combineDicts(products)
                    if reactantsCombined == productsCombined:
                        return [i,j,k]
    return ''
def loopPossibilities21(r, p):
    for x in range(2,8):
        for i in range(1,x):
            for j in range(1,x):
                for k in range(1, x):
                    r1 = copy.deepcopy(r[0])
                    r2 = copy.deepcopy(r[1])
                    p1 = copy.deepcopy(p[0])
                    reactants = [multipyMolecule(r1, i), multipyMolecule(r2, j)]
                    products = [multipyMolecule(p1, k)]
                    reactantsCombined = combineDicts(reactants)
                    productsCombined = combineDicts(products)
                    if reactantsCombined == productsCombined:
                        return [i,j,k]
    return ''
def loopPossibilities13(r, p):
    for x in range(2,8):
        for i in range(1,x):
            for j in range(1,x):
                for k in range(1, x):
                    for l in range(1,x):
                        r1 = copy.deepcopy(r[0])
                        p1 = copy.deepcopy(p[0])
                        p2 = copy.deepcopy(p[1])
                        p3 = copy.deepcopy(p[2])
                        reactants = [multipyMolecule(r1, i)]
                        products = [multipyMolecule(p1, j), multipyMolecule(p2, k), multipyMolecule(p3, l)]
                        reactantsCombined = combineDicts(reactants)
                        productsCombined = combineDicts(products)
                        if reactantsCombined == productsCombined:
                            return [i,j,k,l]
    return ''
def loopPossibilities31(r, p):
    for x in range(2,8):
        for i in range(1,x):
            for j in range(1,x):
                for k in range(1, x):
                    for l in range(1,x):
                        r1 = copy.deepcopy(r[0])
                        r2 = copy.deepcopy(r[1])
                        r3 = copy.deepcopy(r[2])
                        p1 = copy.deepcopy(p[0])
                        reactants = [multipyMolecule(r1, i), multipyMolecule(r2, j), multipyMolecule(r3, k)]
                        products = [multipyMolecule(p1, l)]
                        reactantsCombined = combineDicts(reactants)
                        productsCombined = combineDicts(products)
                        if reactantsCombined == productsCombined:
                            print([i,j,k,l])
                            return [i,j,k,l]
    return ''
def loopPossibilities23():
    pass
def loopPossibilities32():
    pass

def mainMethod():
    basicUI()

mainMethod()
