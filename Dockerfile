FROM tiangolo/uvicorn-gunicorn:python3.7

COPY ./app /app
cmd pip install -r req.txt
cmd cd app
cmd python3 main:app
