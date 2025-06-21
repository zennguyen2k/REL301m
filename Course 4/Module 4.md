1. Mục tiêu

    - Xác định và hiểu rõ các tham số quan trọng ảnh hưởng đến hiệu suất của agent RL.

    - Hình thành nền tảng để chọn một tham số cụ thể làm chủ đề nghiên cứu sâu hơn trong milestone tiếp theo.

2. Nội dung chính  

    2.1 Agent Architecture – Overview of Design Choices
        - Phân tích các tầng trong kiến trúc agent: từ mạng neural (số layer, kích thước, activation) đến optimizer và chiến lược khám phá.
    
    2.2 Let's Review: Non-linear Approximation with Neural Networks 
        - Ôn lại các khái niệm cơ bản của mạng neural dùng làm hàm xấp xỉ giá trị hoặc hàm hành động.

    2.3 Drew Bagnell on System ID & Optimal Control 
        - Giải thích phương pháp xác định hệ thống (system identification), cách modeling và tối ưu hóa trong bối cảnh RL thực tế.
    
    2.4 Susan Murphy on RL in Mobile Health 
        - Trình bày ứng dụng RL cho lĩnh vực y tế di động (Mobile Health), nhấn mạnh đến việc chọn tham số phù hợp (như learning rate, gamma, exploration) để đảm bảo ổn định và hiệu quả lâu dài.

3. Kết luận

    - Hiểu rõ “parameter space”: RL agent không chỉ là thuật toán mà còn phụ thuộc nhiều vào các thiết lập nội tại của mạng và bộ tối ưu.

    - Chọn tham số có ảnh hưởng lớn: Không phải mọi tham số đều tác động giống nhau — cần xác định yếu tố nào ảnh hưởng nhất đến kết quả học.

    - Rèn kỹ năng thiết kế thực nghiệm: Module giúp cách lập kế hoạch và thực hiện thử nghiệm khoa học, quan sát kết quả bằng metric định lượng.