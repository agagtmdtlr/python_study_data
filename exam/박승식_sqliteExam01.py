import sqlite3
class Product:
    def __init__(self,dbname):
        self.conn = sqlite3.connect(dbname)
        self.cursor = self.conn.cursor()

    def create(self):
        sql = " create table products" \
              " (code text , sang text , stock number , dan number )"
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            pass

    def delete(self):
        sql = "drop table products"
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            pass

    def insert(self,data):
        sql = " insert into products (code,sang,stock,dan)" \
              " values(?,?,?,?) "
        try:
            self.cursor.executemany(sql,data)
            self.conn.commit()
        except:
            pass

    def findCode(self,code):
        sql = " select * from products where code = ?"
        return self.cursor.execute(sql,(code,))

    def findStock(self,stock):
        sql = " select * from products where stock >= ?"
        return self.cursor.execute(sql,(stock,))

dbname = 'product.db'
data = [('glove','장갑',3,5000),('leather','가죽장갑',10,50000),('jump','가죽점퍼',5,650000)]
pr = Product(dbname)
pr.delete()
pr.create()
pr.insert(data)
code = 'glove'
result = pr.findCode(code)
for code,sang,stock,dan in result:
    print(f'코드 : {code}, '
          f'이름 : {sang}, '
          f'재고 : {stock}, '
          f'단가 : {dan}')
stock = 5
result = pr.findStock(stock).fetchall()
print(result)