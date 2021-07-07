import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='calpython',
    version='0.0.2',
    license='MIT',
    description='Calculator package for simple arithmetic operations.',
    author='Fortune Uwha',
    author_email='fortune.uwha@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/fortune-uwha/tc_calculator',
    download_url='https://github.com/fortune-uwha/tc_calculator/archive/refs/tags/v0.0.2.tar.gz',
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
