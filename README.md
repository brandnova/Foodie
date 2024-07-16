# Foodie

Welcome to **Foodie**, a food ordering web app designed to streamline the order processing and account-keeping for lounges and eateries.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Usage](#usage)
- [Contact](#contact)

## Introduction

Foodie is a minimalistic yet fully functional food ordering web app that provides a seamless self-service experience for customers while enhancing the workflow and reducing stress for admins. Built on the robust Django framework that the on Python programming language, Foodie offers complete control over operations, ensuring smooth and efficient management.

## Features

- **Online Payment Options**: Secure and convenient payment processing.
- **Direct Bank Transfer Payment Option**: Flexibility for all your customers.
- **Menu Browsing**: Easy navigation through your offerings.
- **Cart Functions**: Simple and efficient order management.
- **User Registration and Login**: Hassle-free user experience.
- **Create an Order to Pay Later**: Flexibility for your customers.
- **Email Notifications**: Keep customers informed about their order status.
- **Admin Control**: Full control over operations for admins, built on Django framework.

## Screenshots

### Landing Page
![Landing Page](images/landing_page.png)

### User Dashboard
![User Dashboard](images/user_dashboard.png)

### Menu Page
![Menu Page](images/menu_page.png)

### Cart Page
![Cart Page](images/cart_page.png)

### Admin Dashboard
![Admin Dashboard](images/admin_dashboard.png)


# Django Installation and Setup Guide (Offline)

This guide will walk you through the process of installing and running this scripts on your local PC.

## Prerequisites

Before you begin, ensure that you have the following installed on your system:

- [Python](https://www.python.org/downloads/): (version 3.6 or higher).
- pip (Python package manager - Usually comes with Python)

## Installation Steps

1. **Create a Virtual Environment**: It's recommended to create a virtual environment to manage the project dependencies. Open your terminal or command prompt and run the following command:
   ```
   python -m venv myenv
   ```
   Replace `myenv` with the name you want to give to your virtual environment.

2. **Activate the Virtual Environment**: Navigate to the directory where you created your virtual environment and activate it. Run the following command:
   - On Windows:
     ```
     myenv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source myenv/bin/activate
     ```

3. **Install Django**: Once your virtual environment is activated, use pip to install Django. Run the following command:
   ```
   pip install django
   ```

## Running the Django Scripts

Now that you have Django installed, you can now clone this repository and run the Django scripts on your localhost server.


1. **Clone the repository**:
    ```sh
    git clone https://github.com/brandnova/Foodie.git
    cd foodie
    ```

2. **Install the project dependencies**: In your terminal, run the following command:
   ```
   pip install -r requirements.txt
   ```

3. **Navigate to the Project Directory**: Change into the directory of the Django project:
   ```
   cd foodie 
   ```

4. **Run the Development Server**: Start the Django development server by running the following command:
   ```
   python manage.py runserver
   ```

5. **Access the Local Development Server**: Once the server is running, open your web browser and navigate to `http://127.0.0.1:8000/` or `http://localhost:8000/` to view the Django project.

6. **Add Menus and Items**: Populate the app with menus and items.
7. **User Registration**: Users can register and log in to place orders.
8. **Order Processing**: Users can browse the menu, add items to their cart, and place orders.
9. **Payment Options**: Users can choose between online payment and direct bank transfer.
10. **Order Tracking**: Users receive email notifications about their order status.

## Additional Resources

- [Project Sample](https://foodie.coursearena.com.ng): View a live sample of the project.

- [My portfolio](https://brandnova.github.io): Visit my portfolio website to contact me.


---
