class Library:

#Defining the Books
    def __init__(self,Books):
        self.Books = Books
#To list the Available Books in the Library
    def List_Books(self):
        print("Available Books : ")
        for Book in self.Books:
            print(Book)
#To Borrow the Book from the Library        
    def Borrow_Book(self,Borrow_Book):
        if Borrow_Book in self.Books:
            print("Get Your Book Now")
            self.Books.remove(Borrow_Book)
        else:
            print("The Book you entered is not Available")
#To Return the Book to the Library
    def Receive_Book(self,Receive_Book):
        print("You have Returned the Book")
        self.Books.append(Receive_Book)

#Available Books and the Meassages to Display to for the Operation
Books = ["A Tale of Two Cities", "The Little Prince", "Harry Potter and Philosopher's Stone", "And Then There Were None", "Dream of the Red Chamber", "The Hobbit"]
A = Library(Books)
Message = """
             1. Display Books
             2. Borrow Books
             3. Return Books
             Enter any integer other than these to Quit"""

#Creating a Loop for Infinite Execution until the Operation gets over
while True:
    print (Message)
    Choice = int(input("Enter Your Choice : "))
   
    if Choice == 1:
        A.List_Books()
    elif Choice == 2:
        Book = input("Enter the Book Name which you want to Borrow : ")
        A.Borrow_Book(Book)
    elif Choice == 3:
        Book= input("Enter the Book Name which you want to Return:")
        A.Receive_Book(Book)
    else:
        print("Thank you for visiting the Library... Come Again...")
        quit()