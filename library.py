import mysql.connector as ms
mc = ms.connect(host='localhost', user='root',
                password='radhika', database='library')
cr = mc.cursor()
chk = None
count = None
ch = None
while chk != 0:
    userlib = input("Enter your name: ")
    userlib = userlib.capitalize()
    i = 1
    cr.execute('select * from log_in')
    data1 = cr.fetchall()
    while ch != 0:
        for details in data1:
            if userlib in details:
                while count != 0:
                    passwrdlib = int(input("Enter your login pin: "))
                    if details[2] != passwrdlib:
                        print("Access Denied")
                        print("PIN Entered wrong")
                        print("You have more", (3-i), "more attempts")
                        i += 1
                        if i == 4:
                            print("Failed login within 3 attempts")
                            print('Incorrect password')
                            print()
                            chk = 0
                            count = 0
                            ch = 0

                    else:
                        print("Access granted!")
                        print()
                        print("Welcome to the Library!")
                        print()
                        cr.execute('select * from books')
                        data2 = cr.fetchall()
                        cr.execute('select * from student')
                        data3 = cr.fetchall()

                        while True:
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

                            ch1 = int(input("Please enter your option: "))
                            print()
                            if ch1 == 1:
                                while True:
                                    print("**********")
                                    print("LOGIN MENU")
                                    print("**********")
                                    print()
                                    print("SELECT YOUR OPTION...")
                                    print("1.CHANGE PASSWORD")
                                    print("2.CREATE NEW LOGIN AND PASSWORD")
                                    print("3.DISPLAY LOGIN DETAILS")
                                    print("4.DELETE LOGIN DETAILS")
                                    print("5.EXIT")

                                    ch2 = int(
                                        input("Please enter your option: "))
                                    print()
                                    if ch2 == 1:
                                        # CHANGE PASSWORD
                                        c1 = None
                                        user = input("Enter the login: ")
                                        user = user.capitalize()
                                        while c1 != 0:
                                            for details in data1:
                                                if user in details:
                                                    passwrd = input(
                                                        "Enter the new password: ")
                                                    update = "update log_in set PASSWORD='"+passwrd +"' where NAME= '"+user+"'"  
                                                    cr.execute(update)
                                                    mc.commit()
                                                    print("PASSWORD successfully changed!")
                                                    c1=0
                                                    print()
                                            if c1!=0:
                                                print("Invalid user")
                                                print()
                                                
                                    elif ch2==2:
                                        #CREATE  NEW LOGIN AND PASSWORD 
                                        newlogin=input('Enter the login ID: ')
                                        newlogin=newlogin.capitalize()
                                        c2=None
                                        while c2!=0:
                                            for details in data1:
                                                if newlogin in details:
                                                    print("User already exits.")
                                                    c2=0
                                                    print()
                                                    break
                                            else:
                                                newpassword=input('Enter the password: ')
                                                sno=str(len(data1)+1)
                                                values="insert into log_in values ('"+sno+"' , '"+newlogin+"','"+newpassword+"')"
                                                cr.execute(values)
                                                mc.commit()
                                                print("Successfully added new Login Details!")
                                                c2=0
                                                print()
                                                
                                    elif ch2==3:
                                        #DISPLAY LOGIN DETAILS
                                        print('SNO','  NAME','  PASSWORD')
                                        for details in data1:
                                            for c in details:
                                                print(c,end='  ')
                                            print()
                                        print()
                                    
                                    elif ch2==4:
                                        #DELETE LOGIN DETAILS
                                        newlogin1=input("Enter the name of the login that has to be deleted: ")                    
                                        newlogin1=newlogin1.title()
                                        c2=None
                                        while c2!=0:
                                            for details in data1:
                                                    if newlogin1 in details:
                                                        delete="delete from log_in where NAME= '"+newlogin1+"' "
                                                        cr.execute(delete)
                                                        mc.commit()
                                                        print("Successfully deleted login details")
                                                        c2=0
                                                        print()
                                                        break
                                            else:
                                                print("No login available with name",newlogin1)
                                                c2=0
                                                print()
                                        
                                        
                                    elif ch2==5:
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
                                        #ADD BOOKS
                                        c3=None
                                        bookname=input("Please enter book name: ")
                                        bookname=bookname.title()
                                        while c3!=0:
                                            for details in data2:
                                                    if bookname in details:
                                                        print("The book already exists")
                                                        c3=0
                                                        print()
                                                        break
                                            else:
                                                authorname=input("Please enter author name: ")
                                                authorname=authorname.title()
                                                bookno= str(len(data2)+1)
                                                newstatus="available"
                                                newbook="insert into books values ('"+bookno+"' , '"+bookname+"' ,                                                '"+authorname+"' , '"+newstatus+"')"
                                                cr.execute(newbook)
                                                mc.commit()
                                                print("The book has been successfully added!")
                                                c3=0
                                                print()
                                                
                                    elif ch3==2:
                                        #DELETE BOOKS
                                        name2=input("Please enter book name: ")
                                        name2=name2.title()
                                        c4=None
                                        while c4!=0:
                                            for details in data2:
                                                    if name2 in details:
                                                        delete="delete from books where B_NAME= '"+name2+"' "
                                                        cr.execute(delete)
                                                        mc.commit()
                                                        print("The book has been succesfully deleted")
                                                        c4=0
                                                        print()
                                                        break
                                            else:
                                                print("This book does not exist")
                                                c4=0
                                                print()
                                                
                                    elif ch3==3:
                                        #SEARCH BOOKS
                                        name3=input("Please enter book name: ")
                                        name3=name3.title()
                                        c5=None
                                        while c5!=0:
                                            for details in data2:
                                                    if name3 in details:
                                                        print("This book exists")
                                                        print("Author:",details[2])
                                                        print("The book is",details[3])
                                                        c5=0
                                                        print()
                                                        break
                                            else:
                                                print("This book does not exist")
                                                c5=0
                                                print()
                                                
                                    elif ch3==4:
                                        #DISPLAY AVAILABLE BOOKS
                                        available ="select B_NAME,B_AUTHOR from books where status='available' "
                                        cr.execute(available)
                                        list= cr.fetchall()
                                        for i in list:
                                            print("Name:",i[0])
                                            print("Author:",i[1])
                                            print()
                                    
                                    elif ch3==5:
                                        #RETURN BOOK
                                        name4=input('Enter the name of the book: ')
                                        name4=name4.title()
                                        c6=None
                                        while c6!=0:
                                            for details in data2:
                                                    if name4 in details:
                                                        if details[3]=='available':
                                                            print("This book was not issued")
                                                            c6=0
                                                            print()
                                                            break
                                                        else:
                                                            b_no= str(details[0])
                                                            status='available'
                                                            return_book1 ="update books set STATUS= '"+status+"' where                                                            B_NAME= '"+name4+"' "
                                                            return_book2 ="update student set IB_NO= NULL where                                                           IB_NO='"+b_no+"' "
                                                            cr.execute(return_book1)
                                                            cr.execute(return_book2)
                                                            mc.commit()
                                                            print("Returned Successfully: ",name4)
                                                            c6=0
                                                            print()
                                                            break
                                    
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
                                        #ADD STUDENT
                                        c4=None
                                        c5=None
                                        studentname1=input("Enter the name of the new student: ")
                                        studentname1=studentname1.title()
                                        while c4!=0:
                                            for details in data3:
                                                    if studentname1 in details:
                                                        print("Student already available with details")
                                                        c4=0
                                                        print()
                                                        break
                                            else:
                                                rollno=str(200+len(data3)+1)
                                                newstudent="insert into student values ('"+rollno+"' ,                                                '"+studentname1+", NULL)"
                                                cr.execute(newstudent)
                                                mc.commit()
                                                print("Successfully  added with details")
                                                c4=0
                                                print()
                                                
                                    elif ch4==2:
                                        #DELETE STUDENT
                                        studentname2=input("Enter the name of the student that has to be deleted: ")
                                        studentname2=studentname2.title()
                                        c5=None
                                        while c5!=0:
                                            for details in data3:
                                                    if studentname2 in details:
                                                        delete="delete from student where S_NAME= "+studentname2+"' "
                                                        cr.execute(delete)
                                                        mc.commit()
                                                        print("Successfully deleted student details")
                                                        c5=0
                                                        print()
                                                        break
                                            else:
                                                print("No students available with name",studentname2)
                                                c5=0
                                                print()
                                                
                                    elif ch4==3:
                                        #SEARCH STUDENT
                                        studentname3=input("Enter the name of the student that has to be searched: ")            
                                        studentname3=studentname3.title()
                                        c6=None
                                        while c6!=0:
                                            for details in data3:
                                                    if studentname3 in details:
                                                        print("The student exists")
                                                        print("Roll no:",details[0])
                                                        c6=0
                                                        print()
                                                        break
                                            else:
                                                print("The student does not exist.")
                                                print("To add details of this student please choose option1")
                                                c6=0
                                                print()
                                    
                                    elif ch4==4:
                                        #DISPLAY STUDENT
                                        print('ROLLNO',' S_NAME')
                                        for details in data3:
                                            print("Name: ",details[1])
                                            print("Rollno: ",details[0])
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
                                                studentname4=studentname4.title()
                                                c7=None
                                                while c7!=0:
                                                    for details in data3:
                                                        if studentname4 in details:
                                                            rollno4=input("Enter new roll number: ")
                                                            if str(details[0])==rollno4:
                                                                print("Same rollno has been entered")
                                                                c7=0
                                                                print()
                                                                break
                                                            else:    
                                                                update_s ="update student set ROLL_NO= '"+rollno4+"' where S_NAME= '"+studentname4+"' "	
                                                                cr.execute(update_s)
                                                                mc.commit()
                                                                print("Successfully modified details")	
                                                                print()
                                                                c7=0
                                                                break
                                                    else:
                                                        print("No students available with name",studentname4)
                                                        c7=0
                                                        print()
                                                        
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
                                        #ISSUE BOOK
                                        bookname5=input('Enter the name of the book: ')
                                        bookname5=bookname5.title()
                                        c8=None
                                        while c8!=0:
                                            for details in data2:
                                                    if bookname5 in details:
                                                        if details[3]=='issued':
                                                            print("This book has already been issued")
                                                            c8=0
                                                            print()
                                                            break
                                                        else:
                                                            student=input('Enter the name of the student: ')
                                                            student=student.title()
                                                            b_no= str(details[0])
                                                            status='issued'
                                                            issue_book1 ="update books set STATUS= "+status+" where B_NAME= "+bookname5+" " +issue_book2+"update student set IB_NO= '"+b_no+"' where S_NAME= "+student+"' "
                                                            cr.execute(issue_book1)
                                                            cr.execute(issue_book2)
                                                            mc.commit()
                                                            print("The book has been succesfully issued")
                                                            c8=0
                                                            print()
                                                            break
                                            else:
                                                print("This book does not exists")
                                                print()
                                                c8=0
                                    
                                    elif ch6==2:
                                         bookname6=input('Enter the issued book name: ')
                                         bookname6=bookname6.title()
                                         for details1 in data2:
                                             if bookname6 in details1:
                                                 if details1[3]=='available':
                                                     print("This book was not issued")                              
                                                     print()
                                                     break
                                                 else:
                                                     ibno=details1[0]
                                         else:            
                                             for details2 in data3:
                                                 if ibno in details2:
                                                     print("Name: ",details2[1])
                                                     print("Roll no: ",details2[0])
                                                     print()
                                                     break
                                    
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
                                mc.close()
                                chk=0
                                count=0
                                break
                            else:
                                print("Wrong choice")
                                print()            
        if count!=0:
            print("This log in name does not exist")
            print()
            chk=0
            ch=0
            break
