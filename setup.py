from setuptools import setup, find_packages

setup(
    name="bettery-alert",
    version="0.0.1",
    author="Felipe Castro",
    author_email="felipe.castro@pinnsystem.com",
    description="Tool to alert about battery levels",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/castroofelipee/battery-alert",
    packages=find_packages(),
    install_requires=[
        "psutil",
        "plyer",
    ],
    entry_points={
        "console_scripts": [
            "bettery-alert=battery_alert.core:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)