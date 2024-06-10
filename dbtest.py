import mysql.connector

# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="passwords",
#     database="ranil_proj"
# )


try:
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="passwords",
    database="ranil_proj"
)
except Exception as e:
    print(e)
    exit()
    
mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE testdb")


# intserting into database

# mycursor.execute("INSERT INTO person(name,age) VALUES (%s,%s)" , ("tim",19))

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)


# inserting multiple

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)



mycursor.execute("DESCRIBE testdb")
for x in mycursor:
    print(x)

# mycursor.execute("SELECT * FROM ranil_proj.testdb")
# for x in mycursor:
#     print(x)



# db.commit()