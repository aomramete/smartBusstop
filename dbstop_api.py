from flask import Flask, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()


app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Tspwcrw42'
app.config['MYSQL_DATABASE_DB'] = 'stoploca'
app.config['MYSQL_DATABASE_HOST'] = '35.186.147.96'
mysql.init_app(app)
@app.route('/allstops/')
def allstops():
    cur = mysql.connect().cursor()
    cur.execute("select Name,Latitude,Longitude from stoploc")
    data = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify(data)

@app.route('/stops/<ID>')
def stops_byNum(ID=None):
    cur = mysql.connect().cursor()
    cur.execute("SELECT * FROM stoploc WHERE ID = %s", ID)
    data = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True, debug=True)
