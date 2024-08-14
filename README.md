# LSTM forecast model
a LSTM model to forecast short-term stock movements using past data and sentiment (obtained from `yfinance` & `newsapi`)

![image](https://github.com/user-attachments/assets/8f767686-4971-4a64-92e8-b64b63c6c226)
![image](https://github.com/user-attachments/assets/1bcda62e-a770-4057-ba76-5ffb140acf27)

## considerations & reflection:
1. scaling
   * min-max was avoided due to strict limit
   * scaling was done all at once which could have caused potential data leakage - instead, fit the `StandardScaler` on only the training data to scale the entire dataset
2. LSTM model
   * used 2 LSTM layers and 2 Dense layers with 20% dropout
   * more optimization could reduce upward/downward bias and overfitting
   * try different number of epochs `epochs=50` and batch sizes `batch_size=32`
3. windowing
   * 20-day window length for a 5-day forecast horizon
   * adjust the window length and data preparation/features for a longer or shorter forecast horizon
4. model evaluation
   * used the mean squared error metric (MSE)
   * could have experimented with other metrics like MAE or RMSE

use at your own risk 
