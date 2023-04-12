from flask import Flask, render_template, request
import mysql.connector
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search_drug():
    if request.method == 'POST':
        drug_name = request.form['drug_name']
        # Use the drug name to search the database and return the result
        return render_template('results.html', result=result)
    return render_template('index.html')
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)

mycursor = mydb.cursor()

def search_drug(drug_name):
  sql = "SELECT * FROM drugs WHERE drug_name = %s"
  val = (drug_name,)
  mycursor.execute(sql, val)
  result = mycursor.fetchone()
  return result
if __name__ == '__main__':
    app.run(debug=True)
    #how to create a website if i have a database of 3 columns drug name ,reason and description where the drug name is taken as the input given by the user and when the input is given it checks for the input keyword in the database then returns the corresponding row identified in the database 
