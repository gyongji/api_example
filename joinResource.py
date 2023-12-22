# 라이브러리 호출
from flask import request   # 클라이언트에서 입력한 정보 받아오기
from flask_restful import Resource  # 입력받은 정보를 자원화
import sqlite3.connector    # DB연동
from sqlite3_connection import get_connection   # DB 연동 정보를 저장한 사용자 파일

# DB 연결, 개인의 환경에 맞게 설정
connection = sqlite3.connector.connect(
    host = 'host',
    database = 'DB',
    user = 'user_name',
    password = 'user_pwd'
)

# API를 만들기 위한 클래스 작성
# 클래스 : 변수와 함수로 구성된 묶음
# 클래스는 상속이 가능
# API를 만들기 위한 클래스는 flask_restful 라이브러리의 Resource class를 상속해서 생성하여야 함
class joinResource(Resource):
    # restfulAPI의 methods에 해당하는 함수 작성
    def post(self):
        # api 실행 코드를 여기에 작성
        # 클라이언트에서 body 부분에 작성한 json을 받아오는 코드
        data = request.get_json()
        try:
            # DATA INSERT
            # 1. Connect DB
            connection = get_connection()

            # 2. SQL Query
            query = '''
                    insert into joinmember
                        (id, name, passward, birthdate, gender, email)
                    values
                        ('%s', '%s', '%s', '%d', '%d', '%s');
                    '''
            record = (data['id'], data['name'], data['passward'], data['birthdate'], data['gender'], data['email'])

            # 3. Get Cursor
            cursor = connection.cursor()

            # 4. Execute Query with cursor
            cursor.execute(query, record)

            # 5. DATA commit
            connection.commit()

            # 6. Close Resource
            cursor.close()
            connection.close()

        # 입력한 값이 올바르지 않을 경우 에러 출력
        except sqlite3.connector.Error as e :
            print(e)
            cursor.close()
            connection.close()
            return {"error" : str(e)}, 503  #HTTPStatus.SERVICE_UNAVAILAVLE

        # 정상적으로 됐을 때 200, 기본 값이므로 생략 가능
        return {"result" : "success"}, 200