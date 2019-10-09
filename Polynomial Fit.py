#%% 
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
sns.set_style('whitegrid')


#%% Create dummy data

x = np.arange(25)
delta = np.random.randint(0,3,25)
delta2 = np.random.randint(0,4, 25)
y = np.sin(x)*delta - delta*delta2 + delta2

plt.scatter(x,y)
plt.show()


#%% Split the data
X_train, X_test, y_train, y_test = train_test_split(x, y, random_state = 0)
X_train = X_train.reshape(-1,1)
X_test = X_test.reshape(-1,1)

#%% Fit linear model
lr = LinearRegression().fit(X_train, y_train)
linear_score = lr.score(X_test, y_test)
print('lr.coef_:  {}'.format(lr.coef_))
print('lr.intercept_: {}'.format(lr.intercept_))

#%% Iterate through to find the best degree
n = 25
deg = np.zeros((n))
poly_score = np.zeros((n))
top_score = 0
for i in np.arange(n):
    deg[i] = i
    poly = PolynomialFeatures(degree = i)
    X_poly = poly.fit_transform(X_train)
    X_poly_test = poly.fit_transform(X_test)
    poly_reg = LinearRegression().fit(X_poly, y_train)
    poly_score[i] = poly_reg.score(X_poly_test, y_test)
    if poly_score[i] > top_score:
        top_degree = i
        top_score = poly_score[i]
    
    # print('Degrees: {}'.format(n))
    # print('poly_reg.coef_:  {}'.format(poly_reg.coef_))
    # print('poly_reg.intercept_: {}'.format(poly_reg.intercept_))
    # print('poly_reg.score_: {}'.format(poly_score))
print('Best Degree: {}  which resulted in a score of {}'.format(top_degree, poly_score[top_degree]))

#%% Plot poly scores
plt.plot(deg, poly_score)
plt.title(label = 'Poly_score by degree')
plt.show()

#%% Create poly model that has highest score
poly = PolynomialFeatures(degree = top_degree)
X_poly = poly.fit_transform(X_train)
poly_reg = LinearRegression().fit(X_poly, y_train)


#%% predict models
x_lin = np.linspace(0,25,100).reshape(-1,1)
x_pol = poly.fit_transform(np.linspace(0,25,100).reshape(-1,1))  # Have to fit_transform x values in order to predict y values!!
y_lin = lr.predict(x_lin)
y_poly = poly_reg.predict(x_pol)

#%% Plot models
plt.scatter(X_train,y_train, label = 'train data', alpha = .4, color = 'blue')
plt.scatter(X_test,y_test, label = 'test data', alpha = .7, color = 'red', marker = 'x')
plt.plot(x_lin, y_lin, label = 'linear, score: {}'.format(linear_score), color = 'Purple', linewidth = 2, alpha = 0.4)
plt.plot(x_lin, y_poly, label = 'poly ({}), score: {}'.format(top_degree, poly_score[top_degree]), color = 'Orange', linewidth = 2, alpha = 0.6)
plt.title(label = 'Linear vs. Poly model w/ best fit for random data')
plt.legend()
plt.show()

#%%
linear_score = lr.score(X_test, y_test)

#%%
