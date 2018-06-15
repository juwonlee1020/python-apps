import psycopg2

#You need to have an existing database on pgAdmin III
#Create a new server: PostgreSQL
#Create a new database whose owner is PostgreSQL
def create_table():
    conn = psycopg2.connect("dbname= 'database 1' user ='postgres' host='localhost'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def delete(item):
    conn = psycopg2.connect("dbname='databse 1' user='postgres' host='localhost'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item))
    conn.commit()
    conn.close()

def update(item, quantity, price):
    conn = psycopg2.connect("dbname='database 1' user='postgres' host='localhost'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect("dbname ='database 1' user='postgres' host='localhost' ")
    cur = conn.cursor()
    #Code below is a bad idea because it's prone to sql injection!
    #cur.execute("INSERT INTO store VALUES('%s', '%s', '%s')" %(item, quantity, price))
    cur.execute("INSERT INTO store VALUES(%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='database 1' user='postgres' host='localhost'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

update("New Wine", 10, 2000000)
print(view())