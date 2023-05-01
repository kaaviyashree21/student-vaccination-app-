from flask import Flask, request
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form method="post" action="/vaccination_status">
            <label for="regno">Registration Number:</label>
            <input type="text" id="regno" name="regno"><br><br>
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/vaccination_status', methods=['POST'])
def vaccination_status():
    conn = psycopg2.connect(
        host="localhost",
        database="studentDetails",
        user="postgres",
        password="1234"
    )
    cur = conn.cursor()
    regno = request.form['regno']
    cur.execute("SELECT * FROM student WHERE RegNo=%s", (regno,))
    result = cur.fetchone()
    if result:
        name = result[1]
        vaccinated = result[2]
        return f'{name} has {vaccinated} Vaccinated'
    else:
        return 'Student not found'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
