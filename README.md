# Coffee Shop Management (OOP in Python)

## Overview

A simple coffee shop management system using Object-Oriented Programming (OOP) in Python. It includes three main classes: **Customer**, **Coffee**, and **Order**.

### Model Relationships:

- **Customer**: Can have multiple orders.
- **Coffee**: Can appear in multiple orders.
- **Order**: Links a customer with a coffee.

## Features

- Manage customers and their orders.
- Track coffee types, their orders, and calculate average prices.
- Ensure data integrity when linking customers to coffee orders.

## Setup

### Requirements:

- Python3
- Text editor/IDE (VS Code, PyCharm, etc.)

### Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/KIPTOO-JOB/cofeeShop.git
   ```

# Project Structure

Organize your project files and folders as follows:

### Project Files:

- **models/**: Contains the classes representing the Coffee, Customer, and Order models.
- **venv/**: Virtual environment folder to manage dependencies.
- **requirements.txt**: List of required Python packages (optional).
- **README.md**: Documentation and setup instructions.

### Virtual Environment Setup:

1. Create the virtual environment:
   ```bash
   python3 -m venv venv
   ```

### License

This project is licensed under the MIT License - see the LICENSE file for details.
