from flask import Flask, request
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='API 문서', description='Swagger 문서', doc="/api-docs")

# 상수값 정의
USER_INFO = [['test', 'test_id'], ['test', 'test_pw']] # [[id], [pw]]

# 네임스페이스 생성
test_api = api.namespace('test', description='조회 API')

# /login 엔드포인트 생성
@test_api.route('/login')
class Test(Resource):
    @api.expect(api.model('LoginData', {
        'id': fields.String(required=True, description='User ID'),
        'pw': fields.String(required=True, description='Password')
    }))
    def post(self):
        request_data = request.get_json()

        input_id = request_data.get('id', '')
        input_pw = request_data.get('pw', '')

        i = 0
        while i < len(USER_INFO):
            user_id = USER_INFO[0][i] #id
            user_pw = USER_INFO[1][i] #pw

            if input_id == user_id and input_pw == user_pw:
                return {'result': 'success'}, 200
            else:
                flag = 'failure'
                status = 401
                i += 1

        return {'result': 'failure'}, 401

# /login 엔드포인트 생성
@test_api.route('/findId')
class FindId(Resource):
    @api.expect(api.model('LoginData', {
        'id': fields.String(required=True, description='User ID')
    }))
    def post(self):
        request_data = request.get_json()

        input_id = request_data.get('id', '')

        i = 0
        while i < len(USER_INFO[0]):
            user_id = USER_INFO[0][i] #id

            if input_id == user_id:
                return {
                    'result': 'success',
                    'id' : user_id,
                    'pw' : USER_INFO[1][i]
                }, 200
            else:
                flag = 'failure'
                status = 401
                i += 1

        return {'result': 'failure'}, 401

if __name__ == '__main__':
    app.run(debug=True)