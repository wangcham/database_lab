from flask import Flask
import mysql.connector

from adduser import adduser_app
from borrowbook import borrowbook_app
from deleteuser import deleteuser_app
from returnbook import returnbook_app
from senddata import senddata_app





app = Flask(__name__)
app.register_blueprint(adduser_app)
app.register_blueprint(deleteuser_app)
app.register_blueprint(borrowbook_app)
app.register_blueprint(returnbook_app)
app.register_blueprint(senddata_app)

config = {
    'user': 'root',
    'password': 'superbl',
    'host': 'localhost',
    'database': 'sqllab',
    'port': '3306',
    'charset': 'utf8mb4'
}

def create_tables():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # 创建user表
    user_table = """
    CREATE TABLE IF NOT EXISTS user (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        dept VARCHAR(255),
        student_id VARCHAR(255)
    )
    """
    cursor.execute(user_table)

    # 创建借阅表
    borrow_table = """
    CREATE TABLE IF NOT EXISTS borrow (
        id INT AUTO_INCREMENT PRIMARY KEY,
        borrowdate DATE,
        returndate DATE,
        bookname VARCHAR(255),
        student_id VARCHAR(255)
    )
    """
    cursor.execute(borrow_table)

    # 创建书籍表
    book_table = """
    CREATE TABLE IF NOT EXISTS book (
        id INT AUTO_INCREMENT PRIMARY KEY,
        bookname VARCHAR(255),
        student_id VARCHAR(255)
    )
    """
    cursor.execute(book_table)

    # 提交更改
    conn.commit()

    # 关闭连接
    cursor.close()
    conn.close()

# 创建表
create_tables()

if __name__ == '__main__':
    app.run()
