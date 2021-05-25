from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route("/")
def url_principal():
	return render_template("template.html",
nombre="JOSE ANTONIO", apellidos="AVILA SALAZAR", escuela="ITESG", edad="24",
nacimiento="28-dic-96",correo="antonio_avila96@outlook.com",ciudad="Guanajuato", carrera="Ing. sistemas computacionales");

if __name__ =="__main__":
	app.run(debug=True);

