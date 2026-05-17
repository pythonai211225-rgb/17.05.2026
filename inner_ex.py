from db import run_query_select, run_update_query

run_update_query("""DROP TABLE IF EXISTS departments;""")
run_update_query("""DROP TABLE IF EXISTS employees;""")

run_update_query("""CREATE TABLE departments (
  id        INTEGER PRIMARY KEY,
  dept_name TEXT    NOT NULL,
  budget    REAL    NOT NULL
);""")

run_update_query(f"INSERT INTO departments VALUES (?, ?, ?)", (1,'Engineering',150000))
run_update_query(f"INSERT INTO departments VALUES (?, ?, ?)", (2,'Marketing',80000))
run_update_query(f"INSERT INTO departments VALUES (?, ?, ?)", (3,'Sales',60000))
run_update_query(f"INSERT INTO departments VALUES (?, ?, ?)", (4,'HR',45000))

run_update_query("PRAGMA foreign_keys = ON;")

run_update_query("""CREATE TABLE employees (
  id         INTEGER PRIMARY KEY,
  name       TEXT    NOT NULL,
  dept_id    INTEGER,
  salary     REAL    NOT NULL,
  FOREIGN KEY (dept_id) REFERENCES departments(id)
); """)

run_update_query(f"INSERT INTO employees VALUES (?, ?, ?, ?)", (1,'Dana',1,9000))
run_update_query(f"INSERT INTO employees VALUES (?, ?, ?, ?)", (2,'Omar',2,7200))
run_update_query(f"INSERT INTO employees VALUES (?, ?, ?, ?)", (3,'Noa',1,6800))
run_update_query(f"INSERT INTO employees VALUES (?, ?, ?, ?)", (4,'Liam',3,5500))
run_update_query(f"INSERT INTO employees VALUES (?, ?, ?, ?)", (5,'Rina',None,6000))
run_update_query(f"INSERT INTO employees VALUES (?, ?, ?, ?)", (6,'Kai',2,7000))

result = run_query_select("""SELECT e.name, d.dept_name, d.budget
    FROM   employees e
    INNER JOIN departments d ON e.dept_id = d.id;""")

for e in result:
    print(e)

# ================================ Interactive
id = int(input('whats your id?'))
name = input('whats your name?')
dept_id = input('whats your dept_id?')
salary = input('whats your salary?')
try:
    run_update_query(f"INSERT INTO employees VALUES (?, ?, ?, ?)", (id, name, dept_id, salary))
except Exception as e:
    print('failed to insert', e)

# ============= input id number from user, then print 'exist' if user exist in employee table
