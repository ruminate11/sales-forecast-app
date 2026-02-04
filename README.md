# 📈 Sales Forecasting & Inventory Optimization

## Problem
Godrej faces seasonal demand spikes for ACs and furniture.
Stockouts cause lost sales, excess stock increases carrying costs.

## Solution
Built SARIMA-based forecasting tool to:
- predict next month demand
- calculate reorder point
- optimize inventory planning

## Stack
Python, Statsmodels, Flask, Pandas

## Steps
1. Generate sales dataset
2. Train SARIMA model
3. Forecast demand
4. Calculate reorder point

## Formula
ROP = (Lead Time × Avg Daily Sales) + Safety Stock

## Business Impact
- Reduces stockouts
- Minimizes warehouse carrying cost
- Improves supply chain planning
