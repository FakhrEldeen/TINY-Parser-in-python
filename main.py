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
    

def mulop():
    
    if Parser_input[row][0]=='*':
        match('*')
       
    else:
        match('/')


def addop():
    if Parser_input[row][0] == '+':
        match('+')
       
    else:
        match('-')
    
    print 'addop found\n'
    
    
def comparison_operator():
    
    if Parser_input[row][0] == '<':
        match('<')
    else:
        match('=')
      
    print 'Comparison operator found\n' 

def write_stmt():
    match('write')
    exp()
    print 'write statement found'
    
def simple_exp():
    term()
    
    if Parser_input[row][0] == '+' or Parser_input[row][0] == '-' :
        addop()
        term()
        
    print 'simple_exp found\n'

def exp():
    
    simple_exp()
    
    if Parser_input[row][0] == '<' or Parser_input[row][0] == '=':
        comparison_operator()
        simple_exp()
       
    print 'exp found\n'

def assign_stmt():
    match('ID')
    exp()
    print 'assignment_statement found\n'
    
def factor():
    if Parser_input[row][0] == '(':
        match('(')
        exp()
        
    elif Parser_input[row][1] == 'number' :
        match('number')
        print 'factor found\n'
       
    elif Parser_input[row][1] == 'ID':
        match('ID')
        print 'factor found\n '
       
    else:
        print 'factor error no such number , identifier or (exp)\n'
        
        
def term():
    factor()
    while Parser_input == '*' or Parser_input == '/':
        mulop()
        factor()
       
    print 'term found\n'
