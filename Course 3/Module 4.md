1. Mục tiêu. 

    - Mở rộng các thuật toán TD control (như Sarsa, Q-learning) sang môi trường có không gian trạng thái liên tục hoặc rất lớn bằng cách sử dụng function approximation (hàm xấp xỉ).

   - Hiểu cách áp dụng Generalized Policy Iteration (GPI) kết hợp với semi-gradient TD để học chính sách tối ưu.

    - Khám phá thêm một cách mô hình hóa bài toán RL thông qua Average Reward, phù hợp với môi trường liên tục lâu dài

2. Nội dung chính 
    2.1 Episodic Sarsa với Function Approximation
        - Triển khai Sarsa trong môi trường liên tục như Mountain Car.

        - Sử dụng function approximation (ví dụ: linear hoặc mạng nơ‑ron) để xấp xỉ hàm Q.

        - Cập nhật trọng số sử dụng công thức semi-gradient dựa trên hành động thực tế đã chọn
    
    2.2 Expected Sarsa với Function Approximation
        - Sử dụng Expected Sarsa: cập nhật Q(s,a) dựa vào kỳ vọng theo chính sách thay vì max hoặc thực hiện, giúp giảm độ phương sai.

        - Giúp học chính sách ổn định hơn đặc biệt khi sử dụng hàm xấp xỉ.

    2.3 Khám phá (Exploration) trong môi trường Approximation
        - Thảo luận cách thiết kế chiến lược khám phá khi hàm Q là xấp xỉ.

        - Xử lý hiện tượng generalization lan truyền sai: cập nhật trong một vùng nhỏ ảnh hưởng rộng trong không gian trạng thái.

        - Cần lựa chọn hợp lý epsilon‑greedy, hành vi ngẫu nhiên, hoặcIntrinsic Rewards để cải thiện khám phá.
    
    2.4 Average Reward Formulation
        - Thay thế chiết khấu γ<1 bằng average reward per time-step để tối ưu trong môi trường không kết thúc rõ (continuing tasks).
        - Mở rộng khái niệm control để thích nghi với các hệ thống dài hạn như kiểm soát robot hoặc hệ thống tự động.

3. Kết luận.
    - Module 4 là bước then chốt, nối liền giữa lý thuyết và ứng dụng. Giúp chúng ta học cách sử dụng function approximation để chạy được các thuật toán TD control trong môi trường phức tạp, đồng thời nắm được chiến lược khai thác-khám phá hợp lý và mô hình hóa bài toán bằng average reward nếu cần.

