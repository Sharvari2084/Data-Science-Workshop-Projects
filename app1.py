from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

# Load the trained model
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "linear.pkl")

with open(file_path, "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None  # Default value

    if request.method == "POST":
        try:
            tv = float(request.form["tv"])
            radio = float(request.form["radio"])
            news = float(request.form["news"])

            # Predict using the model
            prediction = model.predict([[tv, radio, news]])[0]
        except Exception as e:
            prediction = f"Error: {e}"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
