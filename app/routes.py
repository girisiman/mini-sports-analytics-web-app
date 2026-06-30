"""
Application Routes

This module defines the URL routes for the Mini Sports Analytics Web App.
Each route renders a corresponding HTML template.
"""

from flask import Blueprint, render_template

# Create a Blueprint
main = Blueprint("main", __name__)


@main.route("/")
def home():
    """
    Home page.
    
    """
    return render_template("index.html")
    


@main.route("/preprocessing")
def preprocessing():
    """
    Data preprocessing page.
    """
    return render_template("preprocessing.html")


@main.route("/eda")
def eda():
    """
    Exploratory Data Analysis (EDA) page.
    """
    return render_template("eda.html")


@main.route("/visualizations")
def visualizations():
    """
    Data visualization page.
    """
    return render_template("visualization.html")


@main.route("/statistics")
def statistics():
    """
    Statistical analysis page.
    """
    return render_template("statistics.html")


@main.route("/about")
def about():
    """
    About the project.
    """
    return render_template("about.html")