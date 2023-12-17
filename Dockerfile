FROM python:3.10-slim-buster
WORKDIR /app
COPY model.pkl model.pkl
COPY pred_func.py pred_func.py
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD [ "python", "pred_func.py" ]