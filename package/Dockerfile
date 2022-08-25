from python:3.8.12-buster

copy api/app.py /home/app.py
copy requirements.txt /home/requirements.txt

run pip install -U pip
run pip install -r /home/requirements.txt

cmd uvicorn home.app:app --host 0.0.0.0 --port $PORT
