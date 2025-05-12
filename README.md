# REL301m
NguyenVanCuong - QS170119
1. Giới thiệu cơ bản về Reinforcement Learning
Reinforcement Learning (Học tăng cường) là một nhánh của Machine Learning, tập trung vào cách một tác nhân (agent) học cách đưa ra quyết định thông qua tương tác với môi trường để tối đa hóa phần thưởng tích lũy theo thời gian.
* Những khái niệm chính cần biết:
Agent (Tác nhân): Thực thể ra quyết định (ví dụ: robot, chương trình máy tính).

Environment (Môi trường): Nơi mà agent tương tác (ví dụ: một trò chơi, robot di chuyển trong phòng).

Action (Hành động): Những gì agent có thể làm tại một thời điểm.

State (Trạng thái): Thông tin về tình huống hiện tại của môi trường.

Reward (Phần thưởng): Một giá trị số thể hiện mức độ tốt/xấu của hành động agent vừa thực hiện.

Policy (Chính sách): Chiến lược chọn hành động của agent dựa trên trạng thái hiện tại.

Value Function: Ước tính phần thưởng dài hạn nếu làm theo một chính sách nào đó.
==> Mục tiêu của học tăng cường là huấn luyện agent để tìm ra chính sách tối ưu, nhằm tối đa hóa tổng phần thưởng kỳ vọng qua thời gian (còn gọi là return).

2. Một số thuật toán phổ biến trong RL:
Dynamic Programming (Lập trình động) – như Value Iteration, Policy Iteration.

Monte Carlo Methods

Temporal Difference (TD) Learning – như Q-Learning, SARSA.

Deep Reinforcement Learning – ví dụ: Deep Q-Networks (DQN), Policy Gradient, Actor-Critic,…

3. Ứng dụng thực tế: 
Trò chơi (ví dụ: AlphaGo, Dota2, StarCraft)

Robotics (robot tự học cách đi/làm việc)

Tài chính (tối ưu hóa danh mục đầu tư)

Hệ thống khuyến nghị

Giao thông thông minh, năng lượng,…
