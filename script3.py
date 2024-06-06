import sys
import pandas as pd
from sklearn.linear_model import LinearRegression
import category_encoders as ce
import repcount as rc

# Read the training data
d1 = pd.read_excel('ML Main/training.xlsx')

# Create a synthetic dataset
data = {
    'prob': d1.iloc[:, 3].tolist(),
    'size': d1.iloc[:, 4].tolist(),
    'tech_sc': d1.iloc[:, 6].tolist()
}
df = pd.DataFrame(data)

# Separate features (X) and target variable (y)
X = df[['prob', 'size', 'tech_sc']]
y = d1.iloc[:, 5].tolist()

# Binary Encoding:
binary_encoder = ce.BinaryEncoder(cols=['prob'])
X_binary = binary_encoder.fit_transform(X[['prob']])


model_binary = LinearRegression().fit(X_binary, y)

# Read command line arguments
title = sys.argv[1]
target_industry = sys.argv[2]
problem_statement = sys.argv[3]

# Perform text processing for 'problem_statement'
rel = rc.counter(problem_statement)

# Prepare input data for prediction
p = {
    'prob': problem_statement,
    'size': int(target_industry),
    'tech_sc': rel
}
X_test = pd.DataFrame(p, index=['prob', 'size', 'tech_sc'])
X_test_binary = binary_encoder.transform(X_test[['prob']])
y_pred_binary = model_binary.predict(X_test_binary)
y_pred_percentage = int(y_pred_binary[0] * 100)

# Print the prediction result
print(y_pred_percentage)
