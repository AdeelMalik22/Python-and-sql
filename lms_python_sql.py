import mysql.connector

class Library:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="subhan",
            password='Adeel@6Dec2024',
            database="Library"
        )
        self.cursor = self.db.cursor()
        
    def create_tables(self):
        book_table = "CREATE TABLE IF NOT EXISTS Book (ID INT NOT NULL PRIMARY KEY,  Title VARCHAR(50), Author_ID INT, ISBN INT NOT NULL, FOREIGN KEY (Author_ID) REFERENCES Author(ID))"
        student_table = "CREATE TABLE IF NOT EXISTS Student (ID INT NOT NULL PRIMARY KEY, Name VARCHAR(50), Status ENUM('Active', 'Inactive') DEFAULT 'Active')"
        author_table = "CREATE TABLE IF NOT EXISTS Author (ID INT NOT NULL PRIMARY KEY, Name VARCHAR(50))"
        order_table = "CREATE TABLE IF NOT EXISTS Orders( ID  INT NOT NULL PRIMARY KEY, Student_id INT NOT NULL, Book_id INT NOT NULL, Status VARCHAR(50), FOREIGN KEY(Student_id) REFERENCES Student(ID), FOREIGN KEY(Book_id) REFERENCES Book(ID))"
        
        self.cursor.execute(author_table)
        self.cursor.execute(book_table)
        self.cursor.execute(student_table)
        self.cursor.execute(order_table)
        
    def commit(self):
        self.db.commit()
   
    def add_book_prompt(self):
        ID = int(input("Enter the ID of Book: "))
        Title = str(input("Enter the Title of Book: "))
        Author_ID = int(input("Enter the ID of Author:"))
        ISBN = int(input("Enter ISBN Number: "))
        self.add_book(ID, Title, Author_ID, ISBN)
        self.commit()
        
    def add_book(self, ID, Title, Author_ID, ISBN):
        insert_data = "INSERT INTO Book(ID, Title, Author_ID, ISBN) VALUES (%s, %s, %s, %s)"
        values = (ID, Title, Author_ID, ISBN)
        self.cursor.execute(insert_data, values)
        
    def books_data(self):
        self.cursor.execute("SELECT * FROM Book")
        record = self.cursor.fetchall()
        print(len(record), "books are in library and here is the list:")
        print(record)
    
    def add_student(self, ID, Name, Status):
        insert_student = "INSERT INTO Student (ID, Name, Status) VALUES (%s, %s, %s)"
        values = (ID, Name, Status)
        self.cursor.execute(insert_student, values)
        self.commit()
        
    def update_student_prompt(self):
        ID = int(input("Enter the Student ID: "))
        Name = str(input("Enter the Student Name: "))
        Status = str(input("Enter the Status Active/inactive: "))
        self.add_student(ID, Name, Status)
    
    def student_data(self):
        self.cursor.execute("SELECT * FROM Student")
        record = self.cursor.fetchall()
        print(len(record), "students are active in the library, here is the list:")
        print(record)
    
    def add_author(self, ID, Name):
        insert_author = "INSERT INTO Author (ID, Name) VALUES (%s, %s)"
        values = (ID, Name)
        self.cursor.execute(insert_author, values)
        self.commit()
        
    def update_author_prompt(self):
        ID = int(input("Enter the Author ID: "))
        Name = str(input("Enter the Author's Name: "))
        self.add_author(ID, Name)
    
    def get_author(self, Author_ID):
        select_author = "SELECT Name FROM Author WHERE ID = %s"
        self.cursor.execute(select_author, (Author_ID,))
        author = self.cursor.fetchone()[0]
        print(f"Author is: {author}")
        
    def update_get_author(self):
        Author_ID = int(input("Enter Author ID to check Name of Author: "))
        self.get_author(Author_ID)
    
    def orders(self, ID, Student_id, Book_id, Status):
        insert_order = "INSERT INTO Orders (ID, Student_id, Book_id, Status) VALUES (%s, %s, %s, %s)"
        value = (ID, Student_id, Book_id, Status)
        self.cursor.execute(insert_order, value)
        self.commit()
    
    def update_order_prompt(self):
        ID = int(input("Enter Order ID: "))
        Student_id = int(input("Enter Student ID: "))
        Book_id = int(input("Enter Book ID: "))
        Status = str(input("Enter Status of order: "))
        self.orders(ID, Student_id, Book_id, Status)
    
    def get_order_details(self):
        sql = "SELECT Student.Name, Book.Title, Orders.Status \
               FROM Orders \
               LEFT JOIN Student ON Orders.Student_id = Student.ID \
               LEFT JOIN Book ON Orders.Book_id = Book.ID"
        self.cursor.execute(sql)
        records = self.cursor.fetchall()
        print(len(records), "Orders have been placed, here are the details:") 
        print(records)
    
   

