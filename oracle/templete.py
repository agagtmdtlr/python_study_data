import cx_Oracle
import matplotlib.pyplot as plt
from pandas import Series
import pandas as pd

conn = None # 접속객체
cur = None # 커서객체


try:
    plt.rc('font', family='Malgun Gothic')
    # 아이디/비번@hostname:port_number/sid
    loginfo = 'oraman/oracle@localhost:1521/xe'
    conn = cx_Oracle.connect(loginfo)

    # <class 'cx_Oracle.Connection'>
    if isinstance(conn,cx_Oracle.Connection):
        cur = conn.cursor()
        sql = ''
        cur.execute(sql)

        for item in cur:
            print(item)

    plt.savefig('concat_data/oracleChart02.png', dpi=400, bbox_inches='tight')
except Exception as err:
    print(err)
finally:
    # 마지막으로 생성한 부분부터 close
    if cur != None:
        cur.close()
    if conn != None:
        conn.close()