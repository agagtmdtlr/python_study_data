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
        cur = conn.cursor()
        sql = 'select * from country_summary_top_10'
        cur.execute(sql)

        country = [] # 나라이름
        data = [] # 차트 그릴 데이터

        for item in cur:
            country.append(item[0])
            data.append(item[1])

        mycolor = ['r','g','b','y','m','c','#FF0F00','#F0F0FF','#12F0F0','#12F1F4','#653212','#123456']

        chartData = Series(data,index=country)
        chartData.plot(kind='barh',rot=18,title='범죄 빈도 Top 10',
                       color=mycolor,alpha=0.7)

        filename = 'data/oracleChart01.png'
        plt.savefig(filename,dpi=400,bbox_inches='tight')
        print(filename+'파일로 저장됨')


        # pandas.read_sql(sql(str),connection_obj)
        myframe = pd.read_sql(sql,conn,index_col='COUNTRY_TXT') # return pandas.dataframe
        print(myframe)
        print(type(myframe))
        # myframe.plot(kind='bar',rot=18,color=mycolor)

        plt.show()
except Exception as err:
    print(err)
finally:
    # 마지막으로 생성한 부분부터 close
    if cur != None:
        cur.close()
    if conn != None:
        conn.close()