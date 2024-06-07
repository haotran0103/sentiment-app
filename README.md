# Text Sentiments

![Text Sentiments](https://your-image-url.com/banner.png)

Text Sentiments là một ứng dụng phân tích cảm xúc sử dụng mô hình học sâu dựa trên `DistilBERT`. Ứng dụng này cho phép bạn dự đoán cảm xúc của một đoạn văn bản là tích cực hay tiêu cực.

## Giới thiệu

Ứng dụng này sử dụng mô hình `DistilBERT` để phân loại cảm xúc của văn bản. Mô hình được huấn luyện trên tập dữ liệu IMDB và được triển khai sử dụng FastAPI.

![Sentiment Analysis](https://your-image-url.com/sentiment_analysis.png)

## Cài đặt

### Yêu cầu

- Docker
- Python 3.8+

### Cài đặt môi trường

1. Sao chép repository:

   ```bash
   git clone https://github.com/yourusername/textSentiments.git
   cd textSentiments
Download và Giải nén Model

Đầu tiên, bạn cần tải xuống tệp model từ Google Drive. Vui lòng truy cập vào đường dẫn này để tải xuống tệp model.

Sau khi tải xuống, bạn cần giải nén tệp model và đặt nó vào thư mục models/ trong dự án của bạn.

Build Docker Image và Run Container

Tiếp theo, bạn cần xây dựng hình ảnh Docker và chạy container:

bash
Copy code
docker build -t text-sentiments:latest .
docker run -d --name text-sentiments-container -p 8000:8000 text-sentiments:latest
Model Training
Nếu bạn muốn huấn luyện lại mô hình, bạn có thể sử dụng Google Colab hoặc chạy trực tiếp trong dự án:

Using Google Colab
Link tới Google Colab Notebook

Using the Train Pipeline
bash
Copy code
python src/textSentiments/pipeline/train_pipeline.py
Application Deployment
Ứng dụng được triển khai bằng FastAPI và có thể truy cập tại http://localhost:8000.

API Endpoint
POST /predict: Dự đoán cảm xúc của một đoạn văn bản được cung cấp.

Testing the API
Bạn có thể kiểm tra API bằng cách sử dụng curl, Postman, hoặc FastAPI's Swagger UI.

Sử dụng curl:

bash
Copy code
curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"text": "I love this movie! It was fantastic."}'
Sử dụng Postman:

Mở Postman và tạo một yêu cầu mới với phương thức POST.
URL: http://localhost:8000/predict
Headers: Content-Type: application/json
Body: {"text": "I love this movie! It was fantastic."}
Gửi yêu cầu và quan sát phản hồi.