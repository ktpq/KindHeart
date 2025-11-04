# ใช้ Python base image
FROM python:3.12-slim

# ตั้ง working directory ใน container
WORKDIR /app

# คัดลอก requirements.txt และติดตั้ง dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกโค้ดทั้งหมดเข้า container
COPY . .

# เปลี่ยน working directory ไปยังที่มี manage.py
WORKDIR /app/myproject

# เปิดพอร์ต 8000
EXPOSE 8000

# คำสั่งรัน Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
