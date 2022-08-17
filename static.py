class Mobile:
    fp = "test"

    @classmethod
    def show(cls):
        print(cls.fp)

realme = Mobile()
realme.show()
print(Mobile.fp)
Mobile.show()

strins = "python"
for i in strins:
    if i == "o":
        break
    print(i)
print("the loop is breaked")

i = 0
while 1:  
    print(i,'  ',end="")
    i=i+1
    if i == 10:  
        break;
print("came out of while loop")

n=2  
while 1:  
    i=1 
    while i<=10:  
        print(n, "x", i, "=", n*i)
        # print("%d X %d = %d\n"%(n,i,n*i));  
        i = i+1  
    choice = int(input("Do you want to continue printing the table, press 0 for no?"))  
    if choice == 0:  
        break 
    elif choice == 1:
        continue   
    n=n+1