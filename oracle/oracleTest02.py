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
        sql = 'select * from three_country'
        myfrmae = pd.read_sql(sql,conn)
        # Index(['COUNTRY_TXT', 'IYEAR', 'CNT'], dtype='object')
        print(myfrmae.columns)
        # case 1번
        # mygrouping = myfrmae.groupby(by=['COUNTRY_TXT','IYEAR'])['CNT']
        # mydata = mygrouping.sum().unstack(1)
        # print(mydata)

        # case 2번
        myfrmae.set_index(['COUNTRY_TXT','IYEAR'],inplace=True)
        myfrmae = myfrmae.unstack(1)
        print(myfrmae)
        myfrmae.plot(kind='barh',title='Top3 연도별 테러 수')
        # print(type(mygrouping))
        # for i in mygrouping:
        #     print(i)
        #     print(type(i))
        # mydata.plot(kind='barh')
        plt.savefig('concat_data/oracleChart02.png',dpi=400,bbox_inches='tight')

        plt.show()
except Exception as err:
    print(err)
finally:
    # 마지막으로 생성한 부분부터 close
    if cur != None:
        cur.close()
    if conn != None:
        conn.close()