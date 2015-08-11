from setuptools import setup

install_requires = [
    'numpy',
]

tests_require = [
    'coverage',
    'nose',
    'flake8',
]


setup(
    name='barcode-scanner',
    version='0.0.0',
    description='to detect, isolate, parse, and process barcodes',
    install_requires=install_requires,
    author='Marco Ceppi',
    author_email='marco@ceppi.net',
    url="https://github.com/petrolpad/barcode-scanner",
    packages=['barcodescanner'],
)
