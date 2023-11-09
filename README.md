


# Substack: A Blogging Website

## Description
Django offers a user-friendly platform for seamless blog posting and categorization. With an intuitive search feature, finding relevant content is a breeze. Users have the flexibility to create, edit, and manage their profiles, ensuring a personalized experience. Behind the scenes, we've harnessed the power of Django to execute CRUD operations, providing a robust foundation for our web application.

## Installation
### Prerequisites
- Python (3.6 or higher)
- MySQL database server
- Pip


### Installation Steps

#### 1.Clone the repository:
   ```sh
   git clone https://github.com/vishakhamangtani/blog-website/
   ```
#### 2.Configure MySQL Database

- Create a MySQL database for your project.
- Update the database settings in `yourproject/settings.py` with your MySQL database credentials.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yourdb',
        'USER': 'youruser',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

#### 3. Migrate the Database

Run the following commands to apply migrations and create the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 4. Run the Development Server

Start the Django development server.

```bash
python manage.py runserver
```

The application will be accessible at `http://127.0.0.1:8000/`.


### Usage

#### Blogger User

**1. Blog Creation**
- Bloggers can log in using their credentials (username and password).
- After logging in, they can create and publish blog posts.
- Add categories and tags to your posts for easy navigation.


**2. Search Functionality**
- Use the built-in search feature to find specific content or topics.
- Discover blog posts that interest you quickly and easily.


**3. Profile Management**
- Update your blogger profile with your information and preferences.
- Personalize your blogging experience for your readers.


### Features

- **Dynamic Blogging Platform:** Our website provides a dynamic and user-friendly platform for bloggers to create and manage content effectively.

- **User Authentication:** We offer secure login and signup functionalities, ensuring the privacy and security of blogger accounts.

- **Robust Blogging System:** Bloggers can create, edit, and categorize their blog posts for a personalized and organized experience.

- **Categorization and Tagging:** Content can be categorized and tagged, making it easy for readers to discover and navigate through various topics.

- **Search Function:** Our website features a powerful search function, allowing users to find specific content and topics with ease.
