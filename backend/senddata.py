from flask import Blueprint, request, jsonify, render_template
import mysql.connector
from flask_cors import CORS

senddata_app = Blueprint('senddata_app', __name__, static_folder='dist', static_url_path='')
CORS(senddata_app)

config = {
    'user': 'root',
    'password': 'superbl',
    'host': 'localhost',
    'database': 'sqllab',
    'port': '3306',
    'charset': 'utf8mb4'
}
@senddata_app.route('/')
def index():
    return render_template('dist/index.html')


def connect():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    return conn, cursor


def close(conn, cursor):
    cursor.close()
    conn.close()

@senddata_app.route('/getborrowlist',methods=['POST'])
def getborrowlist():
    conn,cursor = connect()
    
    sql = "SELECT borrowdate,returndate,bookname,student_id FROM borrow"
    cursor.execute(sql)

    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # 将数据转换为字典列表形式
    columns = ['borrowdate', 'returndate', 'bookname', 'student_id']
    result = [{columns[i]: row[i] for i in range(len(columns))} for row in data]
    return jsonify(result)

@senddata_app.route('/getuserlist',methods=['POST'])
def getuserlist():
    conn,cursor = connect()

    sql="SELECT name,student_id,dept from user"
    cursor.execute(sql)

    data = cursor.fetchall()

    cursor.close()
    conn.close()
    columns = ['name', 'student_id', 'dept']
    result = [{columns[i]: row[i] for i in range(len(columns))} for row in data]
    return jsonify(result)




