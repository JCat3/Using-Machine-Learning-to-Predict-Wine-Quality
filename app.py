from flask import Flask, render_template
import pickle
import pandas as pd

app = Flask(__name__)

X_red_scaler = pickle.load( open( "X_red_scaler.pkl", "rb" ) )
rf_red = pickle.load( open( "rf_red.pkl", "rb" ) )


@app.route("/")
def index():

    return render_template("index.html")

@app.route("/random_forest")
def random_forest():
    dictionary = {}

    return render_template("random_forest.html", data= dictionary)

# route to accept information from webpage
@app.route("/form", methods=["POST"])
def form():
    if request.method == "POST":
        fixed_acidity = float(request.form["fixed_acidity"])
        volatile_acidity = float(request.form["volatile_acidity"])
        citric_acid = float(request.form["citric_acid"])
        residual_sugar = float(request.form["residual_sugar"])
        chlorides = float(request.form["chlorides"])
        free_sulfur_dioxide = float(request.form["free_sulfur_dioxide"])
        total_sulfur_dioxide = float(request.form["total_sulfur_dioxide"])
        density = float(request.form["density"])
        ph = float(request.form["ph"])
        sulphates = float(request.form["sulphates"])
        alcohol = float(request.form["alcohol"])

        dictionary = {"fixed_acidity": fixed_acidity,
                      "volatile_acidity": volatile_acidity,
                      "citric_acid": citric_acid,
                      "residual_sugar": residual_sugar,
                      "chlorides": chlorides,
                      "free_sulfur_dioxide": free_sulfur_dioxide,
                      "total_sulfur_dioxide":total_sulfur_dioxide,
                      "density": density,
                      "ph": ph,
                      "sulphates": sulphates,
                      "alcohol": alcohol }

        df = pd.DataFrame(dictionary, index= 0)

                    


    return render_template("random_forest.html", data= dictionary)

if __name__== "__main__":
    app.debug = True
    app.run(use_reloader=False)

