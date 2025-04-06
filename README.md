# Library Management System

This is a Library Management System developed using Python, SQLAlchemy, Alembic for database migrations, and interfaces for service and repository layers.

## Features

- User Authentication
- User Profile Management
- Book Management
- Author Management
- Search & Filter Books by Genre, Year, and Author
- Track User's Borrowed Books

## Tech Stack

- **Python**: Main programming language
- **Flask**: Web framework (if applicable)
- **SQLAlchemy**: ORM for database operations
- **Alembic**: For database migrations
- **SQLite**: Database for development (or any other DB you use)

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/LibraryManagement.git
   cd LibraryManagement
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup**:
   Run Alembic migrations to set up the database schema:
   ```bash
   alembic upgrade head
   ```

4. **Run the Application**:
   To run the app (if applicable), use:
   ```bash
   python app.py
   ```

## Contributing

1. Fork the repository.
2. Create your branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
