from flask import Flask, render_template
from flask_mysqldb import MySQL


app = Flask(__name__)

# DB Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '763jHJGfjhg53iggJHv__76gg!'
app.config['MYSQL_DB'] = 'testdb'

mysql = MySQL(app)


@app.route('/', methods=['GET'])
def index():
    cur = mysql.connection.cursor()
    table_details = cur.fetchall()
    return render_template('index.html', table_details=table_details)


if __name__ == '__main__':
    app.run(debug=True)
