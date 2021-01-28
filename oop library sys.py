class Library:
    def __init__(self,list,name):
        self.booklist=list
        self.name=name
        self.lenddict={}

    def Displaybook(self):
        print(f"welcome to the {self.name} Library")
        for books in self.booklist:
            print(books)

    def Lendbook(self,user,book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("lender database has been updated....take your book!!!!")

        else:
            print(f"this book is already being used by {self.lenddict[book]}")

    def Addbook(self,book):
        self.booklist.append(book)
        print("book has been added to book list")

    def Returnbook(self,book):
        self.lenddict.pop(book)
if __name__ == '__main__':
    shree=Library(["netzwerk","maths",'wings of fire','harrypotter','into the wild','subtle art of not giving a f***'],"Shree's")

    while(True):
        print(f"welcome to {shree.name} library. please select the option:")
        print("1.Displaybook\n2.Lend book\n3.Addbook\n4.Returnbook.")
        I1=int(input("->"))
        if I1==1:
            shree.Displaybook()

        elif I1==2:
            book=input("enter the name of the book you want to lend : ")
            user=input("enter your name :")
            shree.Lendbook(user,book)

        elif I1==3:
            book=input("enter the name of the book you want to add in book list : ")
            shree.Addbook(book)
        elif I1==4:
            retu=input("enter the name of the book you are returning : ")
            shree.Returnbook(retu)
        else:
         print("choose correct option from above")

        print("press Q to exit or press C to continue")
        I2=""
        while (I2!="q" and I2!="c"):
            I2 = input("-> ")
            if I2=="q":
                exit()
            elif I2=="c":
                continue

