# Assignment 02: Feature Selection using Decision Trees
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("C:/Users/0555/Downloads/house_data.csv")

data = data.drop(columns=['id', 'date'])

data['sqft_ratio'] = data['sqft_living'] / (data['sqft_lot'] + 1e-5)  # avoid division by zero
data['age'] = 2025 - data['yr_built']
data['bath_per_bed'] = data['bathrooms'] / (data['bedrooms'] + 1e-5)
data['renovated'] = np.where(data['yr_renovated'] > 0, 1, 0)
data['total_rooms'] = data['bedrooms'] + data['bathrooms']

X = data.drop(columns=['price'])
y = data['price']

X = X.fillna(0)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

selected_features = []
remaining_features = list(X.columns)
best_overall_accuracy = 0

print(" Greedy Forward Feature Selection:\n")

while remaining_features:
    best_feature = None
    best_accuracy = 0

    for feature in remaining_features:
        current_features = selected_features + [feature]
        clf = DecisionTreeClassifier(random_state=42)
        clf.fit(X_train[current_features], y_train)
        preds = clf.predict(X_test[current_features])
        acc = accuracy_score(y_test, preds)

        if acc > best_accuracy:
            best_accuracy = acc
            best_feature = feature

    if best_feature and best_accuracy > best_overall_accuracy:
        selected_features.append(best_feature)
        remaining_features.remove(best_feature)
        best_overall_accuracy = best_accuracy
        print(f" Selected: {best_feature} → Accuracy: {best_accuracy:.4f}")
    else:
        break

print("\n Final Feature Ranking:")
for i, f in enumerate(selected_features, 1):
    print(f"{i}. {f}")

final_clf = DecisionTreeClassifier(random_state=42)
final_clf.fit(X_train[selected_features], y_train)
final_preds = final_clf.predict(X_test[selected_features])
final_accuracy = accuracy_score(y_test, final_preds)

print(f"\n Final Model Accuracy: {final_accuracy:.4f}")
