from setuptools import setup, find_packages

setup(
    name="crypto_trading_bot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "ccxt>=4.0.0",
        "pandas>=1.5.0",
        "numpy>=1.21.0",
        "scikit-learn>=1.0.0",
        "ta>=0.10.0",
        "streamlit>=1.22.0",
        "plotly>=5.13.0",
        "pyyaml>=6.0",
        "python-dotenv>=0.19.0",
        "requests>=2.28.0",
        "joblib>=1.2.0"
    ],
) 