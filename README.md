# Quiz App with Django and MySQL

This project is a simple quiz application built using the *Django framework* and *MySQL database*. The app allows users to take multiple-choice quizzes, track their performance, and view their results on a dashboard.

## Features

1. *Dashboard Page*:
   - Displays the user's total questions attempted, correct answers, and overall score percentage.
   - A button to start a new quiz.

2. *Quiz Page*:
   - Displays a random multiple-choice question from the database.
   - Allows the user to select an answer and submit it.
   - Provides feedback on whether the answer is correct or incorrect, along with the correct answer if needed.
   - Options to answer more questions or end the quiz.

3. *Database*:
   - Stores pre-populated multiple-choice questions.
   - Tracks user performance metrics such as total attempts and correct answers.

## Technology Stack

- *Backend*: Django (Python)
- *Database*: MySQL
- *Frontend*: HTML, CSS (with Django templates)

## Setup Instructions

### Prerequisites

- Python 3.8+
- Django 4.0+
- MySQL database
- pip (Python package manager)

### Installation Steps

### Installation Steps (Windows)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Rakshathganiga/Quiz-App.git
   cd QuizApp
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv myenv
   myenv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   - Create a new MySQL database (e.g., `quiz_app_db`).
   - Update the database settings in `settings.py`:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'quiz_app_db',
             'USER': '<your-username>',
             'PASSWORD': '<your-password>',
             'HOST': '127.0.0.1',
             'PORT': '3306',
         }
     }
     ```

5. **Apply database migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Pre-populate the database with questions**:
   - Add sample questions using the Django admin panel or a data migration script.

7. **Run the server**:
   ```bash
   python manage.py runserver
   ```
   - Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser to access the app.


## Usage

1. Navigate to the *Dashboard Page* to view your performance metrics and start a quiz.
2. On the *Quiz Page*, answer a random question and submit your answer.
3. After answering, review the feedback and choose to either continue or end the quiz.
4. Return to the *Dashboard Page* to see your updated performance metrics.

## Project Structure

```
Quiz_App/
├── Quiz_App/             # Main Django project folder
│   ├── settings.py       # Django settings file
│   ├── urls.py           # URL routing
│   ├── wsgi.py           # WSGI configuration
├── quiz/                 # App folder containing core functionality
│   ├── models.py         # Database models
│   ├── views.py          # View logic
│   ├── Templates/        # HTML templates
│   ├── admin.py          # Admin configuration
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
```

## Key Files

- **models.py**: Defines the Question and UserPerformance models.
- **views.py**: Contains the logic for rendering pages and processing user actions.
- **urls.py**: Maps URLs to corresponding views.
- *Templates*: HTML files for the dashboard and quiz pages.

## Future Improvements

- Add user authentication to allow multiple users to track their progress.
- Implement pagination or performance history on the dashboard.
- Use AJAX to update quiz feedback dynamically without reloading the page.
- Add a REST API for integration with external systems.

## Contributing

Feel free to fork the repository, make changes, and submit a pull request. All contributions are welcome!

"# Quiz-App" 
"# Quiz-App" 
"# Quiz-App" 
