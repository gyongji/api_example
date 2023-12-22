from flask import Flask
from flask_restful import Api
from resources.joinmember import joinResource

## API 서버 구축하기
# API 서버를 구축하기 위한 기본 구조
app = Flask(__name__)

# restfulAPI 생성
api = Api(app)

# 경로와 리소스(api코드) 연결
api.add_resource(joinResource, '/join')

# API는 함수로 처리
@app.route('/join', methods=['POST'])   # 얘만 수정함
def join():
    return

if __name__ == '__main__':
    app.run()

