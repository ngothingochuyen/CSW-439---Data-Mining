1. Bối cảnh:
- Olist: e-commerce business
- Quan tâm đến: customer satisfaction 
- customer satisfaction <-- review score (khách hàng đánh giá như nào sau khi mua sản phẩm)
- Dữ liệu giao dịch lịch sử của Olist cho biết:
  11.5% orders được đánh giá 1 sao 

2. Vấn đề:
- Đặt giả thiết: các đánh giá 1 sao có thể đến từ việc khâu vận hành không tốt.
- Các vấn đề xoay quanh khâu vận hành có thể là:
    + Thời gian giao hàng
    + Phương thức thanh toán
    + Vị trí địa lý của khách hàng

3. Mục tiêu:

Xây dựng Data Mining Pipeline để:
- xác định nhóm các nguyên nhân liên quan đến khâu vận hành có khả năng dẫn tới đánh giá 1 sao
- sử dụng phương pháp modeling: Frequent Pattern Mining
- expected output: cause-and-effect rules (Antecedents → Consequents) (Nguyên nhân - Hậu quả) 
--> Hậu quả cụ thể ở bài toán này là: đánh giá 1 sao 



Work in Groups:
- Tìm hiểu các nội dung sau trong Pipeline:
    1. Data Visualization (thuộc Data Understanding)
    2. Data Preprocessing
    3. Data Modeling
- Nội dung cần xác định:
    1. Data Visualization (thuộc Data Understanding)
      - Mỗi biểu đồ thể hiện điều gì? 
    2. Data Preprocessing
      - Quá trình hợp nhất dữ liệu được thực hiện như nào? 
      - Các thuộc tính được lựa chọn cho model
      - Discretization và Binarization là gì trong tiền xử lý dữ liệu? Hai bước này được thực hiện như nào và trả về kết quả gì trong bài này? Tại sao phải thực hiện 2 bước này, dựa vào đâu để xác định phải thực hiện 2 bước này? (xem phần visualization)
      - Itemization và Transaction Matrix là gì? Hai bước này được thực hiện như nào và trả về kết quả gì trong bài này? Tại sao cần 2 bước này cho bài toán Frequent Pattern Mining? 
    3. Data Modeling
      - Các thuật toán Pattern Mining nào được sử dụng trong bài này?
      - Giải thích cách thức hoạt động của các thuật toán đó.
        + input?
        + có hyperpameter (siêu tham số) nào? chúng là gì? tại sao lại gán chúng với các giá trị như vậy?
        + output?
        cụ thể:
          - Với FP-Growth: input là? min_support là? tại sao chọn min_support=0.01 (gợi ý: xem phần visualization)? FP-Growth hoạt động như nào để trả về kết quả? Và kết quả là gì?
          - Với Association Rule: input? Lift metric là gì? min_threshold là gì? tại sao chọn min_threshold = 1.0? Association Rule hoạt động như nào để trả về kết quả? Và kết quả là gì?
      - Step 3: filter rules thực hiện lọc các "luật kết hợp" đã được sinh ra từ step 2. tại sao phải có step 3 này?
      - Kết quả cuối cùng như thế nào?
          + Có bao nhiêu tập luật tìm được?
          + Bạn nhìn thấy được gì từ những tập luật này?

      - Tìm hiểu thuật toán Apriori: thuật toán này hoạt động như nào? khác gì FP-Growth? tại sao không nên sử dụng Apriori để giải bài toán này?