class UpdatedLibrary(Library):
    
    def add_new_table(self):
        new_table = "CREATE TABLE IF NOT EXISTS Updates (ID INT NOT NULL PRIMARY KEY, Table_Name VARCHAR(50), Update_Type VARCHAR(50), Update_Data VARCHAR(100))"
        self.cursor.execute(new_table)
        self.commit()
        
    def update_student_data(self):
        ID = int(input("Enter the Student ID: "))
        Name = str(input("Enter the Student Name: "))
        Status = str(input("Enter the Status Active/inactive: "))
        update = "UPDATE Student SET Name=%s, Status=%s WHERE ID=%s"
        value = (Name, Status, ID)
        self.cursor.execute(update, value)
        self.commit()
        
    def delete_student(self):
     ID = int(input("Enter ID of a student to delete: "))
     delete_orders = "DELETE FROM Orders WHERE Student_id=%s"
     self.cursor.execute(delete_orders, (ID,))
     delete_student = "DELETE FROM Student WHERE ID=%s"
     self.cursor.execute(delete_student, (ID,))
     self.commit()

        
    def update_book_data(self):
        ID = int(input("Enter the ID of Book: "))
        Title = str(input("Enter the Title of Book: "))
        Author_ID = int(input("Enter New ID of Author:"))
        ISBN = int(input("Enter New ISBN Number: "))
        update = "UPDATE Book SET Title=%s, Author_ID=%s, ISBN=%s WHERE ID=%s"
        value = (Title, Author_ID, ISBN, ID)
        self.cursor.execute(update, value)
        self.commit()
        
    def delete_book(self):
     ID = int(input("Enter the ID of the book to delete: "))
     delete_orders = "DELETE FROM Orders WHERE Book_id=%s"
     self.cursor.execute(delete_orders, (ID,))
     delete_book = "DELETE FROM Book WHERE ID=%s"
     self.cursor.execute(delete_book, (ID,))
     self.commit()

        
    def update_author_data(self):
        Author_ID = int(input("Enter Author ID to change author name: "))
        Name = str(input("Enter New Author Name: "))
        update = "UPDATE Author SET Name=%s WHERE ID=%s"
        value = (Name, Author_ID)
        self.cursor.execute(update, value)
        self.commit()
        
    def delete_order(self):
        ID = int(input("Enter Book ID to be deleted: "))
        delete = "DELETE FROM Orders WHERE ID=%s"
        self.cursor.execute(delete, (ID,))
        self.commit()
        
        
        


library = Library()
updated_library = UpdatedLibrary()
library.create_tables()

print("Press 1 To Add a new Book\nPress 2 To check the Details of Book\nPress 3 to add a new Student\nPress 4 to check details of students\nPress 5 to Add Author to an existing book\nPress 6 to check author by author ID\nPress 7 to add new order\nPress 8 to check details of orders\nPress 9 to add new table\nPress 10 to update student data\nPress 11 to delete a Student\nPress 12 to update a book\nPress 13 to delete a book\nPress 14 to update Author\nPress 15 to delete order")        
    
choice = int(input("Enter your choice between 1-15: "))

if choice == 1:
    library.add_book_prompt()
elif choice == 2:
    library.books_data()
elif choice == 3:
    library.update_student_prompt()
elif choice == 4:
    library.student_data()
elif choice == 5:
    library.update_author_prompt()
elif choice == 6:
    library.update_get_author()
elif choice == 7:
    library.update_order_prompt()
elif choice == 8:
    library.get_order_details()
elif choice == 9:
    updated_library.add_new_table()
elif choice == 10:
    updated_library.update_student_data()
elif choice == 11:
    updated_library.delete_student()
elif choice == 12:
    updated_library.update_book_data()
elif choice == 13:
    updated_library.delete_book()
elif choice == 14:
    updated_library.update_author_data()
elif choice == 15:
    updated_library.delete_order()
else:
    print("Invalid Choice")



