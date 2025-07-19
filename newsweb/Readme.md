# NewsWeb Project

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

A web application for managing and displaying news articles. This project demonstrates a basic Django setup with a dedicated "news" application.

---

##  Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.x**: You can download it from [python.org](https://www.python.org/downloads/).
* **pip**: Python's package installer (usually comes with Python).
* **Git**: For version control. Download from [git-scm.com](https://git-scm.com/downloads).

###  Installation

1.  **Clone the Repository**
    If you're setting this up on a new machine or haven't cloned it yet, use:

    ```bash
    git clone [https://github.com/YOUR_USERNAME/newsweb.git](https://github.com/YOUR_USERNAME/newsweb.git)
    cd newsweb
    ```
    *(Remember to replace `YOUR_USERNAME` with your GitHub username.)*

2.  **Create a Virtual Environment**
    It's highly recommended to use a virtual environment to manage project dependencies:

    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment**
    * **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependencies**
    Create a `requirements.txt` file in your `newsweb` project root and add `Django` to it. As your project grows, you'll add more packages here.

    ```bash
    # Create requirements.txt (if it doesn't exist)
    echo "Django" > requirements.txt
    ```

    Then, install them:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure the Django Project**

    * **Secret Key**: In `newsweb/settings.py`, ensure you have a `SECRET_KEY`. For development, a hardcoded one is fine, but for production, use environment variables.

        ```python
        # newsweb/settings.py
        SECRET_KEY = 'your-very-secret-and-unique-key-for-development' # **IMPORTANT: Replace with a strong, random key!**
        ```

    * **Allowed Hosts**: Add `localhost` and `127.0.0.1` to `ALLOWED_HOSTS` in `newsweb/settings.py` for local development.

        ```python
        # newsweb/settings.py
        ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
        ```

    * **Register Your App**: Make sure your `news` app is registered in `INSTALLED_APPS` within `newsweb/settings.py`.

        ```python
        # newsweb/settings.py
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'news',  # Your news app
        ]
        ```

6.  **Run Migrations**
    Apply the initial database migrations:

    ```bash
    python manage.py migrate
    ```

7.  **Create a Superuser (Optional but Recommended)**
    To access the Django admin panel:

    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to set up your admin credentials.

### ▶️ Running the Development Server

Start the Django development server:

```bash
python manage.py runserver