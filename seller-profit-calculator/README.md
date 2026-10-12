# Máy tính lãi thật cho Seller (MVP)

Web app một file (`index.html`), không cần build. Mở trực tiếp bằng trình duyệt hoặc chạy `npx serve seller-profit-calculator`.

## Làm gì
- Nhập giá bán, giá vốn, đóng gói, ship, voucher, quảng cáo, tỷ lệ hoàn, thuế.
- Ra: lãi ròng/đơn, biên lãi, giá hòa vốn, giá để đạt biên mục tiêu, lãi tháng ước tính.
- So sánh nhiều bảng phí (Shopee / TikTok Shop / Lazada / tự thêm) trên cùng một sản phẩm.
- Bảng phí sửa được, lưu trong localStorage, xuất/nhập JSON.

## Mô hình tính (kỳ vọng mỗi đơn đặt)
`w = 1 - tỷ lệ hoàn`.
Lãi = w·P − w·[P·(hoa hồng + thanh toán + phí khác + voucher CT + voucher seller + ads + thuế) + phí cố định + giá vốn + ship + đóng gói] − r·thiệt hại/đơn hoàn.

Giả định (cần validate): phí % của sàn được hoàn khi đơn hoàn/hủy; quảng cáo tính trên đơn thành công; thuế tính trên doanh thu đơn thành công.

## Dữ liệu phí mặc định
| Trạng thái | Nội dung |
|---|---|
| Có nguồn báo chí 5/2026 | TikTok Shop thời trang hoa hồng ~16%; Lazada xử lý đơn 6% + 3.000đ/đơn; Shopee thanh toán ~6%, duy trì hiển thị ≥1% |
| Chưa có nguồn (mặc định 0, viền cam) | Hoa hồng Shopee/Lazada theo ngành; phí thanh toán TikTok Shop |

Phải đối chiếu với Seller Center trước khi dùng cho quyết định giá. Kết quả của bảng phí còn ô "cần nhập" sẽ bị **lạc quan hơn thực tế**.

## Bước tiếp theo gợi ý
1. Preset hoa hồng theo ngành hàng cho từng sàn (sau khi xác minh).
2. Upload file đơn hàng từ Seller Center → báo cáo lãi/lỗ theo SKU và đối soát phí.
3. Validate với 5 seller thật trước khi thêm tính năng trả phí.
