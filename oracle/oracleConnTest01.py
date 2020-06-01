import cx_Oracle

conn = None # 접속 객체
cur = None # 커서 객체

try:
    # 아이디/비번@hostname:port_number/sid
    loginfo = 'oraman/oracle@localhost:1521/xe'
    conn = cx_Oracle.connect(loginfo)

    print(type(conn)) # 제대로 나오면 데이터 베이스 접속 성공
    # <class 'cx_Oracle.Connection'>
    if isinstance(conn,cx_Oracle.Connection):
        cur = conn.cursor()
        print(type(cur))

        sql = 'select power(2,10) from dual'
        cur.execute(sql)

        for item in cur:
            print(item)
except Exception as err:
    print(err)

finally:
    # 마지막으로 생성한 부분부터 close
    if cur != None:
        cur.close()
    if conn != None:
        conn.close()