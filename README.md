# 🇻🇳 AIDEOM-VN
**AI-Driven Decision Optimization Model for Vietnam**

Hệ thống 12 bài toán mô hình ra quyết định phát triển kinh tế Việt Nam trong kỷ nguyên AI.

---

## ⚡ Cài đặt nhanh

### Yêu cầu
- Python 3.10 hoặc 3.11
- Terminal (macOS/Linux) hoặc PowerShell (Windows)

### Các bước

**1. Tải về**
```bash
git clone https://github.com/tên-của-bạn/aideom-vn.git
cd aideom_vn
```

**2. Tạo môi trường ảo**
```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\Activate.ps1
```

**3. Cài thư viện**
```bash
pip install -r requirements.txt
```

**4. Chạy app**
```bash
streamlit run app.py
```

Trình duyệt tự mở tại `http://localhost:8501` 🎉

---

## 🤖 Dùng AI Analyst (Groq)

1. Lấy API key **miễn phí** tại [console.groq.com](https://console.groq.com)
2. Đăng nhập → Create API Key → Copy key
3. Dán vào ô **Groq API Key** ở sidebar trái
4. Vào từng bài toán → nhấn **✨ Phân tích kết quả** hoặc **💬 Câu hỏi thảo luận**

---

## 📁 Cấu trúc thư mục

```
aideom_vn/
├── app.py                  # Trang chủ
├── pages/                  # 12 bài toán
│   ├── 01_Cobb_Douglas.py
│   ├── 02_LP_Ngan_Sach.py
│   └── ...
├── utils/
│   ├── ai_analyst.py       # AI phân tích (Groq)
│   └── data_loader.py      # Đọc dữ liệu
├── data/                   # File CSV dữ liệu Việt Nam
│   ├── vietnam_macro_2020_2025.csv
│   ├── vietnam_sectors_2024.csv
│   └── vietnam_regions_2024.csv
├── requirements.txt
└── README.md
```

---

## 📦 Thư viện chính

| Thư viện | Dùng cho |
|----------|----------|
| streamlit | Dashboard |
| numpy, pandas | Tính toán |
| plotly | Biểu đồ |
| scipy | Tối ưu hóa |
| pulp | Linear Programming |
| pymoo | NSGA-II Pareto |
| cvxpy | Convex optimization |
| groq | AI Analyst |

---

## ❓ Lỗi thường gặp

**`command not found: streamlit`**
```bash
source venv/bin/activate  # kích hoạt môi trường ảo trước
streamlit run app.py
```

**`ModuleNotFoundError`**
```bash
pip install -r requirements.txt
```

**AI không hoạt động**
→ Kiểm tra đã nhập Groq API key ở sidebar chưa (key bắt đầu bằng `gsk_...`)
