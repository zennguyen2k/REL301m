- Mục tiêu:

Kết hợp giữa “lập kế hoạch (planning)” dựa trên mô hình và “học từ dữ liệu” thực tế thông qua phương pháp Dyna.

Cải thiện tính hiệu quả khi thu thập dữ liệu (sample-efficiency) so với các phương pháp RL đơn thuần như Q‑learning 

- Nội dung chính:

1. Khái niệm “Model” trong RL

Một model có thể là: 

 Sample model: mô phỏng trạng thái và phần thưởng dựa trên các mẫu đã thu thập.
 
 Distribution model: cung cấp phân phối xác suất chuyển tiếp.

Sự khác biệt giữa hai loại này được giới thiệu trong tất cả các video đầu 

2. Random Tabular Q‑Planning

Đây là bước chuyến từ việc học trực tiếp sang thử nghiệm mô phỏng trong model (planning).

Thực hiện các bản cập nhật Q‑value dựa trên experience giả lập từ model.

3. Kiến trúc Dyna

Dyna tích hợp:

  Học model: Ước lượng P(s', r | s, a) từ kinh nghiệm thực.

  Planning: Sử dụng model giả để sinh ra các “experience ảo” và cập nhật Q hoặc V values (bootstrap).

  Action in real world: Tác nhân tương tác trực tiếp với môi trường.

Một cách ngắn gọn: “Experience + model learning + planning” 

4. Thuật toán Dyna

Thực hiện như sau:

  1. Tương tác thật → thu nhận (s, a, r, s')
  2. Cập nhật Q via TD (ví dụ Q‑learning).
  3. Cập nhật model bằng data thật.
  4. Lặp n lần planning: chọn ngẫu nhiên (sₚ, aₚ) đã biết, giả lập rₚ, sₚ', cập nhật Q again.

5. Dyna‑Q và Dyna‑Q+

  Dyna‑Q: phiên bản cơ bản với số bước planning cố định.
  Dyna‑Q+ thêm cơ chế khám phá ưu tiên để xử lý môi trường thay đổi (non-stationary).
  Một assignment thực hành sử dụng hai biến thể này để so sánh 

6. Xử lý mô hình không chính xác và môi trường thay đổi

  Phân tích cách Dyna‑Q(+):
  
   Vẫn hoạt động tốt ngay cả khi model bị sai lệch nhẹ.
  
   Cho phép tác nhân thích ứng nhanh với môi trường thay đổi

- Các điểm nổi bật:
  
  Tăng hiệu quả dữ liệu: nhờ kế hoạch dựa trên model, không cần trải nghiệm thật nhiều.

  Kết hợp linh hoạt giữa học và planning, là bước đệm từ các phương pháp thuần túy model-free (Q‑learning) hoặc model-based (dynamic programming).

  Phù hợp trong môi trường thực tế: nơi mà mô hình môi trường thường bị sai lệch và thay đổi theo thời gian.

  Dyna là nền tảng cho các kỹ thuật nâng cao như replay buffer trong deep RL và Prioritized Sweeping.

- Kết luận:
  Module 5 giới thiệu kiến trúc Dyna, giúp tác tử học mô hình từ tương tác thật, phác thảo tương tác giả để planning, kết hợp cả hai để cập nhật giá trị một cách hiệu quả và thích ứng môi trường.




  

    





  

 
