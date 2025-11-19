from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt, datetime
from database import get_db

app = Flask(__name__)
app.config["SECRET_KEY"] = "c91f8e3a4d7b1f2c9eb72a94f5bd13eaa6c4d2f8b73c91e4f0a6b1d29cf84e31"


# -------------------------------
# ROTA DE REGISTRO
# -------------------------------
@app.post("/register")
def register():
    data = request.json
    username = data.get("username")
    password = generate_password_hash(data.get("password"))

    db = get_db()
    try:
        db.execute("INSERT INTO users(username, password) VALUES (?, ?)",
                   (username, password))
        db.commit()
        return jsonify({"message": "Usuário criado!"})
    except:
        return jsonify({"error": "Usuário já existe"}), 400


# -------------------------------
# ROTA DE LOGIN
# -------------------------------
@app.post("/login")
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    db = get_db()
    user = db.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone()

    if not user or not check_password_hash(user[2], password):
        return jsonify({"error": "Credenciais inválidas"}), 401

    token = jwt.encode({
        "user": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }, app.config["SECRET_KEY"])

    return jsonify({"token": token})


# -------------------------------
# ROTA PROTEGIDA
# -------------------------------
@app.get("/protected")
def protected():
    token = request.headers.get("Authorization")

    if not token:
        return jsonify({"error": "Token ausente"}), 401

    try:
        jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
        return jsonify({"message": "Acesso permitido!"})
    except:
        return jsonify({"error": "Token inválido"}), 403


# -------------------------------
# INICIAR SERVIDOR
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
