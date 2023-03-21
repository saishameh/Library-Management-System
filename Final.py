#dictionary containing login and passwords 
Librarian={'Reshma':'1234','Swetha':'4321'}

#Details of all the books in the library 
Rack_Book=[["Scary Stories To Tell In The Dark","Alvin Schwartz"],
["Night Of The Living Dummy", "R.L.Stine"],
["Miss Peregrine's Home For Peculiar Children","Ransom Riggs"],
["World War Z", "Max Brooks"],
["The Amityville Horror", "Jay Anson"],
["Twilight", "Stephenie Meyer"],
["A Mosnter Calls", "Patrick Ness"], 
["Roald Dahl Boy", "Roald Dahl"],
["Encylopedia Of Space", "Heather Couper"],
["Oxford Dictionary", "John Simpson"],
["General Knowledge 2020", "Manohar Pandey"],
["A Game Of Thrones","George R. R. Martin"],
["The Fellowship Of The Ring"," J. R. R. Tolkien"],
["The Lion, the Witch and the Wardrobe","C. S. Lewis"],
["The Colour Of Magic","Terry Pratchett"],
["Assassin’s Apprentice"," Robin Hobb"],
["The Lies Of Locke Lamora", "Scott Lynch"],
["The Name Of The Wind"," Patrick Rothfuss"],
["Dragonflight","Anne McCaffrey"],
["To Kill A Mockingbird","Harper Lee"],
["The Great Gatsby", "F. Scott Fitzgerald"],
["In Cold Blood","Truman Capote"],
["Wide Sargasso Sea","Jean Rhys"],
["Brave New World"," Aldous Huxley"],
["Nimona","Noelle Stevenson"],
["This One Summer","Mariko Tamaki"],
["Blankets","Craig Thompson"],
["American Born Chinese","Gene Luen Yang"],
["The Silence","Kendra Elliot"],
["The Silent Patient","Alex Michaelides"],
["One By One","Ruth Ware"],
["The Last Sister","Kendra Elliot"],
["The Teen model mystery","Carolyn Kenne"],
["The Arsonist","Stephanie Oakes"],
["My Own Worst Frenemy","Kimberly Reid"],
["Overturned","Lamar Giles"],
["Pretty Girl-13","Liz Coley"],
["Grown","Tiffany D.J"],
["And Then There Were None","Agatha Christie"],
["Gone Girl","Gillian Flynn"],
["Tinkle","Luis Fernandes"],
["Pride And Prejudice","Jane Austen"],
["Welcome To The Horrorland", "R.L.Stine"],
["The Diary Of A Young Girl", "Anne Frank"],
["Guinness World Records 2020", "Craig Glenday"],
["I'm Malala", "Malala Yousafzai"],
["Diary of A Wimpy Kid","Jeff Kinney"],
["Dork Diaries","Rachel Renée Russell"],
["The Girl On The Train","Paula Hawkins"]]

#details of all the students
student={"Harshida":1,"Rida":2,"Tanya":3,"Tanisha":4,"Shaheer":5,
         "Harris":6,"Yash":7,"Ajey":8,"Shlok":9,"Lakshya":10,
         'Rahul':11,'Raj':12,'Sarah':13,'Sameera':14,"Kay":15,
         "Nikki":16,"Taki":17,"Sunghoon":18,"Jay":19,"Jake":20}

#list of book details of issued books
Dispatch_Book=[["Gone Girl","Rahul"],
["Tinkle","Rahul"],
["Pride And Prejudice","Ajey"],
["Welcome To The Horrorland", "Shlok"],
["The Diary Of A Young Girl", "Jake"],
["Guinness World Records 2020","Jake"],
["I'm Malala","Jay"],
["Diary Of A Wimpy Kid","Taki"],
["Dork Diaries","Sameera"],
["The Girl On The Train","Sameera"]]

#functions for the login menu
def Change_password(user):
    user=user.capitalize()
    if user not in Librarian:
        print("Invalid user")
        print()
    else:
        passwrd=input("Enter the new password: ")
        Librarian[user]=passwrd
        print("PASSWORD successfully changed!")
        print()

def Create_login(login):
    login=login.capitalize()
    if login not in Librarian:
        newpassword=input('Enter the password: ')
        Librarian[login]=newpassword
        print("Successfully added new Login Details!")
        print()
    else:
        print("User already exits.")
        print()
#functions for book menu
def Add_books(bookname):
    bookname=bookname.title()
    for x in Rack_Book:
        if x[0]==bookname:
            print("The book already exists")
            print()
            break
    else:
        authorname=input("Please enter author name: ")
        authorname=authorname.title()
        item=[bookname,authorname]
        Rack_Book.append(item)
        print("The book has been successfully added!")
        print()   
        
