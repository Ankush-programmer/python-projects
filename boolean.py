#defining functions
def cls():
    import os
    os.system("cls")

 #function:
while 1:
    print("How Many Row You Want To Print")
    lines= int(input())
    cls()
    print("Type 1 Or 0")
    true_false = int(input())
    cls()
    if true_false == 1:
        for i in range(1,lines+1):
            for j in range(1,i+1):
                print("*",end=" ")
            print()
    elif true_false == 0:
        for i in range(lines,0,-1):
            for j in range(1,i+1):
                print("*", end="")
            print()
    y_n=input("Do you want to try again?(y/n)\n")
    if y_n=="y":
        cls()
        continue

    else:
        break
#     end
#finish
