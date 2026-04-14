import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("dataset.csv")

# Features and target
X = data[['temperature', 'humidity', 'ph']]
y = data['rainfall']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Function for prediction
def predict_rainfall(temp, humidity, ph):
    result = model.predict([[temp, humidity, ph]])
    return result[0]

# Test
if __name__ == "__main__":
    print("Predicted Rainfall:", predict_rainfall(28, 65, 6.5))