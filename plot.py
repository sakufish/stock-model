import matplotlib.pyplot as plt
import numpy as np

def plot_history(history):
    loss = history.history['loss']
    val_loss = history.history.get('val_loss', [])

    plt.figure(figsize=(10, 6))
    plt.plot(loss, label='Training Loss')
    plt.plot(val_loss, label='Validation Loss')

    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title('Model Training!')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_window(X_test_rescaled, y_pred_rescaled, y_test_rescaled, window_index):
    past_prices = X_test_rescaled[window_index, :, 0]
    forecast_prices = y_pred_rescaled[window_index]
    actual_prices = y_test_rescaled[window_index]
    
    time_past = np.arange(len(past_prices))
    time_forecast = np.arange(len(past_prices), len(past_prices) + len(forecast_prices))
    
    plt.figure(figsize=(14, 7))
    plt.plot(time_past, past_prices, label='past close price', color='blue')
    plt.plot(time_forecast, forecast_prices, linestyle='--', label='forecasted prices', color='red')
    plt.plot(time_forecast, actual_prices, label='actual Prices', color='green')

    plt.plot([time_past[-1], time_forecast[0]], [past_prices[-1], forecast_prices[0]], color='red', linestyle='--')
    plt.plot([time_past[-1], time_forecast[0]], [past_prices[-1], actual_prices[0]], color='green')
    
    plt.xlabel('days past', color='white')
    plt.ylabel('close price', color='white')
    plt.title('sample forecast', color='white')
    plt.legend()
    plt.grid(True, color='white', linestyle='--', linewidth=0.5)

    ax = plt.gca()
    ax.set_facecolor('black')
    ax.spines['top'].set_color('white')
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.title.set_color('white')
    ax.tick_params(axis='both', colors='white')
    
    ax.xaxis.set_tick_params(labelcolor='white')
    ax.yaxis.set_tick_params(labelcolor='white')
    plt.gcf().patch.set_facecolor('black') 
   
    plt.show()