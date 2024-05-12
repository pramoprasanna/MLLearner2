import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
import pickle


# SOURCING DATA
housing = fetch_california_housing()
print(housing.target_names)
print(housing.feature_names)
print(housing.data[0])

""" print(housing.keys())
    print(housing.data)
    print(housing.target)
    print(housing.frame)
    print(housing.target_names)
    print(housing.feature_names)
    print(housing.DESCR)
"""

#PREPARING DATA
dataset=pd.DataFrame(housing.data, columns=housing.feature_names)
dataset['Price'] = housing.target

#DATA VALIDATION

""" print(dataset.head())
    #DATA TYPE OF FEATURES
    print(dataset.info())
    #SUMMARIZING STATS OF DATA
    print(dataset.describe())
    #MISSING VALUES CHCEK
    print(dataset.isnull().sum())
"""

#EDA
#Linear Regression - Correlation , Multicorrelation
""" print(dataset.corr())
    sns.pairplot(dataset)
    plt.show()
    
    plt.scatter(dataset['MedInc'], dataset['Price'])
    plt.xlabel("Median Income")
    plt.ylabel("Price")
    plt.show()
    
    sns.regplot(x="AveRooms", y="Price", data=dataset)
    plt.show()
"""

#DEPENDENT AND INDEPENDENT FEATURES SPLIT
X = dataset.iloc[:, :-1]
Y = dataset.iloc[:, -1]
#print(Y)

#TRAIN and TEST SPLIT
X_Train, X_Test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3)
#print(X_Train, Y_test)

#STANDARDIZE DATASET
scaler = StandardScaler()
X_Train = scaler.fit_transform(X_Train)
X_Test = scaler.transform(X_Test)

pickle.dump(scaler,open('scaling.pkl','wb'))

#MODEL BUILDING
regression = LinearRegression()
regression.fit(X_Train, Y_train)

#print Coefficient and intercept
#print(regression.coef_,regression.intercept_)

#Parameter on which model is trained
#print(regression.get_params())

#PREDICTION

reg_pred = regression.predict(X_Test)
#print(reg_pred)

#PLOT FOR PREDICTION
plt.scatter(Y_test, reg_pred)
#plt.show()

#Residuals
residuals = Y_test - reg_pred
#Plot Residuals
sns.displot(residuals, kind="kde")
plt.scatter(reg_pred, residuals)# uniform distribution
#plt.show()

#PERFORMANCE METRICS
#print(mean_absolute_error(Y_test, reg_pred))
#print(mean_squared_error(Y_test, reg_pred))
#print(np.sqrt(mean_squared_error(Y_test, reg_pred)))

# R Square and Adjusted R Square
score = r2_score(Y_test, reg_pred)
print(score)
print(1 - (1- score)*(len(Y_test) - 1) / (len(Y_test)- X_Test.shape[1]-1))
# Predict for one single record
print(regression.predict(scaler.transform(housing.data[0].reshape(1, -1))))

#PICKLING THE MODEL FOR DEPLOYMENT

pickle.dump(regression,open('regmodel.pkl','wb'))

#LOAD PICKLED FILE
pickled_model = pickle.load(open('regmodel.pkl', 'rb'))

print(pickled_model.predict(scaler.transform(housing.data[0].reshape(1, -1))))
