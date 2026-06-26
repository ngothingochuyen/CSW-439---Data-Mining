# 1. Đọc dữ liệu
df = pd.read_csv('file.csv')      # Đọc file CSV vào biến df (DataFrame)

# 2. Làm sạch dữ liệu
df.drop(columns=['ID'], inplace=True)  # Xóa cột không cần thiết (inplace=True để lưu thay đổi ngay trên df)
df['cot'].fillna(value, inplace=True)  # Điền các giá trị thiếu (NaN) bằng giá trị 'value' (có thể là mean, median, hoặc hằng số)
df.dropna(inplace=True)                # Xóa các dòng có chứa giá trị thiếu

# 3. Khám phá dữ liệu
df.info()         # Xem kiểu dữ liệu và số lượng giá trị không null
df.describe()     # Xem thống kê cơ bản (trung bình, độ lệch chuẩn, min, max...)
df.corr()         # Xem ma trận tương quan giữa các cột số

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ==========================================
# 1. LOAD & CLEAN DATA
# ==========================================
df = pd.read_csv('Diabetes.csv')

# Xử lý các cột không cần thiết
df.drop(columns=['ID', 'No_Pation'], inplace=True, errors='ignore')

# Điền giá trị thiếu
df['CLASS'].fillna('P', inplace=True)
df['HbA1c'].fillna(df['HbA1c'].median(), inplace=True)
df['VLDL'].fillna(df['VLDL'].median(), inplace=True)

# ==========================================
# 2. FEATURE ENGINEERING
# ==========================================
# Mã hóa dữ liệu
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])
df['CLASS'] = df['CLASS'].map({'N': 0, 'P': 1, 'Y': 2})

# Phân tách X, y
X = df.drop(columns=['CLASS'])
y = df['CLASS']

# Chuẩn hóa dữ liệu (Quan trọng cho KNN)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ==========================================
# 3. MODEL TRAINING
# ==========================================
# Chia tập dữ liệu
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Khởi tạo và huấn luyện KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Dự đoán
y_pred = knn.predict(X_test)

# ==========================================
# 4. EVALUATION & VISUALIZATION
# ==========================================
acc_score = accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc_score:.2f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Vẽ Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()