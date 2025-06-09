- Mục tiêu:

  Tìm hiểu cách kết hợp kế hoạch (planning) dựa trên mô hình đã học và học từ trải nghiệm thực tế (learning) để cải thiện hiệu suất một cách hiệu quả.
  Cụ thể là học về kiến trúc Dyna: sử dụng mô hình môi trường kết hợp với Temporal Difference (TD) để tạo ra cả kinh nghiệm thật và giả (simulated).
  
- Nội dung chính:

1. Khác biệt giữa học với và không có mô hình

Đã học qua Dynamic Programming (cần mô hình) và Sample-Based Methods (không cần mô hình).
Module này giúp hiểu cách kết hợp hai hướng ấy: vừa học từ kinh nghiệm thực, vừa khai thác mô hình tạm thời để tăng tốc.

2. Giới thiệu kiến trúc 

Thu thập trải nghiệm thực: Quan sát các cặp trạng thái → hành động → phần thưởng → trạng thái kế tiếp.

Học mô hình (model learning): Ước lượng xác suất chuyển trạng thái và phần thưởng từ dữ liệu thật.

Kế hoạch (planning): Sử dụng mô hình ước lượng để mô phỏng tiếp trải nghiệm giả — chạy TD-update trên “trải nghiệm của trí tưởng tượng”.

Cập nhật chính sách: Kết hợp giữa học từ trải nghiệm thật và giả để cải thiện chính sách. 

3. Ưu điểm của kiến trúc Dyna

Tăng hiệu quả về dữ liệu (sample efficiency): Thu thập ít dữ liệu thực nhưng khai thác nhiều hơn thông qua mô phỏng.

Linh hoạt: Có thể khai thác mô hình ngay cả khi chưa hoàn thiện.

Ứng dụng mở rộng: Người học có thể thử nghiệm trong môi trường giả để kiểm tra tác động của thay đổi trước khi dùng với môi trường thật.

- Kết luận: Module 4 mang đến một hướng tiếp cận toàn diện: không chỉ học từ “trải nghiệm thật” mà còn tạo trải nghiệm giả từ mô hình để nâng cao năng lực của tác tử một cách hiệu quả về dữ liệu và thời gian.
