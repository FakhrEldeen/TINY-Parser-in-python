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
         print ('ERROR Found : Read statment is not correct \n')




print(Parser_input[row][0])
advance_input()
print(Parser_input[row][0])
