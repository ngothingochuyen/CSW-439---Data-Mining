1. Business Context:

Olist is one of the largest e-commerce platforms in Brazil, connecting thousands of retailers with customers nationwide. In the e-commerce industry, Customer Satisfaction is directly reflected through the Review Score. It is not only a measure of brand reputation but also the "lifeblood" that dictates customer retention rates and repeat purchase revenue.Historical data indicates that while the majority of customers have a positive experience, the system still records a significant proportion (approximately 11.5%) of orders receiving the lowest possible rating: 1 Star.

- Olist: e-commerce business 
- Quan tâm đến: customer satisfaction 
- customer satisfaction: review score (khách hàng đánh giá như nào sau khi mua sản phẩm)
- Dữ liệu giao dịch lịch sử của Olist cho biết: 11.5% orders được đánh giá 1 sao

2. The Core Problem:

Every 1-Star review represents a customer abandoning the platform. However, a 1-Star rating is merely a "Symptom" of a much deeper operational disease.Olist's Board of Directors is facing a massive "Operational Black Box": They possess data on over 100,000 orders, dozens of payment methods, various installment plans, and a delivery network spanning the entire Brazilian territory. The primary pain point for Olist is: They do not know exactly which operational bottleneck, or "combination" of bottlenecks, is directly triggering customer dissatisfaction. Analyzing individual variables in isolation (e.g., only looking at delivery speed) is insufficient. Customer frustration often stems from hidden combinatorial rules (For instance, a customer will be exceptionally angry if they prepaid using a credit card AND experienced a late delivery).

- Đặt giả thiết: các đánh giá 1 sao có thể đến từ việc khâu vận hành không tốt
- các vấn đề xoay quanh khâu vận hành có thể là:
    + Thời gian giao hàng
    + Phương thức thanh toán
    + Vị trí địa lý của khách hàng

3. Objectives:

This lab is conducted to decode that operational black box, transforming hundreds of thousands of raw data rows (Orders, Payments, Customers, Reviews) into practical, battle-tested business knowledge. The specific objectives include:

- Building a Data Pipeline: Integrating and preprocessing data from multiple sources, converting continuous time and financial values into clearly defined, categorical "Items".

- Association Rule Mining: Applying the unsupervised machine learning algorithm FP-Growth to "sift sand for gold." The system will proactively identify frequent itemsets that may have a low overall frequency (Rare items) but carry a high risk of negative impact.

- Extracting Actionable Insights: Providing the Chief Operating Officer (COO) with clear cause-and-effect rules (Antecedents $\rightarrow$ Consequents) that lead to a 1-Star review, rigorously validated by mathematical metrics such as Support, Confidence, and Lift.

- Xây dựng Dât Mining Pipline để: 
    - xác định nhóm các nguyên nhân liên quan đến khâu vận hành có khả năng dẫn tới đánh giá 1 sao
    - sử dụng phương pháp modeling: Frequent Pattern Mining
    - expected output: cause-and-effect rules (Antecedents → Consequents) (Nguyên nhân - Hậu quả) 
    --> Hậu quả cụ thể ở bài toán này là: đánh giá 1 sao 

1. Data Understanding
2. Data preprocessing
3. Data modeling: frequent pattern mining
- Apriori
- 