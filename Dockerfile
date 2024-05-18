# Sử dụng Python base image
FROM python:3.9-slim

# Đặt thư mục làm việc trong container
WORKDIR /app

# Copy file requirements.txt vào container
COPY requirements.txt requirements.txt

# Cài đặt các thư viện cần thiết
RUN pip install -r requirements.txt

# Copy tất cả các file của ứng dụng vào container
COPY . .

# Tạo thư mục để lưu trữ file tải lên
RUN mkdir uploads

# Expose port mà ứng dụng Flask sẽ chạy
EXPOSE 5000

# Khởi chạy ứng dụng Flask
CMD ["python", "app.py"]
