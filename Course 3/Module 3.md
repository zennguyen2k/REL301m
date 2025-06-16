1. Mục tiêu
 - Hiểu tầm quan trọng của feature construction trong  việc xấp xỉ hàm giá trị.

 - Khám phá hai cách tiếp cận phổ biến:

   + Fixed basis features như coarse coding, tile coding.
   + Representation học từ dữ liệu với mạng nơ-ron và backpropagation.

2. Nội dung chính

 2.1 Coarse Coding
   - Chia không gian trạng thái thành các vùng chồng đè.

   - Mỗi vùng tương ứng một feature, và một trạng thái có thể kích hoạt nhiều feature cùng lúc.

   - Mang lại khả năng khái quát hóa tốt, nhưng đòi hỏi nhiều feature khi tăng kích thước trạng thái 

 2.2 Tile Coding
    - Mở rộng coarse coding: dùng nhiều bộ lưới (tilings) chồng lên nhau, mỗi bộ dịch lệch.

    - Feature kết hợp giữa các tilings, giúp đạt tính biểu diễn hiệu quả hơn.

    - Thường ứng dụng trong môi trường liên tục như Cart-Pole hoặc Mountain Car . 

 2.3 Neural Networks
   - Sử dụng NN để tự học representation thông qua backpropagation.

   - Cho phép mô hình hóa mối quan hệ phi tuyến giữa trạng thái và giá trị.

   - Chiến thuật tối ưu gồm: gradient descent, tối ưu sâu (deep), các kỹ thuật như batch norm, regularization .

   - Module bao gồm hướng dẫn từng bước về: “What is a Neural Network?”, “Deep Neural Networks”, “Gradient Descent for Training Neural Networks”, “Optimization Strategies for NNs”

3. Kết luận. 

    - Feature design quyết định hiệu quả học: chọn feature phù hợp giúp giảm bias và tăng generalization.

    - Tile coding là lựa chọn mạnh mẽ khi bạn cần biểu diễn môi trường liên tục mà vẫn giữ linearity trong cập nhật.

    - Neural Networks giúp vượt qua giới hạn của feature thủ công, thích ứng tốt trong không gian lớn nhưng yêu cầu tuning cẩn thận.

    - Phần thực hành gồm Programming assignment: “Semi‑gradient TD with a Neural Network” nâng cao kỹ năng xây dựng feature và huấn luyện model hiệu quả.
