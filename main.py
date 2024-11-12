import psycopg2

db = psycopg2.connect(
    database='fn27',
    user='postgres',
    host='localhost',
    password='1'
)

cursor = db.cursor()

# JADVALLARNI YARATAMIZ

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cars(
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        model TEXT,
        year INTEGER,
        price NUMERIC(12, 2),
        is_available BOOL DEFAULT True
    );
    
    CREATE TABLE IF NOT EXISTS clients(
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        lastname VARCHAR(50),
        phone CHAR(13),
        address TEXT
    );
    
    CREATE TABLE IF NOT EXISTS orders(
        id SERIAL PRIMARY KEY,
        car_id INTEGER NOT NULL REFERENCES cars(id) ON DELETE CASCADE,
        client_id INTEGER NOT NULL REFERENCES clients(id) ON DELETE CASCADE,
        time DATE DEFAULT CURRENT_DATE,
        total_price NUMERIC(12, 2)
    );
    
    CREATE TABLE IF NOT EXISTS employees(
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        job_status VARCHAR(50),
        salary NUMERIC(10, 2)
    );
''')

# JADVALLARGA O'ZGARTIRISH KIRITAMIZ

# cursor.execute('''
#     ALTER TABLE clients ADD COLUMN IF NOT EXISTS email VARCHAR(100) DEFAULT 'example@gmail.com';
#
#     ALTER TABLE clients RENAME COLUMN name TO ism;
#
#     ALTER TABLE clients RENAME TO mijozlar;
# ''')

# natijani ko'ramiz

# cursor.execute('''SELECT * FROM mijozlar''')
# print(cursor.fetchall())

# cursor.execute('''SELECT ism, email FROM mijozlar''')
# print(cursor.fetchall())

# JADVALGA MA'LUMOTLAR QO'SHAMIZ

# cursor.execute('''
#     INSERT INTO cars(name, model, year, price) VALUES
#     ('Mercedes', 'AMG', 2024, 200000),
#     ('BMW', 'M5', 2024, 300000),
#     ('Porsche', '911 Turbo S', 2024, 250000);
#
#     INSERT INTO mijozlar(ism, lastname, phone, address) VALUES
#     ('Toxir', 'Toxirov', '+998991234567', 'Ferghana'),
#     ('Sobir', 'Sobirov', '+998971235897', 'Tashkent'),
#     ('Jalil', 'Jalilov', '+998954213685', 'Andijan');
#
#     INSERT INTO orders(car_id, client_id, total_price) VALUES
#     (1, 1, 200000),
#     (2, 2, 300000),
#     (3, 3, 250000);
#
#     INSERT INTO employees(name, job_status, salary) VALUES
#     ('Jamshid', 'Sales Manager', 15000),
#     ('Bobur', 'Manager', 30000),
#     ('Ali', 'CEO', 150000);
# ''')

# 4 - topshiriq MA'LUMOTLARNI O'ZGARTIRAMIZ

# cursor.execute('''
#     UPDATE employees SET name = 'Azizbek' WHERE id = 3;
#
#     UPDATE employees SET name = 'Akmaljon' WHERE id = 2;
# ''')

# cursor.execute('''select * from employees''')
# for data in cursor.fetchall():
#     print(data)

# 5 - topshiriq MA'LUMOTLARNI O'ZGARTIRAMIZ

# cursor.execute('''
#     DELETE FROM employees WHERE id = 1;
# ''')

# cursor.execute('''select * from employees''')
# for data in cursor.fetchall():
#     print(data)

# HAR BIR JADVAL MA'LUMOTLARINI ALOHIDA KO'RAMIZ

# cursor.execute('''SELECT * FROM cars''')
# for data in cursor.fetchall():
#     print(data)

# cursor.execute('''SELECT * FROM mijozlar''')
# for data in cursor.fetchall():
#     print(data)

# cursor.execute('''SELECT * FROM employees''')
# for data in cursor.fetchall():
#     print(data)

# JOIN ORQALI MA'LUMOTLARNI JAMLAB CHIQARAMIZ

# cursor.execute('''
#     SELECT
#         cars.id,
#         cars.name,
#         cars.price,
#         cars.is_available,
#         mijozlar.ism,
#         mijozlar.phone,
#         mijozlar.email,
#         orders.time
#     FROM cars
#     JOIN orders ON cars.id = orders.car_id
#     JOIN mijozlar ON mijozlar.id = orders.client_id;
# ''')
# for data in cursor.fetchall():
#     print(data)

db.commit()
cursor.close()
db.close()
