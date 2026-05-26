import sqlite3
connection = sqlite3.connect(
"student.db"
)

cursor = connection.cursor()
cursor.execute(
    
"""
CREATE TABLE IF NOT EXISTS students(
id INTEGER,
name TEXT,
city TEXT
)
"""
)

cursor.execute(
"""
INSERT INTO students

VALUES(
1,
'Chintu',
'Warangal'
)
"""
)

cursor.execute(
"""
INSERT INTO students

VALUES(
2,
'ramesh',
'hanamkonda'
)
"""
)

cursor.execute(
"""
SELECT * FROM students
"""
)

data = cursor.fetchall()
print(data)
cursor.execute(
"""
UPDATE students
SET city = 'Bhupalpally'
WHERE id = 1
"""
)

cursor.execute(
"SELECT * FROM students"
)
print(cursor.fetchall())

cursor.execute(
"""
DELETE  FROM students
WHERE id = 2
"""
)

while True:
    print("""
1.Add Student
2.View Students
3.Update Student
4.Delete Student
5.search student
6.Exit
""")
    

    choice = input("enter choice:")

    if choice == "1":
      id = int(input("enter id:"))
      name = input("enter name: ")
      city = input("enter city: ")
      cursor.execute(
      """
      INSERT INTO students
      VALUES(
      ?,?,?
      )
      """,
      (id,name,city)
      )
      connection.commit()
      print("added")
      
    elif choice == "2":
      cursor.execute(
      "SELECT * FROM students"
      )
      print(cursor.fetchall())

    elif choice == "3":
      id = int(input("enter id:"))
      city = input("new city: ")

      cursor.execute(
      """
      UPDATE students
      SET city=?
      WHRE id=?
      """,
      (city,id)
      )
      connection.commit()
      print("updated")

    elif choice == "4":
      id = int(input("enter id:"))

      cursor.execute(
      """
      DELETE FORM students
      WHERE id=?
      """,
      (id,)
      )
      connection.commit()
      print("Deleted")
      
    elif choice == "5":
        id = int(input("enter id: "))
        cursor.execute(
        """
        SELECT * FROM students
        WHERE id =?
        """,
        (id,)
        )
        print(cursor.fetchall())
      
    elif choice == "6":
      break
  

  


cursor.execute(
"""
SELECT * FROM students
"""
)
print(cursor.fetchall())

connection.commit()
connection.close()
