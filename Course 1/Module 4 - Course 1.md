Nội dung chính 
1. Lập trình Động trong MDP
DP sử dụng phương trình Bellman để tính toán chính xác hàm giá trị và chính sách tối ưu khi biết mô hình đầy đủ của môi trường (tức là biết xác suất chuyển trạng thái và phần thưởng).
2. Thuật toán Policy Iteration
Bao gồm hai bước lặp lại:
Đánh giá chính sách (Policy Evaluation): Tính toán hàm giá trị $V^\pi(s)$ cho chính sách hiện tại $\pi$.
Cải thiện chính sách (Policy Improvement): Cập nhật chính sách bằng cách chọn hành động tối ưu dựa trên hàm giá trị đã tính.
Lặp lại hai bước trên cho đến khi chính sách hội tụ.
3. Thuật toán Value Iteration
Kết hợp đánh giá và cải thiện chính sách trong một bước duy nhất bằng cách cập nhật hàm giá trị theo công thức
Tiếp tục cập nhật cho đến khi hàm giá trị hội tụ.
4. Generalized Policy Iteration (GPI)
GPI là khuôn khổ tổng quát mô tả sự tương tác giữa đánh giá và cải thiện chính sách.
Nhiều thuật toán học tăng cường, bao gồm cả DP và các phương pháp học dựa trên mẫu, đều tuân theo khuôn khổ GPI.
Kết luận: 
Lập trình Động yêu cầu biết mô hình đầy đủ của môi trường, điều này không phải lúc nào cũng khả thi trong thực tế.

Value Iteration thường hội tụ nhanh hơn nhưng mỗi bước tính toán có thể tốn kém hơn so với Policy Iteration.

GPI cung cấp một khuôn khổ linh hoạt cho việc phát triển các thuật toán học tăng cường hiệu quả.
