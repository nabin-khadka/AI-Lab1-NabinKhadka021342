import math
from collections import Counter

DATASET = [
    # age, income, jeans_type
    (18, 10000, "Skinny"),
    (21, 15000, "Skinny"),
    (22, 12000, "Skinny"),
    (19, 11000, "Skinny"),
    (25, 20000, "Regular"),
    (24, 18000, "Regular"),
    (28, 22000, "Regular"),
    (27, 21000, "Regular"),
    (29, 23000, "Regular"),
    (30, 25000, "Bootcut"),
    (32, 24000, "Bootcut"),
    (35, 27000, "Bootcut"),
    (36, 26000, "Bootcut"),
    (38, 28000, "Relaxed"),
    (40, 30000, "Relaxed"),
    (42, 33000, "Relaxed"),
    (44, 34000, "Relaxed"),
    (45, 35000, "Relaxed"),
    (48, 37000, "Loose"),
    (50, 40000, "Loose"),
    (52, 42000, "Loose"),
    (55, 45000, "Loose"),
    (53, 43000, "Loose"),
    (60, 47000, "Loose"),
]

K = 3

def compute_distance(age1, income1, age2, income2):
    return math.sqrt((age1 - age2) ** 2 + (income1 - income2) ** 2)

def predict_jeans_type(input_age, input_income, k=K):
    # Lazy learning: no model, compute on demand
    neighbors = []
    for age, income, jeans_type in DATASET:
        dist = compute_distance(input_age, input_income, age, income)
        neighbors.append((dist, jeans_type))
    neighbors.sort(key=lambda x: x[0])
    top_k = [jeans for _, jeans in neighbors[:k]]
    most_common = Counter(top_k).most_common(1)[0][0]
    return most_common

if __name__ == "__main__":
    age = int(input("Enter age: "))
    income = int(input("Enter monthly income (NPR): "))
    result = predict_jeans_type(age, income)
    print(f"\nPredicted jeans type: {result}")