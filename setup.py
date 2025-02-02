from setuptools import setup, find_packages

setup(
    name="digital_footprint",
    version="0.1.0",
    description="Digital Footprint Scanner: Herramienta gratuita para extraer información útil de un correo electrónico.",
    author="Tu Nombre",
    author_email="tuemail@example.com",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "python-whois",
        "dnspython"
    ],
    entry_points={
        "console_scripts": [
            "digital_footprint = digital_footprint.scanner:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
