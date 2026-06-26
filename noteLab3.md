LAB 3: tiếp tục nội dung Lab 2

1. Work in groups:
- Thời gian: 60p
- Nội dung:
    1) Lab 2: trình bày nội dung tìm hiểu được theo hướng dẫn ở lab 2
    2) Tìm hiểu và trình bày nội dung Example 4.3. Apriori. (slide) và Example 4.4. Generating association rules. (slide)
    3) Tương tự với Example 4.5. FP-growth

2. Present
- Ngẫu nhiên 3 nhóm trình bày 3 nội dung trên
- Thời gian: 20p/nhóm
- Gợi ý nội dung trình bày:
    1) Thuật toán Apriori:
        + Bước 1: Khởi tạo
            - Database có bao nhiêu giao dịch (transactions) và bao nhiêu mặt hàng (items)?
            - Siêu tham số min support được setup như nào? Con số đó thể hiện điều gì?
        + Bước 2: Quá trình tìm tập phổ biến (frequent itemset mining)
            - Vòng lặp 1 (L1): Tìm các tập có 1 phần tử
                + Thuật toán quét database để tìm gì?
                + Kết quả được lọc như nào?
            - Vòng lặp 2 (L2): Tìm các tập có 2 phần tử
                + Cách thực hiện "Sinh ứng viên"
                + Quét và lọc phần tử?
            - Vòng lặp 3: tương tự L2
            - Vòng lặp 4: tương tự L3
            - Kết thúc ở vòng lặp thứ mấy?
        + Bước 3: Quá trình sinh "luật kết hợp" (association rules)
            - Quá trình này được thực hiện dựa trên độ đo (công thức) nào?
            - Với từng tập phổ biến (Frequent Itemset) tìm được ở Bước 2, giải thích cách tính toán độ tin cậy cho từng possible rules
            - Giả sử confidence threshold (ngưỡng tin cậy) là 70%, có bao nhiêu Luật kết hợp được sinh ra? 
   
    2) Thuật toán FP-Growth
        + Giai đoạn 1: Xây dựng cây FP-Tree
            - Ở Apriori, thuật toán đã quét qua dữ liệu bao nhiêu lần để hoàn thành? - 3
            - Với FP-Growth, thuật toán cần quét qua dữ liệu bao nhiêu lần? -2
            - Mỗi lần quét dữ liệu, FP-Growth thực hiện điều gì?
                + Nhiệm vụ mỗi lần quét - Lần quét 1: đếm support, item - count, sắp xếp giảm dần - Lần quét 2: Sắp xếp theo thứ tự L, chèn vào cây
                + Các bước thực hiện bên trong mỗi lần quét
                + Kết quả sau mỗi lần quét
            - Hình dạng FP-Tree xây dựng được?
        + Giai đoạn 2: Tìm tập phổ biến (frequent itemset) từ FP-Tree 
            Khi đã xây được cây FP-Tree, FP-Growth không cần sử dụng lại database gốc nữa. Nó bắt đầu thực hiện khai phá tập phổ biến từ cây FP-Tree đã xây dựng được bằng cách nhìn các items từ ít phổ biến đến phổ biến nhất trong danh sách.
            Ví dụ: bắt đầu với item I5
            - Bước 1: tìm cơ sở mẫu điều kiện (conditional pattern base)
            - Bước 2: Xây dựng cây điều kiện cho I5 (conditional FP-Tree)
            - Bước 3: Sinh tập phổ biến với I5
            Tương tự cho các item còn lại (recursion).
            Giải thích các bước trên.

    3) Giải thích cách thuật toán FP-Growth hoạt động trong bài toán Khai phá hành vi vận hành:
        - Bước 1: Xây cây FP-Tree và Tìm tập phổ biến
            Giải thích nội dung xảy ra bên trong:
            + Quét lần 1: Lọc phần tử hiếm
            + Quét lần 2: Xây cây FP-Tree
            + Sinh Frequent Itemset
            ==> Kết quả?
        - Bước 2: Sinh luật kết hợp (association rules)
            VD: Lấy một tập phổ biến tìm được ở bước 2 
                {pay_credit_card, delicery_late, review_1_star}
            Đã có 2 thử nghiệm được thực hiện để sinh luật kết hợp. Giải thích nội dung xảy ra bên trong 2 thử nghiệm:
            + Thử nghiệm 1: {review_1_star} --> {pay_credit_card, delivery_late}
            + Thử nghiệm 2: {pay_credit_card, delivery_late} --> {review_1_star}
            + Trong mỗi thử nghiệm, tính Lift. Kết luận mỗi thử nghiệm.
        - Bước 3: Tính Kulc
            + Lý do cần bước này?
            + Giải thích nội dung hoạt động bên trong
        - Bước 4: Lọc (Filter)
            + Nội dung bên trong bước này?
            
