import cx_Oracle
import matplotlib.pyplot as plt
from pandas import Series
import pandas as pd
conn = None # 접속객체
cur = None # 커서객체


plt.rc('font',family='Malgun Gothic')

try:
    # 아이디/비번@hostname:port_number/sid
    loginfo = 'oraman/oracle@localhost:1521/xe'
    conn = cx_Oracle.connect(loginfo)

    # <class 'cx_Oracle.Connection'>
    if isinstance(conn,cx_Oracle.Connection):
        sql = 'select bungi,mycount from bungitable order by ordering'
        myframe = pd.read_sql(sql=sql,con=conn,index_col='bungi'.upper())
        mySeries = myframe.unstack(0)
        print(mySeries)
        print(type(mySeries))

        mySeries.plot(kind='pie',autopct='%.2f%%',title='분기별 테러 비중')
        plt.ylabel('')
        plt.savefig('concat_data/oracleChart03.png',dpi=400,bbox_inches='tight')
        plt.show()
except Exception as err:
    print(err)
finally:
    # 마지막으로 생성한 부분부터 close
    if cur != None:
        cur.close()
    if conn != None:
        conn.close()