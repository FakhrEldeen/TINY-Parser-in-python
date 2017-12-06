f=open("scanner.txt",'r')
my_txt=f.read()
f_lines=my_txt.splitlines()
Parser_input=[]

for i in f_lines:
    Parser_input.append(i.split(' : '))

global row 
global Error
global write_counter
global Factor_counter
write_counter=0
Factor_counter=0
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
        Error = 0

    elif Parser_input[row][1] == str:
        advance_input()
        Error = 0
    else:
        Error = 1

def mul_op():
    if Parser_input[row][0] == '*':
        match('*')

    else:
        match('/')

    if Error == 0:
        print('mul operator found')

    else:
        print("can't match mull operator , error in mul operator")

def add_op():
    if Parser_input[row][0] == '+':
        match('+')

    else:
        match('-')

    if Error == 0:
        print('add_op found')

    else:
        print("can't match add_op , error in add_op")

def comp_op():
    if Parser_input[row][0] == '<':
        match('<')
    else:
        match('=')

    if Error == 0:
        print('Comparison operator found')

    else:
        print("can't match comparison operator")

def program():
    stmt_seq()

    if Error == 0:
        print('program found')

    else:
        print('Error in the Program')

def read_stmt():
    global Error
    match("read")
    match("ID")
    if Error == 0:

        print("Read found")
        prog.node(name='R',label='Read\n'+'('+Parser_input[row-1][0]+')',shape='square')
    else:
        print('ERROR found : Read statment is not correct')

def repeat_stmt():
    match("repeat")
    stmt_seq()
    match("until")
    exp()
    if Error == 0:
        print("Repeat found")
    else:
        print('ERROR found : Repeat statment is not correct')

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
        print('assignment_statement found')

    else:
        print("migth be an error in identifier")

def statement():
    if Parser_input[row][0] == "if":
        if_stmt()
    elif Parser_input[row][0] == "repeat":
        repeat_stmt()
    elif Parser_input[row][1] == "ID" and Parser_input[row + 1][1] == "Assignment":
        assign_stmt()
    elif Parser_input[row][0] == "read":
        read_stmt()
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
        if row > (len(Parser_input) - 1):
            break

    if Error == 0:
        print('Statement sequence found')

def write_stmt():
    global Error
    global write_counter
    match('write')
    exp()

    if Error == 0:
        print('write statement found')
        prog.node(name='W'+str(write_counter),label='write',shape='square')
        prog.edge('W'+str(write_counter),'F'+str(Factor_counter-1))
        if write_counter >0:
            with prog.subgraph() as c:
                c.attr(rank='same')
                c.edge('W'+str(write_counter-1),'W'+str(write_counter))
        write_counter+=1

    else:
        print('Error in write statement')

def simple_exp():
    term()
    if row <= (len(Parser_input) - 1):
        if Parser_input[row][0] == '+' or Parser_input[row][0] == '-':
            dot.node(Parser_input[row][0],"(op)\n"+Parser_input[row][0])
            dot.edge(Parser_input[row][0],node.body[0][1])
            add_op()
            term()

    print('simple_exp found')


def exp():
    simple_exp()

    if row <= (len(Parser_input) - 1):
        if Parser_input[row][0] == '<' or Parser_input[row][0] == '=':
            dot.node(Parser_input[row][0],"op\n"+Parser_input[row][0])
            dot.edge(Parser_input[row][0],node.body[0][1])
            comp_op()
            simple_exp()

    print('exp found')
    

def factor():
    global Error
    global Factor_counter
    if Parser_input[row][0] == '(':
        match('(')
        exp()
        match(')')

    elif Parser_input[row][1] == 'number':
        prog.node(name='F'+str(Factor_counter),label='number\n(fact)')
        match('number')

        if Error == 0:
            print('factor found as a number')
            Factor_counter+=1

        else:
            print('factor error , might be an error in matching number')

    elif Parser_input[row][1] == 'ID':
        prog.node(name='F'+str(Factor_counter),label='id\n(fact)')
        match('ID')


        if Error == 0:
            print('factor found as an identifier')
            Factor_counter+=1


        else:
            print('factor error , might be an error in matching identifier')

    else:
        Error = 1
        print('factor error no such number , identifier or (exp)')

def term():
    factor()
    if row <= (len(Parser_input) - 1):
        while Parser_input[row][0] == '*' or Parser_input[row][0] == '/':
            dot.node(Parser_input[row][0],"op\n"+Parser_input[row][0])
            dot.edge(Parser_input[row][0],node.body[0][1])
            mul_op()
            factor()
            if row > (len(Parser_input) - 1):
                break

    print('term found')
