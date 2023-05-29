from flask import Blueprint, request, jsonify, render_template
import mysql.connector
from flask_cors import CORS

adduser_app = Blueprint('adduser_app', __name__, static_folder='dist', static_url_path='')
CORS(adduser_app)

config = {
    'user': 'root',
    'password': 'superbl',
    'host': 'localhost',
    'database': 'sqllab',
    'port': '3306',
    'charset': 'utf8mb4'
}
@adduser_app.route('/')
def index():
    return render_template('dist/index.html')


def connect():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    return conn, cursor


def close(conn, cursor):
    cursor.close()
    conn.close()

@adduser_app.route('/adduser',methods=['POST'])
def adduser():
    data = request.get_json()
    name = data['name']
    id=data['id']
    dept=data['dept']

    conn,cursor = connect()

    sql = "SELECT * FROM user WHERE student_id = %s"
    cursor.execute(sql,(id,))
    result = cursor.fetchone()
    if result:
        close(conn,cursor)
        return jsonify({'status': 'fail', 'message': '该用户已经存在！'})
    
    sql = "INSERT INTO user (name,dept,student_id) VALUES (%s,%s,%s)"
    cursor.execute(sql,(name,dept,id))
    conn.commit()

    close(conn,cursor)

    return jsonify({'status': 'success', 'message': '添加学生成功！'})


