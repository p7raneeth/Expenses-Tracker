import pyodbc
import datetime
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=.;'
                      'Database=smp1;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
values = []
k = input('please enter the number of items you bought : ')
for i in range(int(k)):
    x = input('who made the payment : ')
    cursor.execute(f"select Person_name from tbl_persons where Person_ID = {x}")
    result = cursor.fetchall()
    for r in result:
        values.append(r)
    y = input('what is the payment mode : ')
    cursor.execute(f"select payment_mode from tbl_payment where Payment_ID = {y}")
    result = cursor.fetchall()
    for r in result:
        values.append(r)
    z = input('what is the item that was purchased : ')
    cursor.execute(f"select item_Name from tbl_item where item_ID = {z}")
    result = cursor.fetchall()
    for r in result:
        values.append(r)
    a = input(f'what is the quantity of {values[2][0]} purchased? : ')
    cursor.execute(f"select Price_Per_Kg from tbl_item where item_ID = {z}")
    result = cursor.fetchall()
    for r in result:
        values.append(r)
    price = float(values[3][0])*float(a)
    b = input(f'what is ratio of split? : ')
    cursor.execute("INSERT INTO tbl_transaction (transaction_date, day_of_week, payment_mode_name, paid_by, item_name, quantity, split_ratio,total_price ) VALUES (?,?,?,?,?,?,?,?)",
    (datetime.datetime.now(), datetime.datetime.now().strftime("%A"), values[1][0], values[0][0], values[2][0], a, b, price))
    values = []
conn.commit()
conn.close()