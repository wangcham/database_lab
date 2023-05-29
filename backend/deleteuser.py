from flask import Blueprint, request, jsonify, render_template
import mysql.connector
from flask_cors import CORS

deleteuser_app = Blueprint('deleteuser_app', __name__, static_folder='dist', static_url_path='')
CORS(deleteuser_app)

config = {
    'user': 'root',
    'password': 'superbl',
    'host': 'localhost',
    'database': 'sqllab',
    'port': '3306',
    'charset': 'utf8mb4'
}
@deleteuser_app.route('/')
def index():
    return render_template('dist/index.html')


def connect():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    return conn, cursor


def close(conn, cursor):
    cursor.close()
    conn.close()

@deleteuser_app.route('/deleteuser',methods=['POST'])
def deleteuser():
    data = request.get_json()
    id=data['id']

    conn,cursor = connect()

    sql = "SELECT * FROM user WHERE student_id = %s"
    cursor.execute(sql,(id,))
    result = cursor.fetchone()
    if not result:
        close(conn,cursor)
        return jsonify({'status': 'fail', 'message': '该用户不存在！'})
    
    #从user表中删除用户
    sql = "DELETE FROM user WHERE student_id = %s"
    cursor.execute(sql,(id,))

    #从借阅信息中删除用户
    sql = "DELETE FROM borrow WHERE student_id = %s"
    cursor.execute(sql,(id,))
    conn.commit()
    
    #从图书信息中删除用户
    sql="DELETE FROM book WHERE student_id=%s"
    cursor.execute(sql,(id,))
    conn.commit()
    close(conn,cursor)

    return jsonify({'status': 'success', 'message': '删除成功！'})