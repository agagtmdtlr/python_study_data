import sqlite3


def process(dbname):
    try:
        conn = sqlite3.connect(dbname) # 연결 객체생성
        cur = conn.cursor() # 작동 명령 객체생성
        # if exists문은 존재한다면 처리하라는 sql문
        # 해석 : employees 테이블이 존재한다면 drop문을 처리하라
        # 없으면 drop문을 처리하지 말라
        sql = 'drop table if exists employees'
        cur.execute(sql)

        sql = 'create table employees(id text primary key, name text)'
        cur.execute(sql)

        sql = 'insert into employees(id,name) values ("kim","김유신")'
        cur.execute(sql)
        # parameter
        sql = 'insert into employees(id,name) values (?,?)'
        cur.execute(sql,('lee','이순신'))
        # tuple parameter
        mytuple = ('sime','심봉사')
        sql = 'insert into employees(id,name) values (?,?)'
        cur.execute(sql, mytuple)
        # list parameter
        mylist = ['kang','강감찬']
        sql = 'insert into employees(id,name) values (?,?)'
        cur.execute(sql, mylist)
        # dict parameter
        mydict = {'sabun':'yu','irum':'유관순'}
        sql = 'insert into employees(id,name) values (:sabun,:irum)'
        cur.execute(sql, mydict)
        # dict no sort parameter
        # dict 형은 순차적으로 넣어줄 필요가 없다 ( 맵핑화 )
        mydict = { 'irum': '소쩍새','sabun': 'so'}
        sql = 'insert into employees(id,name) values (:sabun,:irum)'
        cur.execute(sql, mydict)

        # 트렌잭션이 끝나면 꼭 커밋해서 진행상황 저장하기
        conn.commit()

        sql = 'select * from employees'
        cur.execute(sql)
        for row in cur :
            print(row)
        print('-'*30)

    except sqlite3.Error as err:
        print('에러 :',err)
        # 트렌잭션 에러 발생시 이전 상태로 복구시키기
        conn.rollback()
    finally:
        cur.close()
        conn.close()

# 해당 스크립트 직접 실행 시 작동
if __name__ == '__main__':
    process('emp.db')
