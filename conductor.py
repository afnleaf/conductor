from flask import Flask, request
import subprocess
import os

app = Flask(__name__)
port = 9000

print(os.getcwd())

@app.route("/paleomap3d", methods=["POST"])
def webhook():
    if request.method == "POST":
        if request.json["ref"] == "refs/heads/main":
            #subprocess.call(["~/prod/paleomap3d/deployprod.sh"], shell=True)
            subprocess.run("/bin/bash /home/x230/prod/paleomap3d/deployprod.sh", shell=True)
            return "Deployment triggered", 200
        else:
            return "Non main branch", 200
        return "OK", 200
    else:
        return "NO", 200

# add other routes here

if __name__ == "__main__":
    print(f"listening on port {port}")
    app.run(host="0.0.0.0", port=port)
    
