# moshe malka
def calcRPN(content):
    s = content.split(" ")
    for x in range(len(s)):
        if('\n' in s[x]):
            s[x]=s[x].split('\n')[0]
    stack=[]
    sc=['*','/','+','-']
    for i in range(len(s)):
        if(s[i] not in sc):
            stack.append(int(s[i]))
        else:
            if(len(stack)<1):
                print "stack length smaller then 1"
                break
            else:
                a=stack.pop()
                b=stack.pop()
                if(s[i]=='*'): stack.append(int(b) * int(a))
                elif(s[i]=='/'): stack.append(int(b) / int(a))
                elif(s[i]=='+'): stack.append(int(b) + int(a))
                else:       #(s[i]=='-') 
                    stack.append(int(b) - int(a)) 
    if(len(stack)==1):
        return stack[0]

def printSpacer():
    print "<"+'-'*60+">"

def do_testing():
    print "Formula : 158485229 9783012491151707981 12863415996971411282 - /"
    print "Answer :"
    print calcRPN("158485229 9783012491151707981 12863415996971411282 - /")
    printSpacer()
    
    print "Formula : 14081963685289588427 1062648031 4138656300 286578566 * - 807969713 + *"
    print "Answer :"
    print calcRPN("14081963685289588427 1062648031 4138656300 286578566 * - 807969713 + *")
    printSpacer()

    print "Formula : 1645109058 6002957117151700798 17371750452013475526 16844446134016717728 - * -"
    print "Answer :"
    print calcRPN("1645109058 6002957117151700798 17371750452013475526 16844446134016717728 - * -")
    printSpacer()

    print "Formula : 2214834052 697324037 3167190441 + 4024420067 3189403559 671301788 / * - +"
    print "Answer :"
    print calcRPN("2214834052 697324037 3167190441 + 4024420067 3189403559 671301788 / * - +")
    printSpacer()

    print "Formula : 2954071453 3950378094 1369641664 / 537596595 3844403077343837951 / * 3604400647 + 5523420129192838073 + +"
    print "Answer :"
    print calcRPN("2954071453 3950378094 1369641664 / 537596595 3844403077343837951 / * 3604400647 + 5523420129192838073 + +")
    printSpacer()

    
if __name__=="__main__":
    do_testing()
