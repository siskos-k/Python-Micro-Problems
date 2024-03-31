## Online R compiler to run R program online
## Print "Try programiz.pro" message
# install.packages("forecast")
# Install the 'vars' package (if not already installed)
# install.packages("vars")

# Load the 'vars' package
library(vars)
library(forecast)
sales_data <- c(100, 110, 120, 115, 125, 130, 135, 140, 145, 150)

# Assuming you want to create a time series object from the sales data
# You can use the ts() function to create a time series
differenced_real_sales_ts <- ts(sales_data, start = c(2020, 1), frequency = 1)
interest_rate_data <- c(5.1, 5.3, 5.2, 5.5, 5.4, 5.6, 5.7, 5.8, 5.9, 6.0)

# Assuming you want to create a time series object from the interest rate data
# You can use the ts() function to create a time series
diff_real_interest_rate_ts <- ts(interest_rate_data, start = c(2020, 1), frequency = 1)
industrial_production_data <- c(120, 125, 128, 122, 130, 135, 132, 138, 140, 145)

# Assuming you want to create a time series object from the industrial production data
# You can use the ts() function to create a time series
diff_real_industrial_production_ts <- ts(industrial_production_data, start = c(2020, 1), frequency = 1)
cpi_data <- c(120, 125, 128, 122, 130, 135, 132, 138, 140, 145)

# Assuming you want to create a time series object from the CPI data
# You can use the ts() function to create a time series
diff_cpi_ts <- ts(cpi_data, start = c(2020, 1), frequency = 1)

# Now, you can use diff_real_interest_rate_ts in your subsequent code
# Now, you can use differenced_real_sales_ts in your subsequent code
# For example, you can use it with auto.arima function
# Note: This example assumes the 'forecast' package is loaded
library(forecast)
arima_model <- auto.arima(differenced_real_sales_ts)

# Print the ARIMA model summary
print(summary(arima_model))
arima_models <- list(
  auto.arima(differenced_real_sales_ts),
  auto.arima(differenced_real_sales_ts, xreg = diff_real_interest_rate_ts),
  auto.arima(differenced_real_sales_ts, xreg = diff_real_industrial_production_ts),
  auto.arima(differenced_real_sales_ts, xreg = diff_cpi_ts)
)

tslm_models <- list(

  tslm(differenced_real_sales_ts ~ diff_real_interest_rate_ts + diff_real_industrial_production_ts),
  tslm(differenced_real_sales_ts ~ diff_real_interest_rate_ts + diff_cpi_ts),
  tslm(differenced_real_sales_ts ~ diff_real_industrial_production_ts + diff_cpi_ts),
  tslm(differenced_real_sales_ts ~ diff_real_interest_rate_ts + diff_real_industrial_production_ts + diff_cpi_ts)
)

var_models <- list(
  VAR(cbind(differenced_real_sales_ts, diff_real_interest_rate_ts, diff_real_industrial_production_ts, diff_cpi_ts), p = 1),
  VAR(cbind(differenced_real_sales_ts, diff_real_interest_rate_ts, diff_real_industrial_production_ts, diff_cpi_ts), p = 2),
  VAR(cbind(differenced_real_sales_ts, diff_real_interest_rate_ts, diff_real_industrial_production_ts, diff_cpi_ts), p = 3),
  VAR(cbind(differenced_real_sales_ts, diff_real_interest_rate_ts), p = 1),
  VAR(cbind(differenced_real_sales_ts, diff_cpi_ts), p = 1),
  VAR(cbind(differenced_real_sales_ts, diff_real_industrial_production_ts), p = 1),
  VAR(cbind(differenced_real_sales_ts, diff_real_interest_rate_ts), p = 2),
  VAR(cbind(differenced_real_sales_ts, diff_cpi_ts), p = 2),
  VAR(cbind(differenced_real_sales_ts, diff_real_industrial_production_ts), p = 2),
  VAR(cbind(differenced_real_sales_ts, diff_real_interest_rate_ts), p = 3),
  VAR(cbind(differenced_real_sales_ts, diff_cpi_ts), p = 3),
  VAR(cbind(differenced_real_sales_ts, diff_real_industrial_production_ts), p = 3),
  VAR(cbind(differenced_real_sales_ts, diff_real_industrial_production_ts, diff_real_interest_rate_ts), p = 1),
  VAR(cbind(differenced_real_sales_ts, diff_cpi_ts, diff_real_interest_rate_ts), p = 1),
  VAR(cbind(differenced_real_sales_ts, diff_cpi_ts, diff_real_industrial_production_ts), p = 1),
  VAR(cbind(differenced_real_sales_ts, diff_real_industrial_production_ts, diff_real_interest_rate_ts), p = 2),
  VAR(cbind(differenced_real_sales_ts, diff_cpi_ts, diff_real_interest_rate_ts), p = 2),
  VAR(cbind(differenced_real_sales_ts, diff_cpi_ts, diff_real_industrial_production_ts), p = 2),
  VAR(cbind(differenced_real_sales_ts, diff_real_industrial_production_ts, diff_real_interest_rate_ts), p = 3),
  VAR(cbind(differenced_real_sales_ts, diff_cpi_ts, diff_real_interest_rate_ts), p = 3),
  VAR(cbind(differenced_real_sales_ts, diff_cpi_ts, diff_real_industrial_production_ts), p = 3)
)
library(forecast)
library(vars)

