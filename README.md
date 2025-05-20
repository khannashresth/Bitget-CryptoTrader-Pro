# Bitget CryptoTrader Pro

A professional cryptocurrency trading bot that implements automated trading strategies on the Bitget exchange. The bot supports both demo and live trading modes, featuring real-time market data processing, technical analysis, and risk management.

## Features

- Real-time market data processing
- Technical analysis indicators (RSI, MACD)
- Risk management system
- Demo and live trading modes
- Web dashboard for monitoring
- Automated trade execution
- Position sizing and portfolio management

## Prerequisites

- Python 3.8 or higher
- Bitget exchange account (for live trading)
- API credentials from Bitget

## Installation

1. Clone the repository:
```bash
git clone https://github.com/khannashresth/bitget-cryptotrader-pro.git
cd bitget-cryptotrader-pro
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Copy the configuration template:
```bash
cp config.yaml.template config.yaml
```

5. Edit `config.yaml` with your Bitget API credentials and trading preferences.

## Usage

1. Start the trading engine:
```bash
python src/trading/bitget_engine.py
```

2. Launch the dashboard:
```bash
streamlit run src/dashboard.py
```

## Configuration

Edit `config.yaml` to customize:
- API credentials
- Trading pairs
- Strategy parameters
- Risk management settings
- Update intervals

## Project Structure

```
src/
├── data/           # Market data handling
├── strategy/       # Trading strategies
├── risk/          # Risk management
├── trading/       # Trading engine
└── dashboard/     # Web interface
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This software is for educational purposes only. Do not risk money which you are afraid to lose. USE THE SOFTWARE AT YOUR OWN RISK. THE AUTHORS AND ALL AFFILIATES ASSUME NO RESPONSIBILITY FOR YOUR TRADING RESULTS. 
