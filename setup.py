from setuptools import setup, find_packages

setup(
    name="password-manager",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "click"
    ],
    entry_points={
        "console_scripts": {
            "pwm=app.main:main"
        }
    }
)