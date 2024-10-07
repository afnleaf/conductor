from flask import Flask, request
import subprocess
import os

app = Flask(__name__)
port = 9000

print(os.getcwd())

# add routes here

# paleomap3d
@app.route("/paleomap3d", methods=["POST"])
def paleomap3d_webhook():
    if request.method == "POST":
        if request.json["ref"] == "refs/heads/main":
            #subprocess.call(["~/prod/paleomap3d/deployprod.sh"], shell=True)
            subprocess.run("/bin/bash /home/x230/prod/paleomap3d/deployprod.sh", shell=True)
            return "Deployment triggered on paleomap3d", 200
        else:
            return "Non main branch", 200
        return "OK", 200
    else:
        return "NO", 200


# weblock
@app.route("/weblock", methods=["POST"])
def weblock_webhook():
    if request.method == "POST":
        if request.json["ref"] == "refs/heads/main":
            subprocess.run("/bin/bash /home/x230/prod/weblock/deployprod.sh", shell=True)
            return "Deployment triggered on weblock", 200
        else:
            return "Non main branch", 200
        return "OK", 200
    else:
        return "NO", 200


'''
# Pharahobs Bot
@app.route("/replaycode", methods=["POST"])
def webhook():
    if request.method == "POST":
        if request.json["ref"] == "refs/heads/main":
            #subprocess.call(["~/prod/paleomap3d/deployprod.sh"], shell=True)
            subprocess.run("", shell=True)
            return "Deployment triggered on replaycode-ocr", 200
        else:
            return "Non main branch", 200
        return "OK", 200
    else:
        return "NO", 200
'''

if __name__ == "__main__":
    print(f"listening on port {port}")
    app.run(host="0.0.0.0", port=port)
    
