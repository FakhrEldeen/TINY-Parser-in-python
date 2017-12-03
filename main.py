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
    




print(Parser_input[row][0])
advance_input()
print(Parser_input[row][0])
