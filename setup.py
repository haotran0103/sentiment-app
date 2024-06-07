from setuptools import setup, find_packages

setup(
    name="textSentiments",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "transformers",
        "datasets",
        "pandas",
        "pyyaml",
    ],
)