def Delete_books(name2):
    name2=name2.title()
    for x in Rack_Book:
        if name2 in x:
            Rack_Book.remove(x)
            print("The book has been succesfully deleted")
            print()
            break
    else:
        print("This book does not exist")
        print()
            
def Search_books(name3):
    name3=name3.title()
    for x in Rack_Book:
        if name3 in x:
            print("This book exists")
            print("Author:",x[1])
            print()
            break
    else:
        print("This book does not exist")
        print()
        
def return_books(name):
    name=name.title()
    for x in Dispatch_Book:
        if name in x:
            Dispatch_Book.remove(x)
            Rack_Book.append(x)
            print("Returned Successfully: ",name)
            print()
            break
    else:
        print("This book was not issued")
        print()
        
#functions for student detail menu
def Add_student(studentname):
    studentname=studentname.title()
    if studentname not in student:
        rollno=int(input("Enter the new roll no: "))
        if rollno not in student.values():
            student[studentname]=rollno
            print("Successfully  added with details",[studentname,rollno])
            print()
        else:
            print("This roll no is already taken")
            print()
    else:
        print("Student already available with details")
        print()
        
def Delete_student(studentname):
    studentname=studentname.title()
    if studentname in student:
        rollno=int(input("Enter the roll no. of the student: "))
        del student[studentname]
        print("Successfully deleted student details",[studentname,rollno])
        print()
    else:
        print("No students available with name",studentname)
        print()
        
def Search_student(studentname):
    studentname=studentname.title()
    search_key=studentname
    if search_key in student.keys():
        print("The student exists")
        print("Roll no:",student[studentname])
        print()
    else:
        print("The student does not exist.")
        print("To add details of this student please choose option1")
        print()
        
#functions for issue menu
def issue_book(bookname):
    bookname=bookname.title()
    choice=None 
    while choice!=0:
        for x in Rack_Book:
            if bookname in x:
                for i in Dispatch_Book:
                    if bookname in i:
                        print("This book has already been issued")
                        choice=0
                        print()
                        break
                else:    
                    student=input('Enter the name of the student: ')
                    student=student.title()
                    issuedbook1=[bookname,student]
                    Dispatch_Book.append(issuedbook1)
                    print("The book has been succesfully issued")  
                    choice=0
                    print()
                    break
    
def search_user_issue_details(bookname):
    bookname=bookname.title()
    for x in Dispatch_Book:
        if bookname in x:
            name=x[1]
            print("Name: ",name)
            print("Roll no: ",student[name])
            print()
            break
    else:
        print("This book was not issued")                              
        print()
 
