from flask import Flask, render_template, session

app = Flask(
    __name__,
    template_folder="app/templates",
    static_folder="app/static"
)

app.secret_key = "preview-key"

@app.route("/")
def preview():
    session["nombre"] = "Administrador"
    session["usuario_id"] = 1
    return render_template(
        "dashboard/index.html",
        stats={"noticias": 5, "eventos": 3, "galeria": 12}
    )

if __name__ == "__main__":
    import webbrowser
    webbrowser.open("http://127.0.0.1:5050")
    app.run(debug=True, port=5050)
