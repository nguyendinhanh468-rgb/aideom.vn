# AIDEOM-VN — AI-Driven Decision Optimization Model for Vietnam

Web app giải 12 bài toán mô hình ra quyết định phát triển kinh tế Việt Nam.

## Cài đặt & chạy

```bash
# 1. Tạo môi trường ảo
python -m venv venv

# 2. Kích hoạt (Windows)
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 3. Cài thư viện
pip install -r requirements.txt

# 4. Chạy app
streamlit run app.py
```

Trình duyệt tự mở http://localhost:8501

## Cấu trúc

```
aideom_vn/
├── app.py                    # Trang chủ + sidebar
├── pages/
│   ├── 01_Cobb_Douglas.py    # Bài 1
│   ├── 02_LP_Ngan_Sach.py    # Bài 2
│   └── ...                   # Bài 3-12
├── data/
│   ├── vietnam_macro_2020_2025.csv
│   ├── vietnam_sectors_2024.csv
│   └── vietnam_regions_2024.csv
├── utils/
│   ├── data_loader.py
│   └── ai_analyst.py
└── requirements.txt
```

## AI Analyst

Nhập Anthropic API key vào sidebar để kích hoạt tính năng phân tích kết quả tự động.
Lấy key tại: https://console.anthropic.com
