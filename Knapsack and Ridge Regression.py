# Assignment 03: Dynamic Programming - Knapsack and Ridge Regression

import numpy as np
def knapsack(weights, values, W, n):
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
n = len(values)
print("----- Part A: 0/1 Knapsack -----")
print("Values:", values)
print("Weights:", weights)
print("Knapsack Capacity:", W)
print("Maximum value in Knapsack =", knapsack(weights, values, W, n))

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1.2, 1.9, 3.0, 4.1, 5.1])
lambda_reg = 0.1  

cache = {}

def ridge_loss(theta, X, y, lam):
    theta = round(theta, 2)  
    if theta in cache:
        return cache[theta]
    
    predictions = X.flatten() * theta
    loss = np.sum((y - predictions) ** 2) + lam * (theta ** 2)
    cache[theta] = loss
    return loss

thetas = np.linspace(0, 2, 201)  
best_theta = min(thetas, key=lambda t: ridge_loss(t, X, y, lambda_reg))
best_loss = ridge_loss(best_theta, X, y, lambda_reg)

print("\n----- Part B: Ridge Regression Optimization -----")
print("Dataset X:", X.flatten())
print("Dataset y:", y)
print("Optimal parameter θ =", best_theta)
print("Minimum Ridge Loss =", best_loss)

