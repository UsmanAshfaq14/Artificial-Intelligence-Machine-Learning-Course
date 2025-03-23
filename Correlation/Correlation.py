# Import the numpy library
import numpy as np

# Define the dataset
x = np.array([1,3,5,7,8,9, 10, 15])
y = np.array([10, 20, 30, 40, 50, 60, 70, 80])

def Pearson_correlation(X,Y):
	if len(X)==len(Y):
		Sum_xy = sum((X-X.mean())*(Y-Y.mean()))
		Sum_x_squared = sum((X-X.mean())**2)
		Sum_y_squared = sum((Y-Y.mean())**2)	 
		corr = Sum_xy / np.sqrt(Sum_x_squared * Sum_y_squared)
	return corr
			
print(Pearson_correlation(x,y)) 
print(Pearson_correlation(x,x))

#print(np.corrcoef(x, y))


