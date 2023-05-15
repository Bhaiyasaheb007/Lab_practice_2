from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Define the employee dataset
# Each data point represents an employee's features and their performance rating
# Replace this with your actual labeled dataset
employee_data = [
    [25, 5, 8, 7, 'High'],
    [30, 7, 9, 8, 'High'],
    [35, 6, 7, 6, 'Low'],
    [40, 8, 9, 9, 'High'],
    [35, 5, 8, 7, 'High'],
    [28, 7, 9, 8, 'High'],
    [35, 6, 3, 6, 'Low'],
    [40, 8, 7, 9, 'High'],
    # Add more data points...
]

# Separate features (X) and labels (y)
X = [data[:-1] for data in employee_data]
y = [data[-1] for data in employee_data]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a decision tree classifier
classifier = DecisionTreeClassifier()

# Train the classifier
classifier.fit(X_train, y_train)

# Make predictions on the test set
predictions = classifier.predict(X_test)

print('-----------------------------------------------------------------------------------')
print(X_test)
print('-----------------------------------------------------------------------------------')
print(predictions)
print('-----------------------------------------------------------------------------------')

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

