# ใช้ base image ของ Python 3.9
FROM python:3.9-slim

# กำหนด directory ใน container
WORKDIR /app

# คัดลอกไฟล์ทั้งหมดจากโปรเจคไปยัง container
COPY . .

# ติดตั้ง dependencies (หากมี requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# รัน Unit Test
CMD ["python", "-m", "unittest", "discover", "-s", ".", "-p", "test_my_solution.py"]
