from fastapi import FastAPI
import os
app = FastAPI()


@app.get("/dodeploy/settraces/{secretKey}")
def read_root(secretKey):
    try:
        envKey = open("envKey.secret", "r").read().strip()
    except:
        return 404
    if secretKey == envKey:
        try:
            os.system("./deployment.sh")
        except Exception as e:
            print(e)
            return {"failed":"file failed"}
        return {"Application": "Deployd"}

    return 404
