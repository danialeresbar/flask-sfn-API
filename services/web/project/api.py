from flask import Flask


app = Flask(__name__)
app.config.from_object('project.config.Config')


@app.route("/", methods=["GET"])
def home():
    return """
    <h1>Distant Reading Archive</h1>
    <p>This site is a prototype API for distant reading of science fiction novels.</p>
    """
