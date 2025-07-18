import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu từ file CSV
data = pd.read_csv('Dataset2.csv')

# Làm sạch dữ liệu
for column in data.columns:
    if data[column].dtype == object:
        data[column] = data[column].replace({',': '.'}, regex=True)
    data[column] = pd.to_numeric(data[column], errors='coerce')
data = data.dropna()

# Lấy tất cả các cột (16 thuộc tính)
all_features = data.columns

# Vẽ biểu đồ phân bố (Histogram) không có đường cong mật độ
plt.figure(figsize=(20, 15))
for i, column in enumerate(all_features, 1):
    plt.subplot(4, 4, i)
    sns.histplot(data[column], bins=20, kde=False)
    plt.title(column.replace('_', ' ').capitalize(), fontsize=10)  # Làm đẹp tên cột
    plt.xticks(rotation=45, fontsize=8)
    plt.yticks(fontsize=8)
    plt.xlabel('')
    plt.ylabel('')
plt.tight_layout(pad=2.0)
plt.savefig('data1_all_histograms_no_kde.png')
plt.show()
