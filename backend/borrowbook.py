from flask import Blueprint, request, jsonify, render_template
import mysql.connector
from flask_cors import CORS
from datetime import date

borrowbook_app = Blueprint('borrowbook_app', __name__, static_folder='dist', static_url_path='')
CORS(borrowbook_app)

config = {
    'user': 'root',
    'password': 'superbl',
    'host': 'localhost',
    'database': 'sqllab',
    'port': '3306',
    'charset': 'utf8mb4'
}
@borrowbook_app.route('/')
def index():
    return render_template('dist/index.html')


def connect():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    return conn, cursor


def close(conn, cursor):
    cursor.close()
    conn.close()

@borrowbook_app.route('/borrowbook',methods=['POST'])
def borrowbook():
    data = request.get_json()
    bookname = data['bookname']
    id=data['id']

    today = date.today()
    formatted_date = today.strftime('%Y-%m-%d') 


    conn,cursor = connect()

    sql = "SELECT * FROM user WHERE student_id = %s"
    cursor.execute(sql,(id,))
    result = cursor.fetchone()
    if not result:
        close(conn,cursor)
        return jsonify({'status': 'fail', 'message': '该用户不存在！'})
    
    #往book表中插入值
    sql = "INSERT INTO book (bookname,student_id) VALUES (%s,%s)"
    cursor.execute(sql,(bookname,id))
    conn.commit()
    
    #borrow table
    sql="INSERT INTO borrow (borrowdate,bookname,student_id) VALUES (%s,%s,%s)"
    cursor.execute(sql,(formatted_date,bookname,id,))
    conn.commit()

    close(conn,cursor)

    return jsonify({'status': 'success', 'message': '借阅成功！'})


