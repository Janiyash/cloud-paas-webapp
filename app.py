from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cloud PaaS Web Application</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #eaf0f6;
                padding: 50px;
                text-align: center;
            }
            .card {
                max-width: 500px;
                margin: auto;
                background: #ffffff;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.15);
            }
            h1 { color: #1f5a8a; }
            .status {
                display: inline-block;
                background: #d4f5dd;
                color: #1a7a3a;
                padding: 8px 16px;
                border-radius: 20px;
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Cloud PaaS Web Application</h1>
            <p>Welcome to my Cloud Computing Lab Practical 5.</p>
            <p>This web application is developed using Python and Flask.</p>
            <p>It is deployed using Platform as a Service (PaaS).</p>
            <div class="status">Application is running!</div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
