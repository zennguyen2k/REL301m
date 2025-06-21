1. Mục tiêu

    - Thực hiện việc chạy một loạt thử nghiệm (parameter sweep) trên agent với các giá trị tham số do khóa học cung cấp.

    - Phân tích kết quả để rút ra nhận định khoa học về cách mỗi tham số ảnh hưởng đến hiệu suất agent.

    - Hoàn thành dự án Capstone, nộp báo cáo kết quả nghiên cứu tham số và tóm tắt dự án.

2. Nội dung

    2.1 Notebook: Implement Your Agent
        - Đã từng triển khai agent (Expected Sarsa hoặc Q-learning với mạng nơ‑ron và optimizer như RMSProp) tại tuần 4.

        - Tuần này, notebook cung cấp skeleton code để chạy agent qua nhiều tham số như learning rate, γ, epsilon, architecture, v.v, và thu thập số liệu (reward, số bước, v.v).

    2.2  Notebook: Completing the Parameter Study
        - Viết script để chạy thử nghiệm trên tập giá trị tham số được yêu cầu, thu thập và trực quan hóa kết quả (ví dụ: đường học, boxplot).

        - So sánh đầu vào của từng tham số để xác định mức ảnh hưởng lên hiệu suất.

    2.3 Course Wrap-Up
        - Tổng kết lại toàn bộ quy trình capstone:
            1. Formalize vấn đề thành MDP

            2. Lựa chọn thuật toán phù hợp

            3. Xác định tham số quan trọng

            4. Triển khai agent

            5. Thực hiện nghiên cứu tham số 

        - Định hướng để tiếp tục mở rộng và áp dụng RL vào các bài toán thực tế hơn.

3. Kết luận

    - Sample-efficiency và robustness đánh giá agent trên nhiều tình huống khác nhau để chứng minh agent hoạt động tốt một cách ổn định.

    - Phương pháp khoa học: Việc chạy parameter sweep và phân tích kết quả giúp lý luận một cách thuyết phục về ảnh hưởng của từng tham số.

    - Hoàn thiện dự án: Module này giúp biến dự án thành một bài nghiên cứu nhỏ chuyên nghiệp – có báo cáo rõ ràng, code reproducible và đồ thị minh hoạ.

    - Chuẩn bị ứng dụng thực tế: Kỹ năng chọn tham số hợp lý và hiểu tương tác giữa chúng là cực kỳ quan trọng để triển khai RL ngoài nghiên cứu, ví dụ như robot, tự động hoá, tài chính,…