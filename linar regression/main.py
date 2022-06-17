import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Stichprobengröße
n = 100

# ziehe x aus Normalverteilung
mu1 = 10
sigma1 = 3
x = np.random.normal(loc=mu1, scale=sigma1, size=n)

# erzeuge y
b1 = 2
b0 = 5
sigmaError = 2
y = b1 * x + b0 + np.random.normal(loc=0.0, scale=sigmaError, size=n)
formelText = (
        "y = "
        + str(b1)
        + "*x+"
        + str(b0)
        + "+ ε mit ε~N(0,"
        + str(sigmaError * sigmaError)
        + ")"
)

# für die lineare Regression aus sklearn muss x eine Spalte sein
x = x.reshape((-1, 1))

# berechne lineare Regression
model = LinearRegression()
model.fit(x, y)

r_sq = model.score(x, y)
intercept = model.intercept_
slope = model.coef_
print("intercept:", intercept)
print("slope:", slope)
print("coefficient of determination:", r_sq)

# plot
plt.scatter(x, y, alpha=0.5)
plt.title(formelText)
plt.xlabel("x")
plt.ylabel("y")
t = (min(x), max(x))
plt.plot(t, model.predict(t), "-r")
ax = plt.gca()
plt.text(
    0.95,
    0.05,
    "R² = " + str(round(r_sq, 2)),
    horizontalalignment="right",
    verticalalignment="center",
    transform=ax.transAxes,
)
plt.show()
