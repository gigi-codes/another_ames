### gxcodes@pm.me #### March 2022
# 3rd MODULE, 2 FUNCTIONS
	# scrubber(df)
	# allmet(X,y)

# ----------
# scrubber 
# ----------
# takes 1 arg: imported df 
# runs preliminary cleaning
# does NOT take any actions with NaN, nulls, etc. 
# merely visualizes and returns descriptors 



# ----------
# allmet
# ----------
# takes 2 args: clean, numeric, dummified (X, y)
# runs linear model, prints and returns 6 errors and y_hat
# checks LINE assumptions, returns plots 
# Runs Ridge and LASSO regularization, prints and returns metrics


##### IMPORTS #####  --- --- --- --- --- --- --- --- --- --- --- ---
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('gstyle.mplstyle') 

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge, RidgeCV
from sklearn.linear_model import Lasso, LassoCV

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn import metrics        					

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures


##### FUNCTION 1: scrubber #####    --- --- --- --- --- --- --- --- --- --- ---
def scrubber(a_df): 
	a_df.head()
	a_df.describe()
	a_df.info()
	a_df.isnull().sum()
	a_df.value_counts()
	a_df.isunique()
	a_df.nunique()
	returns ('Done.')

##### FUNCTION 2: allmet #####  --- --- --- --- --- --- --- --- --- --- --- ---
def allmet(X,y):

	X = X
	y = y 
	
	# making model 
	X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42, train_size = 0.7)
	lr = LinearRegression() 
	lr.fit(X_train, y_train)
		
	# making predictions to get residuals  
	predictions = lr.predict(X)
	residuals = y - predictions
	
	# errors 
	rss = round((residuals **2).sum(), 4)									# rss = sse 
	max_e = round(metrics.max_error(y, predictions)  , 4)					# max error
	rmse = round(np.sqrt(metrics.mean_squared_error(y, predictions)), 4)    # root mean squared error
	mae = round(metrics.mean_squared_error(y, predictions),4)               # mean absolute error
	mse = round(metrics.mean_squared_error(y, predictions),4)               # mean squared error  
	r2 = round(metrics.r2_score(y, predictions), 4)                        	# coefficient of determination
	r2xval = round(cross_val_score(lr, X, y).mean(), 4)						# X-val score
	
	my_metrics_s = ['R2', 'RSS', 'MAX_E', 'RMSE', 'MAE', 
		'MSE', 'Intercept', 'Slope', 'R2 X-Val']
	my_metrics = [r2, rss, max_e, rmse, mae, mse, intercept, slope, r2xval ]
	
	lr_df = pd.DataFrame({
	'Metric':	my_metrics_s,
	'Value':	my_metrics})
			
	
	# --- LINE checks, plots with help from Jessely --- --- --- --- --- ---
	
	fig, ax = plt.subplots(nrows=1, ncols=3, sharey=False, figsize=(15, 6))
	fig.suptitle('LINE Checks')
	
	# linearity
	ax[0].set(xlabel='Target (Actual Price, $)', ylabel='Predictions')
	sns.scatterplot(x= y , y=predictions, ax = ax[0], color = 'lightcoral').set(title='Linearity');
	
	#normality 
	ax[1].set(xlabel='Frequency', ylabel='Residuals')
	sns.histplot(x = residuals, ax = ax[1], color = 'lightcoral', bins = 50).set(title = 'Normality');
	
	# equal variance
	ax[2].set(xlabel='Target', ylabel='Residuals')
	sns.scatterplot(x= y , y = residuals, ax = ax[2], color = 'lightcoral').set(title = 'Equal Variance');
	
		
	# --- Ridge, LASSO with help from Katrin --- --- --- --- --- --- --- ---

	sc = StandardScaler()
	Z_train = sc.fit_transform(X_train)
	Z_test = sc.transform(X_test)

	# Cross-validate over our list of ridge alphas.
	r_alphas = np.logspace(0, 5, 100)
	ridge_cv = RidgeCV(alphas = r_alphas, scoring = 'r2', cv = 5)

	# Fit model using best ridge alpha
	ridge_cv.fit(Z_train, y_train);

	# Cross-validate over our list of Lasso alphas.
	l_alphas = np.logspace(-3, 0, 100)	
	lasso_cv = LassoCV(alphas = l_alphas, cv = 5, max_iter = 50_000, n_jobs = -1)

	# Fit model using best lasso alpha!
	lasso_cv.fit(Z_train, y_train);
	
	
	# Ridge & LASSSO scores: 
	rl_metrics_s = ['Ridge Train', 'Ridge Test', 'LASSO Train', "LASSO Test"]
	rl_metrics = [ridge_cv.score(Z_train, y_train), ridge_cv.score(Z_test, y_test), lasso_cv.score(Z_train, y_train), lasso_cv.score(Z_test, y_test)]
	rl_rs = [list(zip(rl_metrics_s, rl_metrics))]
		
	rl_df = pd.DataFrame({
	'Metric': rl_metrics_s,
	'Value': rl_metrics})


	# --- PRINT METRICS  --- --- --- --- --- --- --- ---	
	print('Linear Regression Metrics')	# Prints OLR Metrics
	print(lr_df)

	print('Ridge and LASSO Scores')		# Prints RIDGE and LASSO Scores	
	print(rl_df)
	
	return lr_df, rl_df, predictions