#Activate conda: conda activate data-privacy-env                     # Activate the data-privacy-env environment
#Lệnh install
# pip install pandas numpy seaborn matplotlib scikit-learn scipy
#import 
import pandas as pd                                    # Import pandas library for data manipulation
import numpy as np                                     # Import numpy for numerical operations
import seaborn as sns                                  # Import seaborn for data visualization
import matplotlib.pyplot as plt                        # Import matplotlib for plotting graphs
from sklearn.model_selection import train_test_split   # Split dataset into training and testing sets
from sklearn.preprocessing import LabelEncoder         # Encode categorical features into numeric
from sklearn.preprocessing import StandardScaler       # Standardize features by removing the mean
from sklearn.metrics import accuracy_score             # Calculate accuracy classification score
from sklearn.metrics import confusion_matrix           # Compute confusion matrix to evaluate accuracy
from sklearn.cluster import KMeans                     # Implement KMeans clustering algorithm
from sklearn.metrics import silhouette_score           # Compute Silhouette Score for clustering evaluation
from sklearn.decomposition import PCA                  # Principal Component Analysis for dimensionality reduction

# --- MACHINE LEARNING ALGORITHMS ---
from sklearn.neighbors import KNeighborsClassifier     # Implement K-Nearest Neighbors classifier
from sklearn.linear_model import LogisticRegression   # Implement Logistic Regression classifier
from sklearn.tree import DecisionTreeClassifier        # Implement Decision Tree classifier
from sklearn.ensemble import RandomForestClassifier    # Implement Random Forest classifier



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

df = pd.read_csv("Dataset of Diabetes.csv")  # 1. Đọc file
print(df.shape)                              # 2. Xuất kích thước (Dòng, Cột)
print(df.columns)                            # 3. Xuất danh sách tên các cột
print(df.dtypes)                             # 4. Kiểu dữ liệu của từng cột
print(df.describe())                         # 5. Thống kê số liệu (Min, Max, Mean, Median)
print(df.head())                             # 6. Xem 5 dòng dữ liệu đầu tiên

# 1. XÓA CỘT KHÔNG CẦN THIẾT (Thay 'ID', 'No_Pation' bằng tên cột rác đề bài yêu cầu xóa)
df.drop(columns=['ID', 'No_Pation'], inplace=True, errors='ignore') 
# 2. ĐIỀN Ô TRỐNG CHO CỘT CHỮ (Thay 'CLASS' bằng tên cột; thay 'P' bằng chữ đề bài muốn điền)
df['CLASS'].fillna('P', inplace=True)
# 3. ĐIỀN Ô TRỐNG CHO CỘT SỐ BẰNG TRUNG VỊ (Thay cả 2 chữ 'HbA1c' bằng cột số đề bài yêu cầu)
df['HbA1c'].fillna(df['HbA1c'].median(), inplace=True)
# 4. ĐIỀN Ô TRỐNG CHO CỘT SỐ BẰNG TRUNG BÌNH (Nếu đề yêu cầu điền bằng giá trị trung bình - Mean)
df['VLDL'].fillna(df['VLDL'].mean(), inplace=True)
# 5. XÓA TOÀN BỘ DÒNG CÓ Ô TRỐNG (Nếu đề ko bảo điền mà bảo xóa thẳng tay các dòng thiếu dữ liệu)
df.dropna(inplace=True)

# KIỂU 1: BOXPLOT (Xem phân phối 1 cột số theo 1 cột chữ. Thay x='cột chữ', y='cột số')
sns.boxplot(x='Gender', y='HbA1c', data=df)
plt.show() # Lệnh bắt buộc để hiển thị hình vẽ ra màn hình
# KIỂU 2: SCATTERPLOT (Mối quan hệ 2 cột số. Thay x='cột số 1', y='cột số 2', hue='cột kết quả để phân màu')
sns.scatterplot(x='AGE', y='Urea', hue='CLASS', data=df)
plt.show()
# KIỂU 3: COUNTPLOT (Biểu đồ đếm số lượng. Thay x='cột chữ cần đếm', hue='cột chữ phụ để chia nhóm nhỏ')
sns.countplot(x='Gender', hue='CLASS', data=df)
plt.show()
###############ĐỀ
# Plot a boxplot to show the distribution of 'HbA1c' across different 'Gender' groups
sns.boxplot(x='Gender', y='HbA1c', data=df)
plt.show()
# Plot a scatter plot of 'AGE' vs 'Urea', colored by 'CLASS'
sns.scatterplot(x='AGE', y='Urea', hue='CLASS', data=df)
plt.show()
# Plot a countplot to show the frequency of 'Gender' categorized by 'CLASS'
sns.countplot(x='Gender', hue='CLASS', data=df)
plt.show()

