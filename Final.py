class Final:
    def payan(self,):
        exit()
    def menu(self):
        return """
1. Avrage
2. Histogarm
3. Fibonacci
4. Perimeter and area
5. calculator
6. anagram
7. Exercise 17
8. ascii code and character
9. lowercase to uppercase and Conversely
10. encode and decode a string
-----------------"""

    def p1(self):
        x = input("enter x: ").lower()
        if x == "end":
            exit()
        y = input("enter y: ").lower()
        if "end" == y:
            exit()

        try:
            x = int(x)
            y = int(y)

            if x > 10:
                raise IOError("Freeze")

            print(x, y)
        except IOError as e:
            print(e)
            global error
            error = True

    def a_1(self,):
        try:
            n=input("please Enter The Number of student: ")
            if n.lower()=="end":
                exit()
            else:
                n=int(n)
            m=2
            while n>0:
                n=n-1
                stud1=input("Please Enter the avrage: ")
                if stud1.lower()=="end":
                    exit()
                else:
                    stud1=float(stud1)
                if m>0:
                    m=m-1
                    one=stud1
                if one>stud1:
                    if two<stud1:
                        two=stud1
                if one<stud1:
                    one=stud1
                    two=one
                while n>0:
                    n=n-1
                    stud2=input("Please Enter the avrage: ")
                    if stud2.lower()=="end":
                        exit()
                    else:
                        stud2=float(stud2)
                    if m>0:
                        m=m-1
                        if stud1>stud2:
                            one=stud1
                            two=stud2
                        else:
                            one=stud2
                            two=stud1
                    if one>stud2:
                        if two<stud2:
                            two=stud2
                    elif one<stud2:
                        two=one
                        one=stud2
            print(two)
            end=input("Do you want to continue to calculate the average ?\n1) continue\n2) Return to menu\n")
            if end=="1":
                self.a_1()
            elif end=="2":
                self.menu()
            elif end.lower()=="end":
                exit()
            else:
                while True:
                    print("\nPlease select a number between 1 and 2")
                    end=input("\n1) continue\n2) Return to menu\n")
                    if end=="1":
                        self.a_1()
                        break
                    elif end=="2":
                        self.menu()
                        break
                    elif end.lower()=="end":
                        exit()
        except Exception as e:
            print("\nPlease Enter a correct number\n")
            self.a_1()

    def his(self,):
        n =[9  ,8  ,7  ,6  ,5  ,4  ,3  ,2  ,1  ,
            2  ,2  ,3  ,4  ,5  ,6  ,7  ,8  ,9  ,
            9  ,8  ,7  ,6  ,5  ,4  ,3  ,2  ,1  ,
            1  ,2  ,3  ,4  ,5  ,6  ,7  ,8  ,9  ,
            10 ,11 ,12 ,13 ,14 ,15 ,16 ,17 ,18 ,19  ]
        try:
            for a in n :
                if a=="end":
                    exit()
                print(f"{a}",end="")
                c=""
                while a>0:
                    c=c+"+"
                    a=a-1
                    if a==0:
                        print(c)
                    if "end"==a:
                        exit()
            end=input("Do you want to continue the program ?\n1) continue\n2) Return to menu\n")
            if end=="1":
                self.his()
            elif end=="2":
                self.menu()
            elif end.lower()=="end":
                exit()
            else:
                while True:
                    print("\nPlease select a number between 1 and 2")
                    end=input("\n1) continue\n2) Return to menu\n")
                    if end=="1":
                        self.his()
                        break
                    elif end=="2":
                        self.menu()
                        break
                    elif end.lower()=="end":
                            exit()
        except Exception as e:
            print(f"\nPlease change {a} to the number in your list")
            end=input("Do you want to continue the program ?\n1) continue\n2) Return to menu\n")
            if end=="1":
                self.his()
            elif end=="2":
                self.menu()
            elif end.lower()=="end":
                    exit()
            else:
                while True:
                    print("\nPlease select a number between 1 and 2")
                    end=input("\n1) continue\n2) Return to menu\n")
                    if end=="1":
                        self.his()
                        break
                    elif end=="2":
                        self.menu()
                        break
                    elif end.lower()=="end":
                        exit()

    def fibo(self,):
        n= input("Enter a Fibo Number: ").lower()
        if n=="end":
            exit()
        try:
            n= int(n)
            a=0
            b=1
            c=1
            while c<n:
                print(a,b,c,sep=',',end=',')
                while c<=n:
                    a=b
                    b=c
                    c=a+b
                    if c<n:
                        print(c,sep=',',end=',')
                    elif c==n:
                        print(c)
            end=input("Do you want to continue the Fibonacci program ?\n1) continue\n2) Return to menu\n")
            if end=="1":
                self.fibo()
            elif end=="2":
                self.menu()
            elif end.lower()=="end":
                exit()
            else:
                while True:
                    print("\nPlease select a number between 1 and 2")
                    end=input("\n1) continue\n2) Return to menu\n")
                    if end=="1":
                        self.fibo()
                        break
                    elif end=="2":
                        self.menu()
                        break
                    elif end.lower()=="end":
                        exit()
        except:
            print("\nPlease Enter a number\n")
            self.fibo()

    def shap(self,):
        a=input("Enter the name of a shape: ").lower()
        if a=="end":
            exit()
        try:
            name=["circle","square","rectangle"]
            if a not in name:
                return  self.shap()
            if a=="circle":
                r=input("Enter the radius of the circle : ")
                if r.lower()=="end":
                    exit()
                else:
                    r=float(r)
                perimeter=r*2*3.14
                area=3.14*r*r
                print(f"perimeter of the circle :{perimeter}")
                print(f"Area of ​​circle : {area}")
            if a=="square":
                s=input("Enter the side of the square : ")
                if s.lower()=="end":
                    exit()
                else:
                    s=float(s)
                perimeter=s*4
                area=s**2
                print(f"perimeter of the square :{perimeter}")
                print(f"Area of ​​square : {area}")
            if a=="rectangle":
                l=input("Enter the length of the rectangle : ")
                if l.lower()=="end":
                    exit()
                else:
                    l=float(l)
                w=input("Enter the width of the rectangle : ")
                if w.lower()=="end":
                    exit()
                else:
                    w=float(w)
                perimeter=(l+w)*2
                area=l*w
                print(f"perimeter of the rectangle :{perimeter}")
                print(f"Area of ​​rectangle : {area}")
            end=input("Do you want to continue the calculation program ?\n1) continue\n2) Return to menu\n")
            if end=="1":
                self.shap()
            elif end=="2":
                self.menu()
            elif end.lower()=="end":
                exit()
            else:
                while True:
                    print("\nPlease select a number between 1 and 2")
                    end=input("\n1) continue\n2) Return to menu\n")
                    if end=="1":
                        self.shap()
                        break
                    elif end=="2":
                        self.menu()
                        break
                    elif end.lower()=="end":
                        exit()
        except Exception as e:
            print("\nPlease Enter a correct input\n")
            self.shap()

    def calculator(self,):
        try:
            a=input("Enter a number: ")
            if a.lower()=="end":
                exit()
            else:
                a=float(a)
            c=input("Enter a math symbol: ")
            if c.lower()=="end":
                exit()
            else:
                c=c
            symbol=["+","-","*","/"]
            d=1
            while d>0:
                if c not in symbol:
                    c=input("Enter a math symbol: ")
                    continue
                else:
                    b=input("Enter a number: ")
                    if b.lower()=="end":
                        exit()
                    else:
                        b=float(b)
                    if c=="+":
                        sum=a+b
                        print(f"{a}{c}{b}={sum}")
                    if c=="-":
                        sub=a-b
                        print(f"{a}{c}{b}={sub}")
                    if c=="*":
                        multi=a*b
                        print(f"{a}{c}{b}={multi}")
                    if c=="/":
                        Division=a//b
                        print(f"{a}{c}{b}={Division}")
                break
            end=input("Do you want to continue the calculator program ?\n1) continue\n2) Return to menu\n")
            if end=="1":
                self.calculator()
            elif end=="2":
                self.menu()
            elif end.lower()=="end":
                exit()
            else:
                while True:
                    print("\nPlease select a number between 1 and 2")
                    end=input("\n1) continue\n2) Return to menu\n")
                    if end=="1":
                        self.calculator()
                        break
                    elif end=="2":
                        self.menu()
                        break
                    elif end.lower()=="end":
                        exit()
        except Exception as e:
            print("\nPlease Enter A number \n")
            self.calculator()

    def anagram(self,):
        x=input("Please Enter your word : ")
        if x.lower()=="end":
            exit()
        try:
            x=x
            if x[: :-1]==x[:]:
                print(x)
            end=input("Do you want to continue the Anagram program ?\n1) continue\n2) Return to menu\n")
            if end=="1":
                self.anagram()
            elif end=="2":
                self.menu()
            elif end.lower()=="end":
                exit()
            else:
                while True:
                    print("\nPlease select a number between 1 and 2")
                    end=input("\n1) continue\n2) Return to menu\n")
                    if end=="1":
                        self.anagram()
                        break
                    elif end=="2":
                        self.menu()
                        break
                    elif end.lower()=="end":
                        exit()
        except Exception as e:
            self.anagram()

    def kwrags(self,):
        a={"ord":"asdfgetrwqyuioplkjhn","chr":"65 66 67 68 69 70 71 72 73 74"}
        if a["ord"].lower()=="end" or a["chr"].lower()=="end":
            exit()
        try:
            a=a
            o=""
            c=""
            if "ord" in a :
                for i in a["ord"]:
                    o=o+i
                    if "end" in o.lower():
                        exit()
                    else:
                        print(ord(i),end=" ")
            if "chr" in a :
                print("")
                chr_crew=a["chr"].split()
                for j in chr_crew:
                    c=c+j
                    if "end" in j.lower():
                        exit()
                    else:
                        j=int(j)
                        print(chr(j),end="")
                print("")
            end=input("Do you want to continue the kwargs program ?\n1) continue\n2) Return to menu\n")
            if end=="1":
                self.kwrags()
            elif end=="2":
                self.menu()
            elif end.lower()=="end":
                exit()
            else:
                while True:
                    print("\nPlease select a number between 1 and 2")
                    end=input("\n1) continue\n2) Return to menu\n")
                    if end=="1":
                        self.kwrags()
                        break
                    elif end=="2":
                        self.menu()
                        break
                    elif end.lower()=="end":
                        exit()
        except Exception as e:
            print('\n\nPlease change the key values\n')
            end=input("Do you want to continue to the change key value ?\n1) continue\n2) Return to menu\n")
            if end=="1":
                self.kwrags()
            elif end=="2":
                self.menu()
            elif end.lower()=="end":
                exit()
            else:
                while True:
                    print("\nPlease select a number between 1 and 2")
                    end=input("\n1) continue\n2) Return to menu\n")
                    if end=="1":
                        self.kwrags()
                        break
                    elif end=="2":
                        self.menu()
                        break
                    elif end.lower()=="end":
                        exit()

    def f_co(self,):
        """تابع پدر"""
        a=input("Enter your sentence: ")
        if a.lower()=="end":
            exit()
        try:
            def my_ord(y):
                """تابع فرزند برای کد اسکی کاراکتر"""
                print(f"ascii code {y} :",ord(y),sep=" ")
            def my_chr(z):
                """تابع فرزند برای کاراکتر کد اسکی"""
                print(f"character {z}  : {chr(z)}",sep=" ")
            a=a
            chr1=0
            ord1=0
            num=""
            c=-1
            l=len(a)
            for i in a:
                c=c+1
                if c<l-2:
                    if ord(i) in range(49,58):
                        if  ord(a[c+1]) and ord(a[c+2]) or ord(a[c+1]) in range(49,58):
                            num=num+i
                            if int(num)<=99 and ord(a[c+1]) not in range(49,58):
                                ord1=ord1+1
                                my_chr(int(num))
                                num=""
                            elif int(num)>255:
                                num=num.rstrip(i)
                                ord1=ord1+1
                                my_chr(int(num))
                                num=i
                            elif int(num)>=100 and int(num)<=255:
                                ord1=ord1+1
                                my_chr(int(num))
                                num=""
                        else:
                            num=num+i
                            ord1=ord1+1
                            my_chr(int(num))
                            num=""
                    else:
                        chr1=chr1+1
                        my_ord(i)
                if c>=l-2 and c<l-1:
                    if ord(i) in range(49,58):
                        if ord(a[c+1]) in range(49,58):
                            num=num+i
                            if int(num)<=99 and ord(a[c+1]) not in range(49,58):
                                ord1=ord1+1
                                my_chr(int(num))
                                num=""
                            elif int(num)>255:
                                num=num.rstrip(i)
                                ord1=ord1+1
                                my_chr(int(num))
                                num=i
                            elif int(num)>=100 and int(num)<=255:
                                ord1=ord1+1
                                my_chr(int(num))
                                num=""
                        else:
                            num=num+i
                            ord1=ord1+1
                            my_chr(int(num))
                            num=""
                    else:
                        chr1=chr1+1
                        my_ord(i)
                if c==l-1:
                    if ord(i) in range(49,58):
                        num=num+i
                        if int(num)<=99 :
                            ord1=ord1+1
                            my_chr(int(num))
                            num=""
                        elif int(num)>255:
                            num=num.rstrip(i)
                            ord1=ord1+1
                            my_chr(int(num))
                            my_chr(int(i))
                        elif int(num)>=100 and int(num)<=255:
                            ord1=ord1+1
                            my_chr(int(num))
                            num=""
                        else:
                            num=num+i
                            ord1=ord1+1
                            my_chr(int(num))
                            num=""
                    else:
                        chr1=chr1+1
                        my_ord(i)
            my_chr(ord1)
            my_chr(chr1)
            end=input("Do you want to continue the Ord and Chr program ?\n1) continue\n2) Return to menu\n")
            if end=="1":
                self.f_co()
            elif end=="2":
                self.menu()
            elif end.lower()=="end":
                exit()
            else:
                while True:
                    print("\nPlease select a number between 1 and 2")
                    end=input("\n1) continue\n2) Return to menu\n")
                    if end=="1":
                        self.f_co()
                        break
                    elif end=="2":
                        self.menu()
                        break
                    elif end.lower()=="end":
                        exit()
        except:
            print("\n\nplease Enter a correct string\n")
            self.f_co()

    def small(self,):
        a= input("Enter your sentence : ")
        if a.lower()=="end":
            exit()
        try:
            a=a
            for i in a :
                if ord(i) in range(65,91):
                    char=ord(i)+32
                    print(chr(char),end="")
                if ord(i) in range(97,123):
                    char1=ord(i)-32
                    print(chr(char1),end="")
                else:
                    if ord(i) not in range(65,123) :
                        print(i,end="")
            print("")
            end=input("Do you want to continue the small_capital program ?\n1) continue\n2) Return to menu\n")
            if end=="1":
                self.small()
            elif end=="2":
                self.menu()
            elif end.lower()=="end":
                exit()
            else:
                while True:
                    print("\nPlease select a number between 1 and 2")
                    end=input("\n1) continue\n2) Return to menu\n")
                    if end=="1":
                        self.small()
                        break
                    elif end=="2":
                        self.menu()
                        break
                    elif end.lower()=="end":
                        exit()
        except:
            print("\n\nplease Enter correct string\n")
            self.small()

    def encode(self,):
        try:
            name=input("Enter your name : ")
            if name.lower()=="end":
                exit()
            code=["encode","decode"]
            name=name
            while True:
                coding=input("Enter your coding format : ").lower()
                if coding=="end":
                    exit()
                if coding not in code:
                    continue
                else:
                    break
            if coding=="encode":
                for a in name:
                    i=ord(a)+1
                    print(chr(i),end="")
                print("")
            if coding=="decode":
                for b in name:
                    j=ord(b)-1
                    print(chr(j),end="")
                print("")
            end=input("Do you want to continue the encode_decode program ?\n1) continue\n2) Return to menu\n")
            if end=="1":
                self.encode()
            elif end=="2":
                self.menu()
            elif end.lower()=="end":
                exit()
            else:
                while True:
                    print("\nPlease select a number between 1 and 2")
                    end=input("\n1) continue\n2) Return to menu\n")
                    if end=="1":
                        self.encode()
                        break
                    elif end=="2":
                        self.menu()
                        break
                    elif end.lower()=="end":
                        exit()
        except Exception as e:
            print("\n\nPlease be careful when entering values\n")
            self.encode()

selector = "0"
error = False

f = Final()

while True:
    try:
        if not error:
            print(f.menu())
            selector = input("choose number of programs: ").lower()
            if selector == "end":
                exit()

        #if selector == "1":
            #error = False
            #f.p1()
        if selector == "1":
            error = False
            f.a_1()
        elif selector == "2":
            error = False
            f.his()
        elif selector == "3":
            error = False
            f.fibo()
        elif selector == "4":
            error = False
            f.shap()
        elif selector == "5":
            error = False
            f.calculator()
        elif selector == "6":
            error = False
            f.anagram()
        elif selector == "7":
            error = False
            f.kwrags()
        elif selector == "8":
            error = False
            f.f_co()
        elif selector == "9":
            error = False
            f.small()
        elif selector == "10":
            error = False
            f.encode()
        # ...
    except Exception as e:
        print(e)
