with open('file.txt') as file:
    text = file.read().splitlines()

text = [row.strip() for row in text]

namespace = {}

def make_variable(x,y):
    try:
        namespace[x] = int(y) 

    except y.isnumeric():
        namespace[x] = int(y)

    finally:
        namespace[x] = y

    return namespace

def for_1(a,action):
    

    for x in range(a):
        print(action)

def for_2(a, b, action):
    
    for x in range(a, b):
        print(action)

def for_3(a, b, c, action):
    
    for x in range(a, b, c):
        print(action)

def add_(a, b):
    return a + b


def sub_(a, b):
    return a - b

def div_(a, b):
    return a / b

def mul_(a, b):
    return a * b

def print_(a):
    return a
    


for row in text:

    splitted_row = row.split()
    print(splitted_row)


    if splitted_row[0] == 'pop':


        if splitted_row[1][0].isalpha() and splitted_row[2] == "=":

            if len(splitted_row) == 4:
                make_variable(splitted_row[1],splitted_row[3])
        
            elif len(splitted_row) == 6:

                if splitted_row[3] in namespace:
                   
                   if namespace[splitted_row[3]].isnumeric():
                        a = int(namespace[splitted_row[3]])
                
                elif splitted_row[3].isnumeric():
                    a = int(splitted_row[3])
                
                else:
                    raise ValueError("Wrong value")
                
                
                if splitted_row[5] in namespace:

                    if namespace[splitted_row[5]].isnumeric():
                        b = int(namespace[splitted_row[5]])
                
                elif splitted_row[5].isnumeric():
                    b = int(splitted_row[5])
                
                else:
                    raise ValueError("Wrong value")
                
                if splitted_row[4] == "+":
                    make_variable(splitted_row[1], add_(a, b))

                elif splitted_row[4] == "-":
                    make_variable(splitted_row[1], sub_(a, b))

                elif splitted_row[4] == "*":
                    make_variable(splitted_row[1], mul_(a, b))

                elif splitted_row[4] == "/":
                    make_variable(splitted_row[1], div_(a, b))
                
                else:
                    raise SyntaxError("Wrong syntax")

        else:
            raise SyntaxError("Wrong syntax")
        
        
    elif splitted_row[0] == "cik":

        if type(splitted_row[1]) == str:

            if splitted_row [2] == 'in' and splitted_row[3] == 'mij' and splitted_row[4] == '(' :
                
                if splitted_row[5].isnumeric() :
                        
                            if splitted_row[6] == ')':
                                
                                if splitted_row[7] == '->':

                                    if splitted_row[8] == 'tpi':
                                
                                        if splitted_row [9] == '(' and splitted_row[11] == ')':
                                
                                            if splitted_row [10].isnumeric():
                                                for_1(int(splitted_row[5]),print_(int(splitted_row[10])))

                                            else:   
                                                if splitted_row[10] in namespace:
                                                    for_1(int(splitted_row[5]),print_(namespace[splitted_row[10]]))

                                                elif (splitted_row[10] == '"' and splitted_row[12] == '"') or (splitted_row[10] == "'" and splitted_row[12] == "'"):
                                                    for_1(int(splitted_row[5]),print_(splitted_row[11]))
                                                
                                        else:
                                            raise SyntaxError("Wrong syntax")
                            
                                else:
                                    raise SyntaxError("Wrong syntax")

                            elif splitted_row[6] == ',' and splitted_row[8] == ')':

                                if splitted_row[7].isnumeric():

                                    if splitted_row[9] == '->':

                                        if splitted_row[10] == 'tpi':
                                
                                            if splitted_row [11] == '(' and splitted_row[13] == ')':
                                
                                                if splitted_row [12].isnumeric():
                                                    for_2(int(splitted_row[5]),int(splitted_row[7]),print_(int(splitted_row[12])))

                                                else:   
                                                    if splitted_row[12] in namespace:
                                                        for_2(int(splitted_row[5]),int(splitted_row[7]),print_(namespace[splitted_row[12]]))

                                                    elif (splitted_row[12] == '"' and splitted_row[14] == '"') or (splitted_row[12] == "'" and splitted_row[14] == "'"):
                                                        for_2(int(splitted_row[5]),int(splitted_row[7]),print_(splitted_row[13]))
                                                
                                            else:
                                                raise SyntaxError("Wrong syntax")
                            
                                    else:
                                        raise SyntaxError("Wrong syntax")

                            elif splitted_row[6] == "," and splitted_row[8] == "," and splitted_row[10] == ")":

                                if splitted_row[7].isnumeric() and splitted_row[9].isnumeric():
                                    
                                    if splitted_row[11] == '->':

                                        if splitted_row[12] == 'tpi':
                                
                                            if splitted_row [13] == '(' and splitted_row[15] == ')':
                                
                                                if splitted_row [14].isnumeric():
                                                    for_3(int(splitted_row[5]),int(splitted_row[7]),int(splitted_row[9]),print_(int(splitted_row[14])))

                                                else:   
                                                    if splitted_row[14] in namespace:
                                                        for_3(int(splitted_row[5]),int(splitted_row[7]),int(splitted_row[9]),print_(namespace[splitted_row[14]]))

                                                    elif (splitted_row[14] == '"' and splitted_row[16] == '"') or (splitted_row[14] == "'" and splitted_row[16] == "'"):
                                                        for_3(int(splitted_row[5]),int(splitted_row[7]),int(splitted_row[9]),print_(splitted_row[15]))
                                                
                                            else:
                                                raise SyntaxError("Wrong syntax")
                            
                                    else:
                                        raise SyntaxError("Wrong syntax")

                                else:
                                    raise TypeError("Wrong type")
                            
                            else:
                                raise SyntaxError("Wrong syntax")
                        
                else:
                    raise TypeError("Wrong type")

            else:
                raise SyntaxError("Wrong syntax")
        
        else:
            raise TypeError("Wrong type")
              
print(namespace)



