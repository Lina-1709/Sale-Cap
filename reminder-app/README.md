# Nhắc Việc Hằng Ngày

Web app (PWA) nhắc lịch làm việc, uống nước, uống thuốc. Không cần build, dữ liệu lưu trong trình duyệt (localStorage).

## Chạy thử
```
cd reminder-app && python3 -m http.server 8000
```
Mở http://localhost:8000 → bấm "Bật thông báo". Trên điện thoại: "Thêm vào màn hình chính".

## Giới hạn hiện tại
Nhắc bằng timer trong trình duyệt: phải mở app/tab (có thể thu nhỏ) thì mới nhắc đúng giờ. Muốn nhắc khi tắt hẳn app cần thêm backend + Web Push, hoặc app native.