# 1. CHUYỂN CHỮ THÀNH SỐ TỰ ĐỘNG (Áp dụng cho cột tính năng dạng chữ như Giới tính. Thay 'Gender' bằng cột của bạn)
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])
# 2. CHUYỂN CHỮ THÀNH SỐ THEO Ý MUỐN (Áp dụng cho cột Kết quả. Thay các chữ 'N','P','Y' và số 0,1,2 theo đề)
df['CLASS'] = df['CLASS'].map({'N': 0, 'P': 1, 'Y': 2})
# 3. TÁCH BIẾN X VÀ y (Thay 'CLASS' bằng tên chính xác của cột Kết Quả/Cột cần dự đoán)
X = df.drop(columns=['CLASS'])                 # X chứa tất cả các cột tính năng (đã bỏ cột kết quả)
y = df['CLASS']                                # y chỉ chứa duy nhất 1 cột kết quả cần dự đoán
# 4. CHUẨN HÓA THANG ĐO (Đưa toàn bộ các cột số lớn nhỏ về cùng một hệ quy chiếu để thuật toán chạy chính xác)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)             # Biến X_scaled này sẽ được dùng để đem đi chia Train/Test
####ĐỀ
# Encode the categorical feature 'Gender' into numerical values
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])
# Map categorical labels in 'CLASS' column to specific numeric values
df['CLASS'] = df['CLASS'].map({'N': 0, 'P': 1, 'Y': 2})
# Separate features (X) and target variable (y)
X = df.drop(columns=['CLASS'])                 # X contains all independent features
y = df['CLASS']                                # y contains the dependent target variable
# Standardize the features / Perform feature scaling using StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)             # Scale the features to have mean=0 and variance=1

# 1. CHIA DỮ LIỆU TỶ LỆ 80-20 (Thay test_size=0.2 thành 0.3 nếu đề yêu cầu chia tỷ lệ 70-30)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 2. KHỞI TẠO MÔ HÌNH (Đề bắt dùng thuật toán nào thì COPY ĐÚNG 1 DÒNG của thuật toán đó xuống dưới)
model = KNeighborsClassifier(n_neighbors=5)    # LƯU Ý: Thay số 5 bằng số K đề bài yêu cầu (nếu đề thi ra KNN)
# model = LogisticRegression()                  # Bỏ dấu # ở đầu dòng này nếu đề yêu cầu dùng Logistic Regression
# model = DecisionTreeClassifier(max_depth=3)   # Bỏ dấu # ở đầu dòng này nếu đề yêu cầu dùng Cây quyết định
# model = RandomForestClassifier(n_estimators=100) # Bỏ dấu # ở đầu dòng nếu đề yêu cầu dùng Rừng ngẫu nhiên

# 3. CHO MÁY HỌC (Huấn luyện mô hình trên tập Train)
model.fit(X_train, y_train)
# 4. CHO MÁY LÀM BÀI KIỂM TRA (Dự đoán kết quả trên tập Test độc lập)
y_pred = model.predict(X_test)


# Evaluate model performance / Calculate classification accuracy score
acc = accuracy_score(y_test, y_pred)           # Compare actual test labels with predicted labels
print(f"Accuracy: {acc * 100:.2f}%")           # Print the final accuracy percentage
# Generate and print the confusion matrix
cm = confusion_matrix(y_test, y_pred)          # Compute confusion matrix
print("Confusion Matrix:")
print(cm)    
                                  # Display the matrix array
