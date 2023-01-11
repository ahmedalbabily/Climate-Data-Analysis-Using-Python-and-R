from flask import Flask, render_template
from bokeh.embed import server_document
from bokeh.server.server import Server
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure
from bokeh.themes import Theme


app = Flask(__name__, template_folder=".")
def create_figure():
    plot = figure()
    plot.circle([1, 2, 3], [4, 5, 6])
    return plot

figure = create_figure()

@app.route("/")
def index():
    script = server_document('http://localhost:39703/bkapp')
    return render_template("index.html", script=script, template="Flask")


if __name__ == '__main__':
    app.run()

