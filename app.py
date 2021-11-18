from flask import Flask, render_template, redirect, jsonify, request
import os
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


#################################################
# Database Setup - SQL
#################################################
#establish connection to SQL database in AWS - refer to https://stackoverflow.com/questions/54300263/connect-to-aws-rds-postgres-database-with-python/54313925

endpoint = os.getenv('db_endpoint')
username = os.getenv('db_username')
password = os.getenv('db_password')

engine = create_engine(f'postgresql://{username}:{password}@{endpoint}:5432/James_Bond')
conn = engine.connect()

# Create an instance of Flask
app = Flask(__name__)


# Route to render index.html template using data 
@app.route("/")
def home():

        # # Return template and data
    return render_template("index.html")

@app.route("/api/get_bond_girls")
def girl_bond():

    #extract the sql table and turn it into a dataframe
    session=Session(engine)
    bond_girl=pd.read_sql_table("bond_girl_data_cleaned_v3", conn)
    bond_girl_json = bond_girl.to_json(orient = "records")
    session.close()

    # # Return template and data
    return (bond_girl_json)

if __name__ == "__main__":
    app.run(debug=True)


