# Calculator
## Table of Contents
* [General Information](#general-information)
* [Technologies Used](#technologies-used)
* [Installation](#installation)
* [Usage](#usage)
* [Features](#features)
* [Project Status](#project-status)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
* [License](#license)

## General Information
This calculator can be used for simple arithmetic operations. Check [features](#features) of this calculator for details.

## Technologies Used
Python - version 3.8

## Installation
Use the package installer [pip](https://pip.pypa.io/en/stable/) to install calculator.
```python
!pip install git+https://github.com/fortune-uwha/tc_calculator

from calculator.calculator import Calculator
```

## Usage
```python
calculator = Calculator()
calculator.add(12)
calculator.subtract(3)
calculator.divide(3)
calculator.nroot(3)
calculator.reset_memory()
```

## Features
* Addition / Subtraction
* Multiplication / Division
* Take (n) root of number
* Reset memory: Stores results in memory until reset

## Project Status
Project is: complete

## Acknowledgements
This project was based on [Turing College](https://www.turingcollege.com) learning on Software testing, licensing and documentation.

## Contact
Created by [@fortune_uwha](https://fortune-uwha.github.io/Fortune_Portfolio/) - feel free to contact me!

## License
This project is open source and available under the terms of the [MIT](https://opensource.org/licenses/MIT) license.
