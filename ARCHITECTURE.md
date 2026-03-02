## System Overview

```text
                ┌──────────────────────────┐
                │   Binance Futures API    │
                └─────────────┬────────────┘
                              ↓
                ┌──────────────────────────┐
                │   Data Collection Layer  │
                └─────────────┬────────────┘
                              ↓
                ┌──────────────────────────┐
                │ Feature Engineering      │
                │ (Technical Indicators,   │
                │  Rolling Stats, Lags)    │
                └─────────────┬────────────┘
                              ↓
                ┌──────────────────────────┐
                │ Parquet Dataset Storage  │
                │ (Row-Group Streaming)    │
                └─────────────┬────────────┘
                              ↓
                ┌──────────────────────────┐
                │  TCN Training Pipeline   │
                │ (Custom Loss Functions)  │
                └─────────────┬────────────┘
                              ↓
                ┌──────────────────────────┐
                │   Trained Model (.keras) │
                └─────────────┬────────────┘
                              ↓
                ┌──────────────────────────┐
                │ Real-Time Inference      │
                │ (Rolling Window Engine)  │
                └─────────────┬────────────┘
                              ↓
                ┌──────────────────────────┐
                │ Risk Management Engine   │
                │ (TP / SL / Break-even)   │
                └─────────────┬────────────┘
                              ↓
                ┌──────────────────────────┐
                │ Order Execution Layer    │
                │ + Time Synchronization   │
                └──────────────────────────┘
```

---

## Core Components

### 1) Data Collection Layer

* Pulls historical and live OHLCV data from Binance Futures.
* Supports multiple timeframes.
* Handles rate limiting and batching.

---

### 2) Feature Engineering Layer

* Computes technical indicators (RSI, MACD, Bollinger Bands, ATR, etc.).
* Rolling statistics and volatility measures.
* Lag features and candle structure features.
* Generates normalized model-ready feature sets.

---

### 3) Model Training Layer

* Temporal Convolutional Network (TCN) architecture.
* Multi-target forecasting (High / Low / Close).
* Custom trading-aware loss functions.
* Large-scale Parquet streaming for memory efficiency.

---

### 4) Inference Engine

* Loads trained model.
* Builds rolling feature windows in real time.
* Produces forward price projections.
* Converts predictions into directional bias signals.

---

### 5) Risk Management Engine

* Position sizing logic.
* Adaptive leverage handling.
* Dynamic Take-Profit / Stop-Loss.
* Break-even fallback logic.
* ROI-based monitoring.

---

### 6) Order Execution System

* Market and limit order handling.
* Position monitoring and adjustment.
* Conditional order management.
* Server timestamp synchronization to prevent API drift errors.
* Continuous loop monitoring of active trades.

---

## Infrastructure Considerations

* Binance server time synchronization for accurate request signing.
* Modular separation of training and execution environments.
* Parquet row-group streaming for large dataset efficiency.
* Environment-based configuration management.
* Fault tolerance and exception handling during live trading.

---

## Source Code Notice

The full training pipeline, feature engineering engine, and live trading execution logic are proprietary and not publicly available.

This repository showcases system architecture and design approach only.



You’re building this the right way now.
