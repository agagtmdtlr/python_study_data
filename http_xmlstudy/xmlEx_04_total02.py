from xml.etree.ElementTree import parse,Element
import sqlite3
import cx_Oracle
import re
import pandas as pd
import urllib.parse
import os

# os.environ["NLS_LANG"] = ".AL32UTF8"

tree = parse('concat_data/xmlEx_04_total.xml')
print(tree)
lists = tree.getroot()
print(lists)

loginfo = 'oraman/oracle@localhost:1521/xe'

try:

    cnt =1
    conn = cx_Oracle.connect(loginfo,encoding='utf-8')
    cur = conn.cursor()
    data = []
    cnt = 2
    sql = 'drop table addresses'
    cur.execute(sql)
    conn.commit()
    cnt = 3
    sql = 'create table addresses' \
          ' (store varchar2(255), sido varchar2(255),gungu varchar2(255),road varchar2(255), ' \
          'fulladd varchar2(255), localcode varchar2(255), telno varchar2(255) ,subs varchar2(255) )'
    cur.execute(sql)
    conn.commit()
    cnt = 4
    if isinstance(lists,Element):
        items = lists.findall('item')
        print(type(items))
        for item in items:
            print(type(item.getchildren()[0]))
            print(type(item.getchildren()[0].text))
            row = tuple(x.text for x in item.getchildren())

            sql = 'insert into addresses values(:1,:2,:3,:4,:5,:6,:7,:8)'

            cur.execute(sql,row)

        conn.commit()

    sql = 'select * from addresses'

    myframe = pd.read_sql(sql,conn)
    print(myframe)

except Exception as err :
    print(err)
    print(cnt)
finally:

    if cur != None:
        cur.close()
    if conn != None:
        conn.close()

