# Business War-Gaming Simulator

## Overview
This project simulates competitive business strategy outcomes by analyzing market share, revenue, ROI, and innovation metrics across multiple companies. Through interactive scenario modeling and visual analytics, it helps benchmark strategic performance and discover optimal decisions in a simulated environment.

## Project Objective
- Simulate company performance under competitive market conditions.
- Normalize and compare KPIs across companies.
- Visualize strategy effectiveness and ROI using rich analytics.

## Dataset & Inputs
- `business_wargame_simulation.csv` with columns:
  - `company`, `market_share`, `budget`, `revenue`, `marketing_spend`, `rnd_spend`, `profit_margin`, `innovation_score`, `action_taken`

## Technologies Used
- Python, Pandas, Seaborn, Matplotlib

## How to Run
```bash
pip install pandas matplotlib seaborn
python war_game_simulator.py
```

## Workflow
1. Load and normalize KPIs
2. Calculate ROI and performance metrics
3. Create visual analytics for strategic insights
4. Generate company leaderboard and summary

## Results
- ROI distribution per strategy
- Company-wise performance comparison
- Strategy frequency patterns

## Key Takeaways
- Visualizes strategic impact clearly.
- Highlights high-ROI and high-innovation companies.
- Identifies which strategies lead to growth.

## Future Enhancements
- Add time-series tracking per round.
- Implement game logic for automated move simulation.
- Integrate a dashboard UI for interactive exploration.
