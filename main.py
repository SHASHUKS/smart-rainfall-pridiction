from rainfall_model import predict_rainfall
from crop_model import predict_crop

print("===== Smart Agriculture System =====")

temp = float(input("Enter Temperature: "))
humidity = float(input("Enter Humidity: "))
ph = float(input("Enter Soil pH: "))
soil = input("Enter Soil Type (Loamy/Sandy/Clay): ")

# Predict rainfall
rainfall = predict_rainfall(temp, humidity, ph)
print("Predicted Rainfall:", rainfall)

# Predict crop
crop = predict_crop(temp, humidity, ph, rainfall, soil)
print("Recommended Crop:", crop)