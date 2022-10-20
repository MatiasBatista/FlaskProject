from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'prueba'
mysql = MySQL(app)

@app.route('/api/customers')
@cross_origin()
def getAllCustomers():
    cur = mysql.connection.cursor()
    cur.execute('SELECT id, firstname, lastname, email, phone, address FROM customers')
    data = cur.fetchall()
    result = []
    for row in data:
        content = {
                'id':row[0],
                'firstname': row[1],
                'lastname': row[2],
                'email': row[3],
                'phone': row[4],
                'address': row[5]
            }
        result.append(content)
    return jsonify(result)


@app.route("/api/personas")
def getAllPersonas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM personas')
    data = cur.fetchall()
    resultado=[]
    for i in data:
        contenido={
            'telefono':i[0],
            'nombre': i[1],
            'apellido': i[2]
        }
        resultado.append(contenido)
    return jsonify(resultado);


@app.route('/api/personas/<telefono>')
@cross_origin()
def getPersona(telefono):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * from personas where telefono=' + str(telefono))
    data = cur.fetchall()
    return jsonify(data)



@app.route('/api/customers/<id>')
@cross_origin()
def getCustomer(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT id, firstname, lastname, email, phone, address FROM customers where id=' + str(id))
    data = cur.fetchall()
    return jsonify(data)





#@app.route('/api/customers', methods=['POST'])
#def cCliente():
    #if 'telefono' in request.json:
     #   modificarCliente()
    #else:
      #  cargarCliente()
    #return "ok"


@app.route('/api/customers/<int:telefono>', methods=['DELETE'])
@cross_origin()
def eliminarCliente(telefono):
    cur = mysql.connection.cursor()
    cur.execute("delete from personas where telefono=" + str(telefono))
    mysql.connection.commit()
    return "Cliente Eliminado"

@app.route('/api/customers', methods=['POST'])
@cross_origin()
def cargarCliente():
    cur = mysql.connection.cursor()
    cur.execute("insert into personas (telefono,nombre,apellido) values (%s,%s,%s)",(request.form['telefono'],request.form['nombre'],request.form['apellido']))
    mysql.connection.commit()
    return "Cliente Guardado"


@app.route('/api/customers', methods=['PUT'])
@cross_origin()
def modificarCliente():
    cur = mysql.connection.cursor()
    cur.execute("update personas set telefono=%s, nombre=%s, apellido=%s where telefono=%s",(request.form['telefono'],request.form['nombre'],request.form['apellido'],request.form['telefono']))
    mysql.connection.commit()
    return "Cliente Modificado"




@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(None, 5000, True)