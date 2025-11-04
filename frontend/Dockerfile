# Dockerfile
FROM node:20-alpine

WORKDIR /app

# ติดตั้ง dependencies
COPY package*.json ./
RUN npm install

# คัดลอกโค้ดสำรอง (dev จะใช้ mount source code)
# COPY . .

# เปิด port 5173
EXPOSE 5173

# รัน dev server ที่ทุก interface และใช้ polling สำหรับ Docker
CMD ["npm", "run", "dev", "--", "--host"]
