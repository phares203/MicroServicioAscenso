from distutils.log import debug
from sqlite3 import Cursor
from unicodedata import name
from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


from config import config

app = Flask(__name__)

# settings
app.secret_key = 'mysecretkey'

conexion=MySQL(app)


@app.route('/campañas_a2censo')
def Index():
    cur = conexion.connection.cursor()
    cur.execute('SELECT * From campaign')
    data = cur.fetchall()
    return render_template('index.html', campaigns = data)

#Mensaje de error si se ingresa una url erronea
def pagina_no_encontrada(error):
    return '<h1>La página que intentas buscar no existe...</h1>'

#
@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        requestedAmount = request.form['requestedAmount']
        cur = conexion.connection.cursor()
        cur.execute('INSERT INTO campaign (name, amount, requestedAmount) VALUES (%s, %s, %s)',
        (name, amount, requestedAmount))
        conexion.connection.commit()
        flash ('Campaign Added successfully')
        return redirect(url_for('Index'))


@app.route('/edit/<string:idcampaign>')
def get_contact(idcampaign):
    cur = conexion.connection.cursor()
    cur.execute('SELECT * FROM campaign WHERE idcampaign = %s', (idcampaign))
    data = cur.fetchall()
    print(data[0])
    return render_template('Edit-campaign.html', campaign = data[0])
    
@app.route('/update/<idcampaign>', methods = ['POST'])
def update_campaign(idcampaign):
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        requestedAmount = request.form['requestedAmount']
    cur = conexion.connection.cursor()
    cur.execute("""
      UPDATE campaign
      SET name = %s,
          amount = %s,
          requestedAmount = %s
      WHERE idcampaign = %s
    """, (name, amount, requestedAmount,idcampaign))
    conexion.connection.commit()
    flash('Campaing Updated Successfully!')
    return redirect(url_for('Index'))

@app.route('/delete/<string:idcampaign>')
def delete_contact(idcampaign):
    cur = conexion.connection.cursor()
    cur.execute('DELETE FROM campaign WHERE idcampaign = {0}'. format(idcampaign))
    conexion.connection.commit()
    flash('Campaing removed successfully')
    return redirect(url_for('Index'))


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run() 