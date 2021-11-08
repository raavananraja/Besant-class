# simple calculator

def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

def mul(a,b):
    print(a*b)

def div(a,b):
    print(a/b)

print("""select the your choice
1.add
2.sub
3.mul
4.div
""")


choice = int(input("enter the choice value"))
a=int(input("enter the a vulue"))
b=int(input("enter the b value"))
if choice == 1:
        print("add value:"+add(a,b))

elif choice == 2:
        print("sub value:"+sub(a,b))
elif choice == 3:
        print("mul value:"+mul(a,b))
elif choice == 4:
        print("div value:" + div(a,b))
else:
        print("select the corrcet choice")

