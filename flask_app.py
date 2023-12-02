from flask import Flask, render_template
app = Flask(__name__)
items = [{"product": "vanille ijs 1 liter",
          "prijs": "2 euro"}, {"product": "chocolade-ijs 1 liter","prijs": "2 euro"}]

@app.route('/')
    
def home():
    return render_template("home.html",)
@app.route("/recepten")
def recepten():
    receptenn=[{"recept": "Tiramisu di nona","img": "tiramisu.png"}, 
    {"recept": "IJstaart met chocolade","img": "ijstaart.png"}]
    return render_template("recepten.html", items = receptenn)
@app.route("/prijzen")
def prijven():
    return render_template("prijzen.html", items=items)
if __name__=="__main__":

    app.run(port=5000,debug=True)