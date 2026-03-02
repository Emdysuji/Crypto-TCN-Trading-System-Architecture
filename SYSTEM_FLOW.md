## Example Trade Flow

1) Fetch latest 3m candles
2) Compute engineered features
3) Scale features
4) Build rolling window
5) Predict future High/Low/Close log-returns
6) Convert to price targets
7) Evaluate long/short bias
8) Apply risk filters
9) Execute trade
10) Monitor ROI
11) Adjust stop-loss dynamically

## ✅ example_prediction_output.json
```json
{
  "symbol": "BTCUSDT",
  "timeframe": "3m",
  "current_price": 65200.50,
  "predicted_high": 65420.12,
  "predicted_low": 64980.33,
  "predicted_close": 65280.40,
  "long_bias_probability": 0.64,
  "short_bias_probability": 0.36
}
```
