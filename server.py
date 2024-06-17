from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("home.html")
    
@app.route("/register_page")
def register_page():
    return render_template("register.html")
    
@app.route("/Registro_Usuario", methods=["post"])
def Registro_Usuario():
    id = request.form["id"]
    Nombre = request.form["Nombre"]
    Apellidos = request.form["Apellidos"]
    Telefono = request.form["Telefono"]
    Correo = request.form["Correo"]
    Nombre_Mascota = request.form["Nombre_Mascota"]
    print(id, Nombre, Apellidos, Telefono, Correo, Nombre_Mascota)
    return "ok"
    
@app.route("/consult_page")
def consult_page():
    return render_template("consult.html")

@app.route("/info_page")
def info_page():
    return render_template("info.html")

@app.route("/info_page")
def inicio_page():
    return render_template("home.html")
    
if __name__ == "__main__":
    host = '0.0.0.0'
    port = '8080' 
    app.run(host, port)