from re import DEBUG
from flask import Flask,jsonify
app = Flask(__name__)
import pypyodbc
import json





conn = pypyodbc.connect('Driver={SQL Server};Server=10.10.10.10;Database=EFCoreWebDemo;UID=sa;PWD=Password1')

cursor = conn.cursor()
cursor.execute('SELECT TOP 1000 [SchoolId],[Title] FROM [EFCoreWebDemo].[dbo].[Schools]')
result = cursor.fetchall()



@app.route('/')
def index():
    return "Index"

@app.route("/Schools" , methods=['GET'])
def get():
    return jsonify({"schools:":result})

@app.route("/Schools/<int:schoold_id>" , methods=['GET'])
def get_id(schoold_id):
    cursor.execute(f'SELECT TOP 1000 [SchoolId],[Title] FROM [EFCoreWebDemo].[dbo].[Schools] where SchoolId = {schoold_id}')
    result = cursor.fetchall()
    return jsonify({"school:":result})


if __name__ == "__main__":
    app.run(debug=True)