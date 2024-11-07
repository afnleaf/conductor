import logging
import os
import subprocess
import time
from flask import Flask, request
#from functools import wraps

app = Flask(__name__)
port = 9000

#print(os.getcwd())
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="webhook_deployment.log"
)
logger = logging.getLogger(__name__)

def execute_script(script_path):
    result = subprocess.run(
        f"/bin/bash {script_path}",
        shell=True,
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        raise Exception(f"Deployment of {script_path} failed: {result.stderr}")
    return result

# add routes here

# paleomap3d
@app.route("/paleomap3d", methods=["POST"])
def paleomap3d_webhook():
    if request.method == "POST":
        try:

            if request.json["ref"] == "refs/heads/main":
                script_path ="/home/x230/prod/paleomap3d/deployprod.sh"
                result = execute_script(script_path)
                logger.info("Paleomap3d deployment successful")
                return "Deployment triggered on paleomap3d", 200
            else:
                return "Non main branch", 200
        except Exception as e:
            logger.error(f"Paleomap3d deployment error: {str(e)}")
            raise
    return "Method not allowed", 405

# weblock
@app.route("/weblock", methods=["POST"])
def weblock_webhook():
    if request.method == "POST":
        try:
            if request.json["ref"] == "refs/heads/main":
                script_path ="/home/x230/prod/weblock/deployprod.sh"
                result = execute_script(script_path)
                logger.info("Paleomap3d deployment successful")
                return "Deployment triggered on weblock", 200
            else:
                return "Non main branch", 200
        except Exception as e:
            logger.error(f"Paleomap3d deployment error: {str(e)}")
            raise
    return "Method not allowed", 405

## Pharahobs Bot
#@app.route("/replaycode", methods=["POST"])
#def webhook():
#    if request.method == "POST":
#        if request.json["ref"] == "refs/heads/main":
#            #subprocess.call(["~/prod/paleomap3d/deployprod.sh"], shell=True)
#            subprocess.run("", shell=True)
#            return "Deployment triggered on replaycode-ocr", 200
#        else:
#            return "Non main branch", 200
#        return "OK", 200
#    else:
#        return "NO", 200


if __name__ == "__main__":
    print(f"listening on port {port}")
    logger.info(f"Server started on {port}")
    app.run(host="0.0.0.0", port=port)
    
