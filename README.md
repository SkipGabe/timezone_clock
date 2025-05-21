# Timezone Clock Django Application

A simple Django web application that displays a ticking clock showing both Eastern Time (EST/EDT) and Pacific Time (PST/PDT) zones. The application features an eye-friendly background and detailed but not overwhelming clock designs.

## Features

- Real-time ticking analog clocks for Eastern and Pacific time zones
- Digital time display for each time zone
- Responsive design
- Soft color scheme that's easy on the eyes

## Installation

1. Clone this repository to your local machine:
   ```
   git clone <repository-url>
   cd timezone_clock
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```
   pip install django
   ```

## Running the Application

1. Start the Django development server:
   ```
   python manage.py runserver
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

## Transferring to Another Device

This application is designed to be portable and can be easily transferred to another device:

1. Copy the entire `timezone_clock` directory to the target device
2. Install Python and Django on the target device
3. Follow the "Running the Application" instructions above

## Project Structure

- `timezone_project/` - Django project settings
- `clock_app/` - The main Django application
- `templates/` - HTML templates for the application
  - `clock.html` - The main clock display template

## Technologies Used

- Django
- HTML/CSS
- JavaScript
- Date and Time APIs