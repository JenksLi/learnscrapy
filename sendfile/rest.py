'''
# coding: utf8
'''
# pip install flask
import sys
import json
# reload(sys)
# sys.setdefaultencoding('utf-8')
from flask import Flask, abort, request, jsonify

app = Flask(__name__)

# 测试数据暂时存放
tasks = []

@app.route('/voice_msg/', methods=['POST'])
def add_task():
    # if not request.json or 'username' not in request.json or 'password' not in request.json:
    #     abort(400)
    # task = {
    #     'username': request.json['username'],
    #     'password': request.json['password']
    # }
    # tasks.append(task)
    # if request.json['username'] == 'jenks':
    #     return jsonify({"status":0,"message":"验证成功","data": 'null'})
    # else:
    #     return jsonify({"status":1,"message":"验证失败!账号或密码错误！","data":'null'})
    res = {
        "result": 'True',
        "code": "00",
        "message": "",
        "data": {
            "instance_id": "2662152044"
        }
    }
    app.logger.debug(request.data)
    return jsonify(res)


if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.run(host="0.0.0.0", port=8383, debug=True)

