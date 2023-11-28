from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Sample data for training the decision tree
# Features: [health, distance]
X = [
    [80, 10],  # high health, short distance
    [60, 5],   # moderate health, short distance
    [30, 15],  # low health, medium distance
    [10, 20],  # very low health, long distance
    [70, 8],   # high health, short distance
    [40, 18],  # moderate health, medium distance
    [20, 25],  # low health, long distance
    [5, 30],   # very low health, very long distance
]

# Labels: 0 for defend, 1 for attack
y = [1, 1, 0, 0, 1, 0, 0, 0]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Decision Tree classifier
clf = DecisionTreeClassifier()

# Train the classifier on the training data
clf.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = metrics.accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Example: Use the trained model to make a prediction for a new scenario
new_scenario = [[50, 12]]  # moderate health, short distance
prediction = clf.predict(new_scenario)
print(f"Prediction for new scenario: {'Attack' if prediction[0] == 1 else 'Defend'}")
