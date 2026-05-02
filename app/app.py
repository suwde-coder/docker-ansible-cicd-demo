from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Sayfada gösterilecek sade ve şık HTML içeriği
    html_content = """
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DevOps Projesi</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f4f7f6;
            }
            .container {
                text-align: center;
                background: white;
                padding: 3rem 4rem;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            }
            h1 {
                color: #2c3e50;
                margin: 0 0 10px 0;
                font-size: 2.2rem;
            }
            p {
                color: #7f8c8d;
                font-size: 1.2rem;
                margin: 0;
                font-weight: 500;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 CI/CD ile deploy edildi!</h1>
            <p>Docker + Ansible + GitHub Actions</p>
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    # Flask uygulamasını tüm IP'lerden erişilebilir (0.0.0.0) ve 5000 portunda başlatır
    app.run(host='0.0.0.0', port=5000)
