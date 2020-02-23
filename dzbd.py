import sqlite3
conn = sqlite3.connect("dz.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE Employees
                                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    'name' TEXT,
                                    'surname' TEXT ,
                                    'phone' INTEGER)''')

cursor.execute('''CREATE TABLE Salary
                                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    id_Employees INTEGER,
                                    Salary INTEGER,
                                    Bonus INTEGER,
                                    Overtime INTEGER,
                                    FOREIGN KEY (id_Employees) REFERENCES Employees(id))''')
cursor.execute('''CREATE TABLE Position
                                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    id_Employees INTEGER,
                                    Skill TEXT,
                                    Position TEXT,
                                    Education TEXT,
                                    FOREIGN KEY (id_Employees) REFERENCES Employees(id))''')


conn.execute('insert into Employees ( name, surname, phone) values( "Evgeniy", "Stupka", +380501112211)')
conn.execute('insert into Employees ( name, surname, phone) values( "Aleksandr", "Gunko", +380507777777)')
conn.execute('insert into Employees ( name, surname, phone) values( "Victor", "Matat", +380502221122)')
conn.commit()

conn.execute('insert into Salary ( Salary, Bonus, Overtime) values( "500", "100", 150)')
conn.execute('insert into Salary ( Salary, Bonus, Overtime) values( "100", "20", 40)')
conn.execute('insert into Salary ( Salary, Bonus, Overtime) values( "1000", "500", 2000)')
conn.commit()

conn.execute('insert into Position ( Skill, Position, Education) values( "Сounting", "Accountant", Higher)')
conn.execute('insert into Position ( Skill, Position, Education) values( "Coding", "Programmer", Higher)')
conn.execute('insert into Position ( Skill, Position, Education) values( "Sales", "Seller", Secondary)')
conn.commit()
