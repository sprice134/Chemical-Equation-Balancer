def splitAlpha(x):
    y = list()#y is a list of capital seperated components, splicing a string with a name was goiing to be way to complicated
    for i in range(len(x)):
        if x[i].isupper():
            y.append(i)
    if len(y) == 1:
        print(x)
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
    for i in range(len(x)):
        if (x[i].isalpha() == False):
            if x[i] == "(":
                y = i
                count += 1
            elif x[i] == ")":
                z = i
                count -= 1
    if count != 0:
        print("Please make sure you have the right syntax")
        return []
    a.append(y+1)
    a.append(z)
    return a

def mainMethod():
    print("Welcome, DISCLAIMER: Can only handle 1 set of parenthases per molecule")
    x = input("What is the first reactant: \n")
    test = findSyntax(x)
    if len(test) > 0:
        print(x[test[0]:test[1]])

mainMethod()
