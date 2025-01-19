# Ger-T: Quiz Website

## Overview

Ger-T is an interactive quiz website designed to provide a dynamic and engaging platform for users to test their knowledge of the German language through various quizzes. Powered by a dataset sourced from Kaggle, the application ensures a diverse range of questions for users to explore.

The website leverages Django as the backend framework, with HTML and CSS providing a clean and responsive user interface. A touch of JavaScript enhances the interactivity, enabling features like dynamic charts and quiz options. Ger-T offers a seamless experience, allowing users to easily navigate between quizzes and view their progress on the dashboard.

---

## Project Architecture

- **Frontend**: HTML, CSS, and JavaScript for creating the user interface.
  - JavaScript is specifically used for handling dynamic elements such as charts and interactive quiz options.
- **Backend**: Django for managing logic, data processing, and serving web pages.
- **Templates**: Django templates (`templates/`) for rendering dynamic HTML pages.
- **Static Files**: CSS, JavaScript, and images stored in the `static/` directory to style and enhance the website.
- **Dataset**: Quiz data loaded from a dataset sourced from Kaggle.
- **Virtual Environment**: A Python virtual environment (`venv`) to manage dependencies and isolate the project environment.

---

## Setup Instructions

### Prerequisites

1. **Install Python**:
   Ensure you have Python installed on your system (version 3.7 or higher).
   - Check Python version:
     ```bash
     python3 --version
     ```
2. **Install Git**:
   If not already installed, set up Git for version control:
   ```bash
   sudo apt install git  # Linux
   brew install git      # macOS
   winget install git.git  # Windows
   ```

### Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/portfolio-project.git
   cd portfolio-project
   ```

2. **Set Up a Virtual Environment**:

   ```bash
   python3 -m venv venv
   ```

3. **Activate the Virtual Environment**:

   - **Linux/macOS**:
     ```bash
     source venv/bin/activate
     ```
   - **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```

4. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Project**:

   - Start the application:
     ```bash
     python manage.py runserver
     ```
   - Access the application in your browser:
     ```
     http://127.0.0.1:8000/
     ```

---

## Usage Guidelines

1. **Navigating the Website**:

   - **Register**: Create an account to participate in quizzes.
   - **Login**: Create an account to participate in quizzes.
   - **Quizzes**: Browse and participate in various quizzes sourced from the Kaggle dataset to test your knowledge.
   - **Dashboard**: View your quiz history.
   - **Logout**: Logout from your account securely.

2. **Customization**:

   - Update quiz data or modify the appearance by editing the respective files in the `templates/` or `static/` directories.

3. **Adding Dependencies**:

   - Install any new Python packages using:
     ```bash
     pip install package_name
     ```
   - Update `requirements.txt`:
     ```bash
     pip freeze > requirements.txt
     ```

---

## Project Features

- Interactive quizzes powered by a Kaggle dataset.
- Performance tracking and visualization using JavaScript-powered charts.
- Responsive design for mobile and desktop.
- Modular codebase for easy updates.
- Dependency management with virtual environments.

---

## Troubleshooting

- **Virtual Environment Issues**:
  If the virtual environment is not activating, ensure you have execution permissions.

  ```bash
  chmod +x venv/bin/activate  # Linux/macOS
  ```

- **Missing Dependencies**:
  Ensure `requirements.txt` is up-to-date and install missing packages:

  ```bash
  pip install -r requirements.txt
  ```

---

## Contributing

Feel free to fork the repository and submit pull requests for improvements or new features.

---

## License

This project is licensed under the [MIT License](LICENSE).

