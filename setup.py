from setuptools import setup, find_packages

setup(
    name="tbot",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "python-binance",
        "streamlit",
        "python-dotenv",
    ],
)
