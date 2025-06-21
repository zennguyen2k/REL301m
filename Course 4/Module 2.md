1. Mục tiêu: 

    - Chuyển một bài toán thực tế thành Markov Decision Process (MDP) đầy đủ.

    - Xây dựng môi trường mô phỏng dựa trên định nghĩa MDP cho dự án capstone.

    - Phục vụ như nền tảng để chọn thuật toán và triển khai agent trong các module sau.

2. Nội dung chính:
 
    - Ôn tập về MDP: Nhắc lại thành phần của MDP – trạng thái, hành động, xác suất chuyển tiếp, phần thưởng, chiết khấu.

    - Ví dụ về Episodic vs Continuing Giúp phân biệt 2 loại task khác nhau mà bạn sẽ quyết định khi mô hình hóa.

    - Programming Assignment: "MoonShot Technologies" Bài tập code chính – hoàn chỉnh môi trường MDP từ skeleton để chuẩn bị cho training agent. Cần:

        + Xác định state space, action space, reward và transition dynamics.

        + Cài đặt điều kiện dừng (terminal states) nếu là bài toán episodic.

3. Kết luận.

    - Hạ tầng MDP là cốt lõi: Không chỉ là lý thuyết, phải code ra môi trường để agent tương tác.

    - Bài tập thực hành chi tiết: Giúp hiểu sâu mô tả bài toán, định nghĩa state/action rõ ràng, xác suất và phần thưởng, và đặc tả các task theo từng loại môi trường.

    - Chuẩn bị cho các bước tiếp theo: Một MDP đúng đắn là nền tảng để chọn Expected Sarsa, Q-learning, hoặc Actor‑Critic trong các milestone tiếp theo.