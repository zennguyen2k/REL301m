# Mục tiêu: 
- Hiểu khái niệm về quyết định tuần tự trong học tăng cường.
- Khám phá bài toán K-armed bandit và tầm quan trọng của việc cân bằng giữa khám phá và khai thác.
- Áp dụng các thuật toán đơn giản để ước lượng giá trị hành động và lựa chọn hành động.

- Nội dung chính: 
1. Bài toán K-armed Bandit
Mô hình hóa tình huống mà một tác nhân phải chọn giữa nhiều hành động (cánh tay của máy đánh bạc), mỗi hành động mang lại phần thưởng ngẫu nhiên.
Mục tiêu là tối đa hóa tổng phần thưởng nhận được qua thời gian bằng cách học giá trị kỳ vọng của từng hành động.

2. Ước lượng giá trị hành động
Sử dụng phương pháp cập nhật gia tăng để ước lượng giá trị kỳ vọng của mỗi hành động dựa trên phần thưởng nhận được.
Công thức: Qn+1 = Qn + alpha(Rn - Qn)
trong đó : Qn là ước lượng hiện tại của giá trị hành động.
           Rn là phần thưởng nhận được sau lần chọn hành động thứ n. 
           Alpha là tốc độ học (learning rate).

3. Chiến lược khám phá-khai thác
Epsilon-greedy: Với xác suất $\epsilon$, chọn hành động ngẫu nhiên (khám phá); với xác suất $1 - \epsilon$, chọn hành động có giá trị ước lượng cao nhất (khai thác).
Softmax: Gán xác suất chọn hành động dựa trên giá trị ước lượng của chúng, cho phép cân bằng tốt hơn giữa khám phá và khai thác. 

- Điểm quan trọng: 
Khám phá giúp tác nhân tìm hiểu về môi trường, trong khi khai thác giúp tận dụng kiến thức hiện có để tối đa hóa phần thưởng.

Cân bằng giữa khám phá và khai thác là yếu tố then chốt trong học tăng cường.

Các thuật toán đơn giản như epsilon-greedy cung cấp nền tảng cho các phương pháp học tăng cường phức tạp hơn.
