# Yatube API - Final Project

A RESTful API for a social media platform built with Django and Django REST Framework. This project is part of the Yandex.Practicum course.

## Project Overview

**Yatube API** is a backend API that provides functionality for managing posts, comments, groups, and user follow relationships. The API uses JWT token-based authentication and includes comprehensive test coverage.

## Tech Stack

- **Framework**: Django 3.2.16
- **API Framework**: Django REST Framework 3.12.4
- **Authentication**: Django REST Framework Simple JWT 4.7.2
- **Database**: SQLite (included in project)
- **Testing**: pytest 6.2.4, pytest-django 4.4.0
- **Additional Libraries**:
  - django-filter 2.4.0 (filtering and search)
  - Pillow 9.3.0 (image processing)
  - requests 2.26.0 (HTTP library)

## Project Structure

```
api-final-yatube-ad/
├── yatube_api/              # Main Django project
│   ├── api/                 # API app with views, serializers, and URLs
│   │   ├── views.py         # ViewSets for API endpoints
│   │   ├── serializers.py   # DRF serializers
│   │   └── urls.py          # API routing
│   ├── posts/               # Posts app with models
│   │   ├── models.py        # Post, Comment, Group, Follow models
│   │   └── migrations/      # Database migrations
│   ├── static/              # Static files (ReDoc API documentation)
│   ├── settings.py          # Django settings
│   └── manage.py            # Django management script
├── tests/                   # Test suite
│   ├── test_post.py         # Post endpoint tests
│   ├── test_comment.py      # Comment endpoint tests
│   ├── test_follow.py       # Follow endpoint tests
│   ├── test_group.py        # Group endpoint tests
│   ├── test_jwt.py          # JWT authentication tests
│   └── conftest.py          # pytest configuration
├── postman_collection/      # Postman API collection
│   ├── API_for_yatube.postman_collection.json
│   └── set_up_data.sh       # Database setup script
├── requirements.txt         # Python dependencies
├── pytest.ini              # pytest configuration
└── README.md               # Original project README

```

## Data Models

### Post
- `text`: Main content of the post
- `pub_date`: Publication date (auto-generated)
- `author`: Foreign key to User
- `image`: Optional image attachment
- `group`: Optional foreign key to Group

### Comment
- `text`: Comment content
- `author`: Foreign key to User
- `post`: Foreign key to Post
- `created`: Creation timestamp

### Group
- `title`: Group name
- `slug`: Unique URL-friendly identifier
- `description`: Group description

### Follow
- `user`: User who is following (Foreign key to User)
- `following`: User being followed (Foreign key to User)
- Constraint: Each (user, following) pair must be unique

## API Endpoints

### Posts
- `GET /api/v1/posts/` - List all posts (paginated with limit/offset)
- `POST /api/v1/posts/` - Create a new post (authenticated)
- `GET /api/v1/posts/{id}/` - Retrieve post details
- `PUT /api/v1/posts/{id}/` - Update post (author only)
- `PATCH /api/v1/posts/{id}/` - Partial update post (author only)
- `DELETE /api/v1/posts/{id}/` - Delete post (author only)

### Comments
- `GET /api/v1/posts/{post_id}/comments/` - List comments for a post
- `POST /api/v1/posts/{post_id}/comments/` - Add comment to post (authenticated)
- `GET /api/v1/posts/{post_id}/comments/{id}/` - Retrieve comment details
- `PUT /api/v1/posts/{post_id}/comments/{id}/` - Update comment (author only)
- `PATCH /api/v1/posts/{post_id}/comments/{id}/` - Partial update comment (author only)
- `DELETE /api/v1/posts/{post_id}/comments/{id}/` - Delete comment (author only)

### Groups
- `GET /api/v1/groups/` - List all groups (read-only)
- `GET /api/v1/groups/{id}/` - Retrieve group details (read-only)

### Follow
- `GET /api/v1/follow/` - List user's followed accounts (authenticated)
- `POST /api/v1/follow/` - Follow a user (authenticated)
- `GET /api/v1/follow/?search=username` - Search followed accounts by username

### JWT Authentication
- `POST /api/v1/jwt/create/` - Obtain JWT token pair (username & password)
- `POST /api/v1/jwt/refresh/` - Refresh access token using refresh token
- `POST /api/v1/jwt/verify/` - Verify JWT token validity

## Permissions & Authentication

- **Posts**: Authenticated users can create; only authors can edit/delete; everyone can read
- **Comments**: Authenticated users can create; only authors can edit/delete; everyone can read
- **Groups**: Everyone can read (read-only)
- **Follow**: Only authenticated users can access; users see only their own follows
- **JWT**: Token-based authentication required for protected endpoints

## Setup Instructions

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run migrations**:
   ```bash
   cd yatube_api
   python manage.py migrate
   ```

3. **Create superuser** (optional):
   ```bash
   python manage.py createsuperuser
   ```

4. **Run development server**:
   ```bash
   python manage.py runserver
   ```

5. **For Postman testing**, use the setup script:
   ```bash
   cd postman_collection
   bash set_up_data.sh
   ```

## Testing

Run the test suite with pytest:

```bash
pytest
```

Or with verbose output:
```bash
pytest -vv
```

**Test Coverage**:
- `test_post.py` - Post CRUD operations and permissions (18.65 KB)
- `test_comment.py` - Comment CRUD operations and relationships (18.65 KB)
- `test_follow.py` - Follow/unfollow functionality (9.46 KB)
- `test_group.py` - Group listing and filtering (5.77 KB)
- `test_jwt.py` - JWT token generation and validation (6.84 KB)

Tests use pytest fixtures defined in `conftest.py` for setup and teardown.

## Custom Permissions

### IsAuthorOrReadOnly
- Allows read access to all users
- Write access only to the author of the content
- Used for Post and Comment endpoints

## Key Features

✅ Full CRUD operations for posts and comments  
✅ Group management and filtering  
✅ User follow/unfollow system with search  
✅ JWT token-based authentication  
✅ Pagination support for posts (limit/offset)  
✅ Search functionality for follows (by username)  
✅ Permission checks for content ownership  
✅ Comprehensive test coverage with pytest  
✅ Postman collection for API testing  

## API Documentation

OpenAPI/ReDoc documentation available at:
- `static/redoc.yaml` - OpenAPI specification (33.13 KB)

## Database

- SQLite database included (`db.sqlite3`)
- All migrations located in `yatube_api/posts/migrations/`
- Database can be reset using the Postman setup script

## Notes

- The project is configured to run with pytest's Django integration (`pytest-django`)
- All test modules are located in the `tests/` directory
- The API uses Standard Django User model for authentication
