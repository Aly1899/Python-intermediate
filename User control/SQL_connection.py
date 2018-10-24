import pyodbc

class connection:
    def __init__(self,conString):
        self.conn=pyodbc.connect(conString)
        self.cur=self.conn.cursor()

    def query(self,qString):
        self.cur.execute(qString)
        for row in self.cur:
            print(row)