chk=None
count=None
while chk!=0:
    userlib=input("Enter your name: ")
    userlib=userlib.capitalize()
    i=1
    if userlib not in Librarian:
        print("This log in name does not exist")
        print()
        chk=0
    else:
        while count!=0:
            passwrdlib=input("Enter your login pin: ")
            if Librarian[userlib]!=passwrdlib: 
                print("Access Denied")
                print("PIN Entered wrong")
                print("You have more",(3-i),"more attempts")
                i+=1
                if i==4:
                    print("Failed login within 3 attempts")
                    print('Incorrect password')
                    print()
                    chk=0
                    count=0       
            else:
                print("Access granted!")
                print()
                while True:
                    print("Welcome to the Library!")
                    print()
                    print("*********")
                    print('MAIN MENU')
                    print("*********")
                    print()
                    print("SELECT YOUR OPTION...")
                    print('1.LOGIN MENU')
                    print('2.BOOK MENU')
                    print('3.STUDENT MENU')
                    print('4.ISSUE MENU')
                    print('5.EXIT')
    
                    ch1=int(input("Please enter your option: "))
                    print()
                    if ch1==1:
                        while True:
                            print("**********")
                            print("LOGIN MENU")
                            print("**********")
                            print()
                            print("SELECT YOUR OPTION...")
                            print("1.CHANGE PASSWORD")
                            print("2.CREATE NEW LOGIN AND PASSWORD")
                            print("3.DISPLAY LOGIN DETAILS")
                            print("4.EXIT")
                            
                            ch2=int(input("Please enter your option: "))
                            print()
                            if ch2==1:
                                user=input("Enter the login: ")
                                Change_password(user)
                                
                            elif ch2==2:
                                newlogin=input('Enter the login ID: ')
                                Create_login(newlogin)
    
                            elif ch2==3:
                                for item in Librarian:
                                    print(item,":",Librarian[item])
                                    
                            elif ch2==4:
                                print("Exited successfully!")
                                print()
                                break
                            
                            else:
                                print("Wrong choice")
                                print()
                
                    elif ch1==2:
                        while True:
                            print("*********")
                            print("BOOK MENU")
                            print("*********")
                            print()
                            print("SELECT YOUR OPTION...")
                            print('1.Add books')
                            print('2.Delete books')
                            print('3.Search books')
                            print('4.Display available books')
                            print('5.Return book')
                            print('6.Exit')
        
                            ch3=int(input('Enter the choice: '))
                            print()
                            if ch3==1:
                                name1=input("Please enter book name: ")
                                Add_books(name1)
                
                            elif ch3==2:
                                name2=input("Please enter book name: ")
                                Delete_books(name2)
                
                            elif ch3==3:
                                name3=input("Please enter book name: ")
                                Search_books(name3)
                
                            elif ch3==4:
                                for x in (Rack_Book):
                                    for y in (Dispatch_Book):
                                        if x[0] in y:
                                            continue
                                    else:
                                        print("Book:",x[0])
                                        print ("Author:",x[1])
                                        print()
                
                            elif ch3==5:
                                name4=input('Enter the name of the book: ')
                                return_books(name4)
                    
                            elif ch3==6:
                                print("Exited successfully!")
                                print()
                                break
            
                            else: 
                                print('Wrong choice')
                                print()
    
                    elif ch1==3:
                        while True:
                            print("***********")
                            print("STUDENT MENU")
                            print("***********")
                            print()
                            print("SELECT YOUR OPTION...")
                            print('1.Add student ')
                            print('2.Delete student ')
                            print('3.Search student ')
                            print('4.Display student ')
                            print("5.Modify student details")
                            print('6.Exit')
            
                            ch4=int(input('Enter the choice: '))
                            print()
                            if ch4==1:
                                studentname1=input('Enter the name of the new student: ')
                                Add_student(studentname1)

                            elif ch4==2:
                                studentname2=input("Enter the name of the student that has to be deleted: ")	
                                Delete_student(studentname2)
                    
                            elif ch4==3:
                                studentname3=input("Enter the name of the student that has to be searched: ")	
                                Search_student(studentname3)

                            elif ch4==4:
                                for key in student:
                                    print("Name: ",key)
                                    print("Rollno: ",student[key])
                                    print()

                            elif ch4==5:
                                while True:
                                    print("**************************")
                                    print("MODIFY STUDENT DETAIL MENU")
                                    print("**************************")
                                    print()
                                    print("SELECT YOUR OPTION...")
                                    print("1.Modify Name of student")
                                    print("2.Modify Roll number of student")
                                    print("3.EXIT")
                        
                                    ch5=int(input("Enter your choice: "))
                                    print()
                                    if ch5==1:
                                        print("Name of the student cannot be modified")  
                                        print("To delete old name please choose option2")
                                        print("To add a new student name please choose option1")
                                        print()
                                        break
                    
                                    elif ch5==2:
                                        studentname4=input("Enter the name of the student whose roll number is to be modified: ")
                                        rollno4=int(input("Enter new roll number: "))
                                        studentname4=studentname4.title()
                                        if student.get(studentname4)==rollno4:
                                            print("Same rollno has been entered")
                                            print()
                            
                                        else:
                                            student[studentname4]=rollno4
                                            print("Successfully modified details",[studentname4,rollno4])	
                                            print()
                                            break
                        
                                    elif ch5==3:
                                        print("Exited successfully")
                                        break
                                        print()
                    
                                    else:
                                        print('Wrong choice')
                                        print()
                    
                            elif ch4==6:
                                print("Exited successfully!")
                                print()
                                break
            
                            else: 
                                print('Wrong choice')
                                print()

                    elif ch1==4:                
                        while True:
                            print("**********")
                            print("ISSUE MENU")
                            print("**********")
                            print()
                            print("SELECT YOUR OPTION...")
                            print('1.Issue book')
                            print('2.Search user issue details')
                            print('3.Exit')
            
                            ch6=int(input('Enter the choice: '))
                            print()
                            if ch6==1:
                                bookname5=input('Enter the name of the book to be issued: ')
                                issue_book(bookname5)
                   
                            elif ch6==2:
                                bookname6=input('Enter the issued book name: ')
                                search_user_issue_details(bookname6)
                                           
                            elif ch6==3:
                                print("Exited successfully!")
                                print()
                                break
            
                            else: 
                                print('Wrong choice')
                                print()
     
                    elif ch1==5:
                        print("Exited successfully!")
                        print()
                        chk=0
                        count=0
                        break
                    
                    else:
                        print("Wrong choice")
                        print()