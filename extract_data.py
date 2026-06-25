import pandas as pd 
import numpy as np

messy_data = {
    'ODERID' :[ 101,102, 103 , 104 , 105] ,
    'PRODUCT':['apple', 'banana', 'kewi' , 'mango', 'orange'],
    'Price': ['1200.50', '25.00', '45.99', 'Not Available', '25.00'],
    'Quantity': [1, 2, 1, np.nan, 3]
}


df = pd.DataFrame(messy_data)
df.to_csv('messy.csv', index=False)

print ("file is ready" )