# Django CSV Analyzer with Streamlit Integration

This project is a web application built with Django that allows users to upload CSV files, perform data analysis using pandas and numpy, and display the results and visualizations using Streamlit, all integrated within a Django interface.

## Features

- CSV file upload functionality
- Data analysis using pandas and numpy
- Interactive data visualization with Streamlit
- Django-based web interface

## Requirements

- Python 3.8+
- Django 3.2+
- pandas
- numpy
- matplotlib
- seaborn

## Installation

1. Clone the repository:
git clone https://github.com/yourusername/django-csv-analyzer.git
cd django-csv-analyzer

2. Create a virtual environment and activate it: python -m venv venv

3. Install the required packages: pip install -r requirements.txt 

4. Apply database migrations: python manage.py migrate

5. Run the Django development server: python manage.py runserver

6. Access the application at `http://localhost:8000`

## Usage

1. Navigate to the home page and use the form to upload a CSV file.
2. After uploading, you'll be redirected to the analysis page.
3. The analysis page will display an iframe containing the Streamlit app with various visualizations and analyses of your CSV data.

## Project Structure

Here's a comprehensive README.md file for your project:
markdownCopy# Django CSV Analyzer with Streamlit Integration

This project is a web application built with Django that allows users to upload CSV files, perform data analysis using pandas and numpy, and display the results and visualizations using Streamlit, all integrated within a Django interface.

## Features

- CSV file upload functionality
- Data analysis using pandas and numpy
- Interactive data visualization with Streamlit
- Django-based web interface

## Requirements

- Python 3.8+
- Django 3.2+
- Streamlit 1.0+
- pandas
- numpy
- matplotlib
- seaborn

## Installation

1. Clone the repository:
git clone https://github.com/yourusername/django-csv-analyzer.git
cd django-csv-analyzer
Copy
2. Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
Copy
3. Install the required packages:
pip install -r requirements.txt
Copy
4. Apply database migrations:
python manage.py migrate
Copy
5. Run the Django development server:
python manage.py runserver
Copy
6. Access the application at `http://localhost:8000`

## Usage

1. Navigate to the home page and use the form to upload a CSV file.
2. After uploading, you'll be redirected to the analysis page.
3. The analysis page will display an iframe containing the Streamlit app with various visualizations and analyses of your CSV data.

## Project Structure
django-csv-analyzer/
├── csv_analyzer/          # Django project directory
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── analyzer/              # Django app directory
│   ├── migrations/
│   ├── templates/
│   │   ├── upload.html
│   │   └── analysis.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── streamlit_app.py   # Streamlit application
├── manage.py
├── requirements.txt
└── README.md



