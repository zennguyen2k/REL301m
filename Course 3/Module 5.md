1. Mục tiêu
    - Tìm hiểu các phương pháp policy gradient, giúp học trực tiếp chính sách mà không cần ước lượng hàm giá trị.

    - Áp dụng kỹ thuật actor-critic, kết hợp giữa học chính sách (actor) và học giá trị (critic).

    - Thích nghi với môi trường có không gian trạng thái và hành động liên tục nhờ policy gradient.

2. Nội dung chính
    2.1 Giới thiệu policy gradient
        - Khác biệt so với value-based methods (như Q-learning), policy gradient học trực tiếp tham số chính sách 
        - Sử dụng thuật toán như REINFORCE, tận dụng gradient của kỳ vọng reward để cập nhật trực tiếp các tham số chính sách.
    
    2.2 Actor‑Critic
        - Actor phụ trách điều chỉnh chính sách, critic đánh giá hành động bằng hàm giá trị.

        - Kết hợp giữa policy gradient và TD learning, giúp giảm độ phương sai và cải thiện hiệu quả học.
    
    2.3 Hành động và trạng thái liên tục
        - Học policy dạng phân phối, ví dụ Gaussian policy, thích hợp cho môi trường với hành động liên tục.

        - Triển khai trên các bài toán thực tế như robot control hoặc environment có state liên tục.
    2.4 Ứng dụng thực tế
        - Programming assignment: Average Reward Softmax Actor-Critic using Tile-coding (~180 phút), giúp bạn thực hành kỹ thuật Actor-Critic trong môi trường có action liên tục

3. Kết luận.
    - Không cần value function: học trực tiếp policy giúp đơn giản hóa (không cần ước lượng Q).

    - Actor‑Critic: kết hợp ưu điểm của policy gradient và value-based để học nhanh hơn và ổn định hơn.

    - Thích nghi môi trường liên tục: Gaussian hoặc Softmax policies mở rộng ứng dụng sang các bài toán điều khiển thực tế.

    - Thực hành mạnh mẽ: assignment yêu cầu tích hợp tile coding, softmax và actor-critic — giúp bạn nắm vững cả lý thuyết lẫn thực thi 