from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",env_vars=dict(os.environ),greetcolour=(os.environ.get("color") or "red"))

if __name__ == "__main__":
     if os.path.exists("certs/tls.crt") and os.path.exists("certs/tls.key"):
       print("Certificate Found!! Starting Secure Connection...on port 8443")
       app.run(debug=True,host='0.0.0.0',port=8443,ssl_context=("certs/tls.crt", "certs/tls.key"))
     else:
       print("Certificate Not Found!! Communicating insecurely on port 5000")
       app.run(debug=True,host='0.0.0.0',port=5000)
