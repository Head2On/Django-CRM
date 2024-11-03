Customer Management System:
A simple Django-based web application to manage customer records. This project allows users to add, update, and view customer information. It tracks who last updated each customer record and provides a clean and easy-to-use interface.

Features:
Add new customer records with details like name, email, phone, address, etc.
Update existing customer records, with user tracking to show who last updated each entry.
User authentication for secure access.

Usage:
Log in as an authenticated user to add or update customer records.
After adding or updating a record, a message displays the user who performed the action.
You will be redirected to the homepage after each add/update.

Project Structure:
models.py: Defines the Customer model.
forms.py: Includes the form for adding and updating customer records.
views.py: Contains the logic for handling add and update operations.
templates/: Contains HTML templates for rendering pages.

License
This project is licensed under the MIT License
