f=open("scanner.txt",'r')
my_txt=f.read()
f_lines=my_txt.splitlines()
Parser_input=[]

for i in f_lines:
    Parser_input.append(i.split(' : '))

global row
global Error
row=0

def advance_input():
    global row
    row += 1

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


def read():
    global Error
    match("read")
    match("ID")
    if Error == 0:
        print("Read found!")
    else:
         print ('ERROR found : Read statment is not correct')

def repeat ():
    match ("repeat")
    stmt_seq()
    match ("until")
    if Error == 0:
        print("Repeat found!")
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
    if Parser_input[row][0] == "*" or Parser_input[row][0] == "/"
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



def statement():
    if Parser_input[row][0] == "if":
        if_stmt()
    elif Parser_input[row][0] == "repeat":
        repeat()
    elif Parser_input[row][1] == "Assignment":
        assignment()
    elif Parser_input[row][0] == "read":
        read()
    elif Parser_input[row][0] == "write":
        write()
    else:
        global Error
        Error = 1




def stmt_seq():
    statement()
    if Parser_input[row][0] == ";":
        statement()