# 1. TÍNH ĐỘ CHÍNH XÁC (Accuracy)
acc = accuracy_score(y_test, y_pred)           # So sánh kết quả thật (y_test) và kết quả máy đoán (y_pred)
print(f"Độ chính xác: {acc * 100:.2f}%")       # In ra màn hình tỷ lệ phần trăm chính xác (Ví dụ: 95.50%)
# 2. XUẤT MA TRẬN NHẦM LẪN (Confusion Matrix)
cm = confusion_matrix(y_test, y_pred)          # Tạo ma trận thống kê các trường hợp đoán đúng/đoán sai
print("Ma trận nhầm lẫn:")
print(cm)                                      # Hiển thị ma trận số ra màn hình

# Initialize a vector consisting entirely of N zero elements
arr = np.zeros(5)                      # Tạo mảng gồm 5 số 0 (Thay số 5 bằng N của đề bài)
# Initialize a vector consisting entirely of N elements, all equal to 1
arr = np.ones(5)                       # Tạo mảng gồm 5 số 1 (Thay số 5 bằng N của đề bài)
# Create a vector with values ranging from Start to End
arr = np.arange(10, 50)                # Tạo mảng chạy từ 10 đến 49 (Thay số 10 và 50 theo đề)
# Create a 3x3 identity matrix
matrix = np.eye(3)                     # Tạo ma trận đơn vị kích thước 3x3 (Thay số 3 bằng kích thước đề cho)
# Create a 3x3 matrix with values ranging from 0 to 8
matrix = np.arange(9).reshape(3, 3)    # Tạo mảng từ 0-8 rồi ép về ma trận vuông 3x3 (Sửa số theo đề)
# Find indices of non-zero elements from an array [1, 2, 0, 0, 4, 0]
indices = np.nonzero([1, 2, 0, 0, 4, 0]) # Tìm vị trí các phần tử khác 0 trong mảng

# Reverse a vector (first element becomes last)
reversed_arr = arr[::-1]               # Đảo ngược chuỗi/mảng arr từ đuôi lên đầu (Giữ nguyên cú pháp [::-1])
# Extract the diagonal elements of a matrix
diag = np.diag(matrix)                 # Lấy các phần tử trên đường chéo chính của ma trận
# Find the minimum and maximum values of a matrix
matrix_min = matrix.min()              # Tìm giá trị nhỏ nhất trong ma trận
matrix_max = matrix.max()              # Tìm giá trị lớn nhất trong ma trận
# Find the mean (average) value of a vector
matrix_mean = arr.mean()               # Tính giá trị trung bình của mảng/vector

# Add a border (filled with 0s) around an existing array
padded_arr = np.pad(arr, pad_width=1, mode='constant', constant_values=0) # Thêm viền số 0 bao quanh mảng
# Transpose a matrix / Swap rows and columns
transposed = matrix.T                  # Chuyển vị ma trận (Biến dòng thành cột, cột thành dòng)
# Multiply matrix A by matrix B (Dot product)
result = np.dot(A, B)                  # Nhân 2 ma trận A và B với nhau (Hoặc viết: A @ B)

# Q1: Check data types of all columns / Get columns info
print(df.dtypes)                                  # Check data types of each column
# Q2: Convert data type of column 'a' to float
df['a'] = df['a'].astype(float)                  # Convert column to float type (Sửa 'a' và float theo đề)
# Q3: Convert data type of column 'b' to string (object)
df['b'] = df['b'].astype(str)                    # Convert column to string type (Sửa 'b' và str theo đề)
# Q4: Convert values in column 'd' to lowercase
df['d'] = df['d'].str.lower()                    # Convert string values to lowercase / Sửa tên cột 'd'
# Q4_alternative: Convert values in column 'd' to uppercase
df['d'] = df['d'].str.upper()                    # Convert string values to uppercase
# Q5: Replace string 'X' with 'A' in column 'd'
df['d'] = df['d'].str.replace('X', 'A')          # Replace characters or substrings / Sửa cột và kí tự theo đề