# Assuming you have an actual time series `actual_ts` that corresponds in length and time to your predictions
# Make sure to replace actual_ts with your actual time series data

# Define your actual time series data
# Make sure to replace actual_ts with your actual time series data

# Define your actual time series data
# Make sure to replace actual_ts with your actual time series data
library(forecast)
library(vars)

# Assuming you have an actual time series `actual_ts` that corresponds in length and time to your predictions
# Make sure to replace actual_ts with your actual time series data
actual_ts <- c(160, 170, 180, 175, 185, 190, 195, 200, 205, 210)

# Define a function to calculate RMSE
calculate_rmse <- function(predictions, actual) {
  sqrt(mean((predictions - actual)^2))
}

# Initialize a vector to store RMSE values
rmse_values <- numeric()
# Loop through ARIMA models
for (i in seq_along(arima_models)) {
  model <- arima_models[[i]]
  # Check if the model has regressors
  if (is.null(attr(model$arma, "xreg"))) {
    # Forecast without regressors
    predictions <- forecast(model, h = length(actual_ts))$mean
  } else {
    # Forecast with regressors
    predictions <- forecast(model, newdata = data.frame(diff_real_interest_rate_ts = diff_real_interest_rate_ts))$mean
  }
  # Calculate RMSE
  rmse_values <- c(rmse_values, calculate_rmse(predictions, actual_ts))
}

# Loop through ARIMA models <- c(rmse_values, calculate_rmse(predictions, actual_ts))


# Loop through TSLM models
for (model in tslm_models) {
  # Forecast using the model
  predictions <- forecast(model, newdata = data.frame(diff_real_interest_rate_ts = diff_real_interest_rate_ts, diff_real_industrial_production_ts = diff_real_industrial_production_ts, diff_cpi_ts = diff_cpi_ts))$mean
  # Calculate RMSE
  rmse_values <- c(rmse_values, calculate_rmse(predictions, actual_ts))
}

# Loop through VAR models
for (model in var_models) {
  # Forecast using the model
  if (length(model$varresult) == 1) {
    # If only one series in VAR model
    predictions <- predict(model, n.ahead = length(actual_ts))$fcst
  } else {
    # If multiple series in VAR model
    predictions <- predict(model, n.ahead = length(actual_ts), dumvar = list(diff_real_interest_rate_ts = diff_real_interest_rate_ts, diff_real_industrial_production_ts = diff_real_industrial_production_ts, diff_cpi_ts = diff_cpi_ts))$fcst
  }
  # Assuming 'differenced_real_sales_ts' is the first series in your VAR models
  predicted_values <- predictions[,1] # Selecting the first series' predictions
  
  # Calculate RMSE
  rmse_values <- c(rmse_values, calculate_rmse(predicted_values, actual_ts))
}

# Print RMSE values
print(rmse_values)
