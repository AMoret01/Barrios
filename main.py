from flask import Flask,jsonify,request
from sqlalchemy import create_engine
import psycopg2
import pandas as pd


app=Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return """
    <h1> Pantalla Inicio</h1>
    Rutas:</br>
    All barrios->/api/v1/barrios</br>
    By Nombre->/api/v1/barrios/nombre</br>
    By Limites->/api/v1/barrios/limits
    """

@app.route("/api/v1/barrios", methods=["GET"])
def get_barrios():
    engine = create_engine('postgresql://postgres:7bN4HwuhMBqwWXCBVWzY@containers-us-west-45.railway.app:7071/railway')
    datos=pd.read_sql('SELECT * FROM "Barrios"', con=engine )

    return jsonify(datos.to_json())

@app.route("/api/v1/barrios/nombre", methods=["GET"])
def by_name():
    nombre=request.args["Nombre"]
    engine = create_engine('postgresql://postgres:7bN4HwuhMBqwWXCBVWzY@containers-us-west-45.railway.app:7071/railway')
    datos=pd.read_sql(f"""SELECT * FROM "Barrios" where "Nombre"='{nombre}'""", con=engine )

    return jsonify(datos.to_json())

@app.route("/api/v1/barrios/limits", methods=["GET"])
def by_limits():
    min_limit=request.args["min_limit"]
    max_limit=request.args["max_limit"]
    engine = create_engine('postgresql://postgres:7bN4HwuhMBqwWXCBVWzY@containers-us-west-45.railway.app:7071/railway')
    datos=pd.read_sql(f"""SELECT * FROM "Barrios" WHERE "Areas de barrios">'{min_limit}' and "Areas de barrios"<'{max_limit}'""", con=engine )
    return jsonify(datos.to_json())

if __name__=="__main__":
    app.run(debug=True)
