# Q6: Drop columns that contain any missing values (NaN)
df.dropna(axis=1, inplace=True)                  # Drop columns with NaN values (axis=1 nghĩa là xóa cột)
# Q6_alternative: Drop rows that contain any missing values (NaN)
df.dropna(axis=0, inplace=True)                  # Drop rows with NaN values (axis=0 hoặc bỏ trống nghĩa là xóa dòng)
# Q7: Check if values in column 'd' are in a given list ['X', 'Y'] / Filter rows using .isin()
filtered_df = df[df['d'].isin(['X', 'Y'])]        # Filter rows matching multiple conditions / Thay ['X', 'Y'] theo đề
# Q8: Group by column 'd' and calculate the mean (average) of column 'a'
grouped_mean = df.groupby('d')['a'].mean()        # Group by and find mean / Thay 'd' (cột nhóm) và 'a' (cột tính toán)
# Q8_alternative: Group by column 'd' and calculate the sum of column 'a'
grouped_sum = df.groupby('d')['a'].sum()          # Group by and find sum / Thay 'd' và 'a' theo đề bài
# Q9: Calculate the cumulative sum (cumsum) of all values in column 'a'
df['a_cumsum'] = df['a'].cumsum()                # Calculate cumulative sum for column 'a'

# Q10: Use the np.log() function to calculate the natural logarithm of values in column 'b'
log_values = np.log(df['b'].astype(float))        # Calculate natural logarithm (log) / Sửa cột 'b' theo đề
# Q10_alternative: Calculate square root (sqrt) of values in column 'a'
sqrt_values = np.sqrt(df['a'])                    # Calculate square root using np.sqrt()

# Select numeric and categorical features from your dataframe
numeric_features = ['cột_số_1', 'cột_số_2']           # Identify numeric columns (Sửa tên cột theo đề bài)
categorical_features = ['cột_chữ_1', 'cột_chữ_2']     # Identify categorical columns (Sửa tên cột theo đề bài)

# Define preprocessor using Pipeline and ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),               # Scale numeric features / Chuẩn hóa cột số
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features) # Encode categorical features / Mã hóa cột chữ
    ]
)

# Apply preprocessing to dataframe
X_preprocessed = preprocessor.fit_transform(df)       # Preprocess the entire dataframe / Chạy biến đổi dữ liệu

# Loop through different values of k to calculate silhouette scores
for k in range(2, 6):                                  # Try k from 2 to 5 (Thay đổi khoảng range(start, end) theo đề)
    kmeans = KMeans(n_clusters=k, random_state=0)      # Initialize KMeans algorithm with k clusters
    kmeans.fit(X_preprocessed)                         # Fit KMeans on the preprocessed data
    clusters = kmeans.predict(X_preprocessed)          # Predict cluster labels for each data point
    
    # Evaluate clustering performance using Silhouette Score
    score = silhouette_score(X_preprocessed, clusters) # Calculate the average silhouette score
    print(f"For n_clusters = {k}, Silhouette Score is : {score:.3f}") # Print the score for each k

    optimal_k = 3                                          # Set optimal k based on the question / Sửa số cụm theo đề bài


# Initialize and fit the final KMeans model
kmeans = KMeans(n_clusters=optimal_k, random_state=0)  # Initialize KMeans with optimal k clusters
kmeans.fit(X_preprocessed)                             # Fit the model on preprocessed data
clusters = kmeans.predict(X_preprocessed)              # Predict the cluster assignments
# Assign the cluster labels back to the original dataframe
df['Cluster'] = clusters                               # Add a new 'Cluster' column to store results
print(kmeans.cluster_centers_)                         # Print coordinates of cluster centers / Xuất tâm cụm


# Reduce dimensions using PCA to visualize clusters in 2D space
pca = PCA(n_components=2)                              # Initialize PCA to reduce data to 2 components
X_pca = pca.fit_transform(X_preprocessed)              # Fit and transform the data into 2D dimensions
# Plot the resulting clusters
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=clusters, palette="colorblind") # Scatter plot of PCA 1 vs PCA 2
plt.title('Visualizing Clusters using PCA')            # Set plot title
plt.xlabel('PCA Component 1')                          # Set X-axis label
plt.ylabel('PCA Component 2')                          # Set Y-axis label
plt.legend(title='Cluster')                            # Show legend labeled by cluster
plt.show()                                             # Display the plot