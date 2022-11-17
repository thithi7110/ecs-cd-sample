FROM python:3.9

#RUN pip install fastapi uvicorn


# EXPOSE 80

COPY ./src /src
COPY ./requirements.txt /src
# RUN ls -la ./src
RUN pip install -r /src/requirements.txt
WORKDIR /src
CMD ["python", "app.py"]
# CMD ["uvicorn", "app:api", "--host", "0.0.0.0", "--port", "80"]
# FastAPIを8000ポートで待機
# CMD ["uvicorn", "app:api", "--reload", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["python", "app.py"]
