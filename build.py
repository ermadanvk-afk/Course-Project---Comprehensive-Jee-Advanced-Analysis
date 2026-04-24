import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import KFold
from sklearn.metrics import mean_absolute_error, r2_score

# Load data
df = pd.read_csv("rank predictor.csv").dropna()

# Features
df['pct_score'] = df['Marks'] / df['max marks']
df['pct2'] = df['pct_score'] ** 2
df['pct3'] = df['pct_score'] ** 3

X = df[['pct_score', 'pct2', 'pct3', 'no of candidates', 'max marks']]
y = np.log(df['Rank'])

# Train
model = GradientBoostingRegressor(n_estimators=500, learning_rate=0.03, max_depth=6, subsample=0.8, random_state=42)
model.fit(X, y)

# Predict function
def predict_rank(marks, max_marks, candidates):
    pct = marks / max_marks
    X_pred = pd.DataFrame([[pct, pct**2, pct**3, candidates, max_marks]],
                           columns=['pct_score', 'pct2', 'pct3', 'no of candidates', 'max marks'])
    return int(np.round(np.exp(model.predict(X_pred)[0])))
import joblib

# Model ko file mein save karein
joblib.dump(model, "rank_model.pkl")