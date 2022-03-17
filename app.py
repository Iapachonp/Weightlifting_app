from flask import Flask, render_template

from WeightLifter import WeightLifter
app = Flask(__name__)

@app.route("/")
def hello():
  return render_template('index.html')

if __name__ == "__main__":
  app.run()