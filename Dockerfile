FROM python:3.8-slim

WORKDIR /app

COPY . /app

CMD ["python", "my_solution.py", "testdata.txt", "2"]
