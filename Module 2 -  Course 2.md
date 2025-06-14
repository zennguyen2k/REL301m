- Mục tiêu: 
Hiểu khái niệm và cơ chế hoạt động của Temporal Difference (TD) Learning.

So sánh TD Learning với Monte Carlo và Dynamic Programming.

Áp dụng TD Learning để ước lượng hàm giá trị trạng thái V(s) cho một chính sách cố định.

Thực hành triển khai thuật toán TD(0) trong môi trường mô phỏng. 

- Nội dung chính: 
1. Giới thiệu về Temporal Difference (TD) Learning
TD Learning là phương pháp học tăng cường không cần mô hình môi trường, học từ trải nghiệm thực tế của tác nhân.

Kết hợp ưu điểm của Monte Carlo (học từ trải nghiệm) và Dynamic Programming (cập nhật giá trị dựa trên ước lượng hiện tại).

Khả năng học trực tuyến (online learning), không cần chờ đến cuối mỗi tập (episode) như Monte Carlo.
2. Thuật toán TD(0) cho Dự đoán
TD(0) là phiên bản đơn giản nhất của TD Learning, cập nhật giá trị trạng thái sau mỗi bước: ![image](https://github.com/user-attachments/assets/aa2569bd-5d2d-47f7-9814-afa596efaf0d)

3. So sánh TD Learning với Monte Carlo và Dynamic Programming
a/ TD vs. Monte Carlo:
TD cập nhật giá trị sau mỗi bước, trong khi Monte Carlo cần chờ đến cuối tập.
TD có thể học hiệu quả hơn trong các môi trường dài hoặc không có điểm kết thúc rõ ràng.
b/ TD vs. Dynamic Programming:
TD không yêu cầu kiến thức về mô hình môi trường, trong khi Dynamic Programming cần biết xác suất chuyển trạng thái và phần thưởng.
TD phù hợp với các môi trường phức tạp hoặc không xác định.
4. Thực hành: Ước lượng Hàm Giá trị với TD(0)
Triển khai thuật toán TD(0) để ước lượng hàm giá trị trạng thái cho một chính sách cố định trong môi trường mô phỏng.
So sánh kết quả với phương pháp Monte Carlo để đánh giá hiệu quả.

- Kết luận: 
TD Learning cho phép cập nhật giá trị trạng thái một cách liên tục và hiệu quả hơn so với Monte Carlo.

Không cần kiến thức về mô hình môi trường, phù hợp với các tình huống thực tế.

Là nền tảng cho các thuật toán học tăng cường nâng cao như Sarsa, Q-learning, và Expected Sarsa.

