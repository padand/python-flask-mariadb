# import the necessary packages
import flask
import json
import mysql.connector as database
import os

app = flask.Flask(__name__)
# This will auto reload the flask app when a code change happens:
app.config["DEBUG"] = True

# configuration used to connect to MariaDB
# https://www.digitalocean.com/community/tutorials/how-to-store-and-retrieve-data-in-mariadb-using-python-on-ubuntu-18-04
config = {
    'host': os.environ['DB_HOST'],
    'port': os.environ['DB_PORT'],
    'user': os.environ['DB_USER'],
    'password': os.environ['DB_PASS'],
    'database': os.environ['DB_NAME']
}

# route to return all people
@app.route('/api/people', methods=['GET'])
def index():
   # connection for MariaDB
   conn = database.connect(**config)
   # create a connection cursor
   cur = conn.cursor()
   # execute a SQL statement
   cur.execute("select * from people")

   # serialize results into JSON
   row_headers=[x[0] for x in cur.description]
   rv = cur.fetchall()
   json_data=[]
   for result in rv:
        json_data.append(dict(zip(row_headers,result)))

   # return the results!
   return json.dumps(json_data)

app.run(host='0.0.0.0')