import pandas as pnd  
import mysql.connector
from flask import Flask, Response, request, render_template, redirect, url_for
import matplotlib.pyplot as plt
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

app = Flask(__name__)

#http://127.0.0.1:5000/TP_record


def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='******',
        password='*****',
        database='*****'
    )

@app.route('/index')
def homeindex():
    return render_template('insert.html')

@app.route('/TP')
def temp_md():
    return render_template('Record.html')




@app.route('/temp', methods=['GET', 'POST'])
def temp():
    if request.method == 'POST':
        temp = request.form['temperatura']
        umid = request.form['umidita']
  
        insert_st = "INSERT INTO TM (temperatura, umidita) VALUES (%s, %s)"
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(insert_st, (temp, umid))
            conn.commit()
        finally:
            cursor.close()
            conn.close()
        return render_template('insert.html')
    


@app.route('/temp_delete', methods=['POST'])
def tempdelete():
    if request.method == 'POST':
        id_to_delete = request.form.get('id')  
        delete_st = "DELETE FROM TM WHERE id = %s"
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(delete_st, (id_to_delete,))
            conn.commit()
        finally:
            cursor.close()
            conn.close()
        return redirect(url_for('temRecord')) #temRecord()
    




@app.route('/TP_record') 
def temRecord():
    conn = get_db_connection()  
    try:
        cursor = conn.cursor()
        query = "SELECT id, temperatura, umidita FROM TM;"
        cursor.execute(query)
        data = cursor.fetchall()
    finally:
        cursor.close()  
        conn.close()  
    return render_template("Record.html", data=data)




@app.route('/show')
def show_tem():
        conn = get_db_connection()
   
        df = pnd.read_sql("SELECT id, temperatura, umidita FROM TM", conn)

       
        fig, ax = plt.subplots()
        df.plot(kind="bar", x="umidita", y="temperatura", ax=ax)

       
        ax.set_title('Temperature vs Humidity')
        ax.set_xlabel('Humidity')
        ax.set_ylabel('Temperature')

       
        img = io.BytesIO()
        FigureCanvas(fig).print_png(img)  
        img.seek(0)
        plt.close(fig)  

       
        return Response(img.getvalue(), mimetype='image/png')
    
    
        conn.close()












if __name__ == '__main__':
    app.run(debug=True)
