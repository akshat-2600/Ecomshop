from flask  import Flask , render_template , request
import requests

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/products")
def products():
    return render_template("products.html")


@app.route("/productsdetails")
def product_details():
    return render_template("productsdetails.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0" , port=8888 , debug=True)