3. Lecture




# Phân Tích Chi Tiết Cấu Trúc Và Cơ Chế Duyệt FP-Tree

FP-Tree (Frequent Pattern Tree) là giải pháp tối ưu để khai thác tập phổ biến nhờ vào việc nén dữ liệu và hạn chế việc quét cơ sở dữ liệu (CSDL) nhiều lần.

---

## 1. Cơ Chế Hình Thành Cây (Xây dựng FP-Tree)

Cây được xây dựng qua 2 lần quét CSDL:
1.  **Quét lần 1:** Đếm tần suất các mục đơn lẻ và sắp xếp chúng vào **Header Table** theo thứ tự giảm dần. Các mục không đủ độ hỗ trợ tối thiểu (min_sup) sẽ bị loại bỏ ngay từ đây.
2.  **Quét lần 2:** Đọc từng giao dịch, sắp xếp các mục trong giao dịch đó theo thứ tự trong Header Table và chèn vào cây.
    * Nếu các giao dịch có chung tiền tố (prefix), chúng sẽ chia sẻ các nút gốc (ví dụ: `I2 -> I1`).
    * Mỗi nút lưu trữ giá trị `count` (tần suất). Khi một giao dịch mới đi qua nút cũ, `count` sẽ tăng thêm 1.

---

## 2. Giải Thuật Duyệt Cây Chi Tiết (Khai thác I5 làm ví dụ)

Để khai thác các tập phổ biến, ta sử dụng phương pháp **Chia để trị (Divide and Conquer)** bằng cách duyệt từ dưới lên (Bottom-up).

### Bước 1: Tìm Đường dẫn tiền tố (Suffix -> Prefix Paths)
Dựa vào đường liên kết nút (Node-link) từ Header Table, ta xác định các nhánh chứa **I5**:
* Nhánh trái: `(I2, I1 : 1)`
* Nhánh phải: `(I2, I1, I3 : 1)`
* *Lưu ý: Chỉ lấy các nút nằm TRƯỚC mục đang xét.*

### Bước 2: Xây dựng Cơ sở mẫu điều kiện (Conditional Pattern Base)
Tập hợp các tiền tố này tạo thành một CSDL nhỏ chỉ dành riêng cho I5:
* `CPB(I5) = { (I2, I1: 1), (I2, I1, I3: 1) }`

### Bước 3: Tạo FP-Tree điều kiện (Conditional FP-Tree)
Tính tổng số lần xuất hiện của các mục trong CPB của I5:
* **I2:** 1 + 1 = 2
* **I1:** 1 + 1 = 2
* **I3:** 1
* *Nếu min_sup = 2*, I3 sẽ bị loại bỏ khỏi cây điều kiện của I5.

### Bước 4: Sinh tập phổ biến (Frequent Itemsets)
Kết hợp I5 với các mục còn lại trong cây điều kiện:
* `{I2, I5: 2}`
* `{I1, I5: 2}`
* `{I2, I1, I5: 2}`

---

## 3. Tại sao FP-Tree lại tối ưu?

| Tiêu chí | Giải thuật Apriori | Giải thuật FP-Growth |
| :--- | :--- | :--- |
| **Cách tiếp cận** | Sinh các tập ứng viên (Candidate Generation) | Khai thác cấu trúc cây (Tree Projection) |
| **Số lần quét CSDL** | Rất nhiều lần (bằng độ dài tập mục lớn nhất) | Duy nhất **2 lần** |
| **Không gian lưu trữ** | Tốn kém cho các tập ứng viên trung gian | Nén dữ liệu hiệu quả trong bộ nhớ |
| **Tốc độ** | Chậm khi dữ liệu lớn/nhiều tập mục dài | Nhanh hơn đáng kể, đặc biệt với dữ liệu dày đặc |

---

## 4. Kết luận
FP-Tree không chỉ là một sơ đồ lưu trữ, mà là một phép biến đổi dữ liệu từ dạng bảng (Table) sang dạng cấu trúc liên kết (Linked Structure), giúp thuật toán có thể tìm ra tất cả các mối quan hệ mua sắm của khách hàng chỉ bằng cách đi dọc các cành cây.