from fastapi import FastAPI

app = FastAPI()


@app.get("/dodeploy/settraces/{secretKey}")
def read_root(secretKey):
    try:
        envKey = open("envKey.secret", "r").read().strip()
    except:
        return 404
    if secretKey == envKey:
        try:
            exec("deployment.sh")
        except:
            return {"failed":"file failed"}
        return {"Application": "Deployd"}

    return 404
