import SQL_connection

conString='Driver={SQL Server};''server=ALI-PC\SQLEXPRESS;''Database=user_controll;''Trusted_Connection=yes;'
qString='SELECT * FROM users'
qString2='SELECT * FROM users WHERE user_ID=2'

conn=SQL_connection.connection(conString)
conn.query(qString)
conn.query(qString2)