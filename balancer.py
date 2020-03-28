def splitAlpha(x):
    y = list()
    print(len(x))
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
        print(sections)


def mainMethod():
    print("Welcome")
    x = input("What is the first reactant: \n")
    splitAlpha(x)

mainMethod()
