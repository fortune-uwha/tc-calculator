import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='calpy',
    version='0.0.1',
    license='MIT',
    description='This calculator can be used for simple arithmetic operations.',
    author='Fortune Uwha',
    author_email='fortune.uwha@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/fortune-uwha/calculator',
    download_url='https://github.com/fortune-uwha/calculator/archive/refs/tags/v0.1.tar.gz',
    packages=setuptools.find_packages(),
    keywords=['calculator', 'maths', 'arithmetic'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires=">=3.6",
)
