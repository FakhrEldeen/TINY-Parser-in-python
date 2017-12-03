f=open("scanner.txt",'r')
my_txt=f.read()
f_lines=my_txt.splitlines()
Parser_input=[]

for i in f_lines:
    Parser_input.append(i.split(' : '))

global row
row=0

def advance_input():
    global row
    row += 1
    
def match(str):
    if Parser_input[row][0] == str:
        advance_input()

    elif Parser_input[row][1] == str:
        advance_input()
    else:
        print ('ERROR found\n')


def read():
    match("read")
    match("ID")
    

def addop():
    if Parser_input[row][0] == '+':
        match('+')
       
    else:
        match('-')
    
    print 'addop found\n'
    

def simple_exp():
    term()
    if Parser_input[row][0] == '+' || Parser_input[row][0] == '-' :
        addop()
        term()
        
    print 'simple_exp found\n'

def comparison_operator():
    
    if Parser_input[row][0] == '<':
        match('<')
    else:
        match('=')
      
    print 'Comparison operator found\n'
    
    
def exp():
    
    simple_exp()
    
    if Parser_input[row][0] == '<' || Parser_input[row][0] == '=':
        comparison_operator()
        simple_exp()
       
    print 'exp found\n'


def write_stmt():
    match('write')
    exp()
    print 'write statement found'

    
def assign_stmt():
    match('ID')
    exp()
    print 'assignment_statement found\n'
    
def factor():
    if temporary_list[row][0] == '(':
        exp()
        
    else:
        match('number')
        print 'factor found\n'
       
    else:
        match('ID'):
        print 'factor found\n '
       
    else:
        print 'factor error no such number , identifier or (exp)\n'
