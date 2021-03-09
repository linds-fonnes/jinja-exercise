from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-secret-secret"

debug = DebugToolbarExtension(app)

@app.route("/")
def show_form():
    """Home page shows form pront to add words to story"""
    prompts = story.prompts
    return render_template("form_page.html", prompts=prompts)

@app.route("/story")
def show_story():
    """Shows story based off of form input"""
    words = story.generate(request.args)
    return render_template("story.html", words=words)
