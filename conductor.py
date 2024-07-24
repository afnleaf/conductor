from flask import Flask, request
import subprocess

app = Flask(__name__)
port = 9000

@app.route("/paleomap3d", methods=["POST"])
def webhook():
    if request.method == "POST":
        if request.json["ref"] == "refs/heads/main":
            subprocess.call(["/home/x230/prod/paleomap3d/deployprod.sh"])
            return "Deployment triggered", 200
    return "OK", 200

# add other routes here

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
    print(f"listening on port {port}")