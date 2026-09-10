from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Azure Container Apps</title>
        </head>

        <body style="font-family: Arial; text-align: center; margin-top: 100px;">

            <h1>Hello Azure Container Apps!</h1>

            <p>My first serverless container application.</p>

        </body>
    </html>
    """


@app.route("/health")
def health():
    return {
        "status": "healthy"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)