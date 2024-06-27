from flask import Flask, render_template, request

app = Flask(__name__)

lista_productos = [
    dict(
        nombre = "auriculares",
        categoria = "electrónica"
    ),
    dict(
        nombre = "camiseta",
        categoria = "ropa"
    ),
    dict(
        nombre = "cafetera",
        categoria = "electrodoméstico"
    )
]

@app.route("/")
def bienvenida():
    return render_template(
        'index.html'
    )

@app.route("/product")
def producto():
    return render_template(
        'productos.html',
        lista = lista_productos
    )


@app.route("/add_product", methods = ["POST", "GET"])
def add_product():
    if request.method == "POST":
        nombre_post = request.form['name']
        categoria_post = request.form['class']
        lista_productos.append(dict(
            nombre = nombre_post,
            categoria = categoria_post
        ))
    return render_template(
        'agregar_productos.html'

    )




