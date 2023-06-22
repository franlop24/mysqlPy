import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="example",
  database="base3a"
)

mycursor = mydb.cursor()

def add_customer(name, address):
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = (name, address)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    return mycursor.lastrowid

def add_many_customers(customers):
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    mycursor.executemany(sql, customers)
    mydb.commit()
    print(mycursor.rowcount, "records inserted.")

customers = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

#add_many_customers(customers)
def show_customers():
  mycursor.execute("SELECT * FROM customers")

  myresult = mycursor.fetchall()

  for x in myresult:
    print(x)

def get_customer_by_id(id):
  mycursor.execute(f"SELECT * FROM customers WHERE id = { id }")

  myresult = mycursor.fetchone()

  return myresult

def get_customer_by_name(name):
  sql = f"SELECT * FROM customers WHERE name LIKE '%{ name }%'"
  mycursor.execute(sql)

  myresult = mycursor.fetchall()   

  return myresult

def delete_customer_by_id(id):
  sql = f"DELETE FROM customers WHERE id = { id }"

  mycursor.execute(sql)

  mydb.commit()

  print(mycursor.rowcount, "record(s) deleted")

def update_customer(id, name="", address=""):
  customer = get_customer_by_id(id)
  if not name:
     name = customer[0]
  if not address:
     address = customer[1]
  sql = "UPDATE customers "
  sql += f"SET address = '{ address }', name = '{ name }'"
  sql += f" WHERE id = { id }"

  print(sql)
  mycursor.execute(sql)

  mydb.commit()

  print(mycursor.rowcount, "record(s) affected") 