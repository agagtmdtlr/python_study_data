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
        sql = 'select * from region_summary_ranking'
        myframe = pd.read_sql(sql,conn,index_col='region_txt'.upper())
        print(myframe.unstack(0))
        print(type(myframe.unstack(0)))
        mySerise = myframe.unstack(0)

        mySerise.plot(kind='barh',title='지역별 테러 5~8위',color=['b','r','y','g'])
        plt.savefig('concat_data/oracleChart04_01.png', dpi=400, bbox_inches='tight')
        plt.figure()
        mySerise.plot(kind='pie',autopct='%.2f%%',title='지역별 테러 5~8위')
        plt.ylabel('')
        plt.savefig('concat_data/oracleChart04_02.png', dpi=400, bbox_inches='tight')

    plt.show()
except Exception as err:
    print(err)
finally:
    # 마지막으로 생성한 부분부터 close
    if cur != None:
        cur.close()
    if conn != None:
        conn.close()