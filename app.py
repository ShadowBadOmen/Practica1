import os

import mysql.connector
from flask import Flask, jsonify, render_template, request


app = Flask(__name__)


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "db"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        user=os.getenv("MYSQL_USER", "flaskuser"),
        password=os.getenv("MYSQL_PASSWORD", "flaskpass"),
        database=os.getenv("MYSQL_DATABASE", "flaskdb")
    )


@app.route("/")
def index():
    return render_template(
        "index.html",
        titulo="Aplicación Flask",
        cursos=["Python", "Flask", "Docker", "MySQL"]
    )


@app.route("/contacto/<nombre>")
def contacto(nombre):
    return render_template("contacto.html", nombre=nombre)


@app.route("/query_string")
def query_string():
    nombre = request.args.get("nombre", "Invitado")
    return render_template("query_string.html", nombre=nombre)


@app.route("/api/cursos")
def api_cursos():
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT id, nombre, descripcion FROM cursos")
        cursos = cursor.fetchall()

        return jsonify(cursos)

    except mysql.connector.Error as error:
        return jsonify({"error": str(error)}), 500

    finally:
        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()


@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template("404.html"), 404


@app.before_request
def before_request():
    pass


@app.after_request
def after_request(response):
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
