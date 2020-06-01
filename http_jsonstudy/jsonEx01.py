import json

def get_Json_Data():
    filename = 'data/jumsu.json'
    myfile = open(filename,'rt',encoding='utf-8')
    myfile = myfile.read()
    # print(type(myfile))

    jsonData = json.loads(myfile)
    # print(type(jsonData))
    # print(jsonData)

    for oneitem in jsonData :
        print(oneitem.keys())
        print(oneitem.values())
        print('이름 : '+oneitem['name'])
        kor = float(oneitem['kor'])
        eng = float(oneitem['eng'])
        math = float(oneitem['math'])
        total = kor+eng+math
        print('총점 : '+str(total))

        if 'hello' in oneitem.keys():
            message = oneitem['hello']
            print('메시지 : '+message)
        else :
            pass
        # if 'F' is oneitem['gender']:
        #     print('성별 : 여자')
        # else :
        #     print('성별 : 남자')
        gender = lambda x : '남자' if x['gender'] is 'M' else '여자'
        print(f'성별 : {gender(oneitem)}')
if __name__ == '__main__':
    get_Json_Data()