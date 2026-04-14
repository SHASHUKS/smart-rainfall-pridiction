import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load dataset
data = pd.read_csv("dataset.csv")

# Encode soil type
le_soil = LabelEncoder()
data['soil_type'] = le_soil.fit_transform(data['soil_type'])

# Encode crop
le_crop = LabelEncoder()
data['crop'] = le_crop.fit_transform(data['crop'])

# Features and target
X = data[['temperature', 'humidity', 'ph', 'rainfall', 'soil_type']]
y = data['crop']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Prediction function
def predict_crop(temp, humidity, ph, rainfall, soil):
    soil_encoded = le_soil.transform([soil])[0]
    prediction = model.predict([[temp, humidity, ph, rainfall, soil_encoded]])
    return le_crop.inverse_transform(prediction)[0]

# Test
if __name__ == "__main__":
    print("Suitable Crop:", predict_crop(28, 65, 6.5, 180, "Clay"))