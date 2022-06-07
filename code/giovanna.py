# FIRST CUSTOM MODULE: shared with peers

# runs OLR and returns 6 errors. 
# takes in (clean, numeric) X, y, where X has been dummified already. 

import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn import metrics        					

def allmet(X,y):

	X = X
	y = y 
	
	# making model 
	X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42)
	lr = LinearRegression() 
	lr.fit(X_train, y_train)
	
	intercept = lr.intercept_
	slope = lr.coef_[0]
	
	# making predictions to get residuals  
	predictions = lr.predict(X)
	residuals = y - predictions
	
	# errors 
	rss = (residuals **2).sum()                                     # rss = sse 
	max_e = metrics.max_error(y, predictions)                       # max error
	rmse = np.sqrt(metrics.mean_squared_error(y, predictions))      # root mean squared error
	mae = metrics.mean_squared_error(y, predictions)                # mean absolute error
	mse = metrics.mean_squared_error(y, predictions)                # mean squared error    #mse = rss/len(residuals)
	r2 = metrics.r2_score(y, predictions)                           # coefficient of determination
	
	my_metrics_s = ['r2', 'rss', 'max_e', 'rmse', 'mae', 'mse']
	my_metrics = [r2, rss, max_e, rmse, mae, mse]
	
	list_out = list(zip(my_metrics_s, my_metrics))
	
	return list_out
    #return my_metrics