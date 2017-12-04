f=open("scanner_output.txt",'r')
my_txt=f.read()
f_lines=my_txt.splitlines()
Parser_input=[]

for i in f_lines:
    Parser_input.append(i.split(' : '))

global row
global Error
row=0
Error=0

def advance_input():
    global row
    row += 1
    return


def match(str):
    global Error
    if Parser_input[row][0] == str:
        advance_input()
        Error =0

    elif Parser_input[row][1] == str:
        advance_input()
        Error =0
    else:
        Error =1

def mulop():

    if Parser_input[row][0]=='*':
        match('*')

    else:
        match('/')

    if Error == 0:
        print ('mul operator found')

    else:
        print ("can't match mull operator , error in mul operator")


def addop():
    if Parser_input[row][0] == '+':
        match('+')

    else:
        match('-')

    if Error == 0:
        print ('addop found')

    else:
        print ("can't match addop , error in addop")

def comparison_operator():

    if Parser_input[row][0] == '<':
        match('<')
    else:
        match('=')

    if Error == 0:
        print ('Comparison operator found')

    else:
        print ("can't match comparison operator")

def program():
    stmt_seq()

    if Error ==0 :
        print ('program found')

    else:
        print ('Error in the Program')

def read():
    global Error
    match("read")
    match("ID")
    if Error == 0:

        print ("Read found")
    else:
         print ('ERROR found : Read statment is not correct')


def repeat ():
    match ("repeat")
    stmt_seq()
    match ("until")
    exp()
    if Error == 0:
        print("Repeat found")
    else:
         print ('ERROR found : Repeat statment is not correct')


def mulop():
    if Parser_input[row][0]== "*":
        match("*")
    elif Parser_input[row][0]== "/":
        match("/")
    else :
        global Error
        Error =1


def term():
    factor()
    if Parser_input[row][0] == "*" or Parser_input[row][0] == "/":
        mulop()
    factor()




def if_stmt():
    match("if")
    exp()
    match("then")
    stmt_seq()
    if Parser_input[row][0] == "else":
        stmt_seq()
    match("end")

    if Error == 0:
        print("If statement found")
    else:
        print("ERROR in if statement")

def assign_stmt():
    global Error
    match('ID')
    match(":=")
    exp()

    if Error == 0:
        print ('assignment_statement found')

    else:
        print ("migth be an error in identifier")

def statement():
    if Parser_input[row][0] == "if":
        if_stmt()
    elif Parser_input[row][0] == "repeat":
        repeat()
    elif Parser_input[row][1] == "ID" and Parser_input[row+1][1] == "Assignment":
        assign_stmt()
    elif Parser_input[row][0] == "read":
        read()
    elif Parser_input[row][0] == "write":
        write_stmt()
    else:
        global Error
        Error = 1

def stmt_seq():
    statement()
    while Parser_input[row][0] == ";":
        advance_input()
        statement()
        if row > (len(Parser_input)-1):
            break

    if Error == 0:
        print ('Statement sequence found')

def write_stmt():
    global Error
    match('write')
    exp()

    if Error == 0:
        print ('write statement found')

    else :
        print ('Error in write statement')

def simple_exp():
    term()
    if row <= (len(Parser_input)-1):
        if Parser_input[row][0] == '+' or Parser_input[row][0] == '-' :
            addop()
            term()

    print ('simple_exp found')




def exp():

    simple_exp()

    if row <= (len(Parser_input)-1):
        if Parser_input[row][0] == '<' or Parser_input[row][0] == '=' :
            comparison_operator()
            simple_exp()

    print ('exp found')



def factor():
    global Error
    if Parser_input[row][0] == '(':
        match('(')
        exp()
        match(')')

    elif Parser_input[row][1] == 'number' :
        match('number')

        if Error == 0:
            print ('factor found as a number')

        else:
            print ('factor error , might be an error in matching number')

    elif Parser_input[row][1] == 'ID':
        match('ID')

        if Error == 0:
            print ('factor found as an identifier')

        else:
            print ('factor error , might be an error in matching identifier')

    else:
        Error=1
        print ('factor error no such number , identifier or (exp)')


def term():
    factor()
    while Parser_input[row][0] == '*' or Parser_input[row][0] == '/':
        mulop()
        factor()
        if row > (len(Parser_input)-1):
            break


    print ('term found')

program()
