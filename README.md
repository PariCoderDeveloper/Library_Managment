# Library Management System

## Description

The **Library Management System (LMS)** is a desktop application built using **Tkinter** for **Windows**. It allows users to manage and track books, authors, and user profiles through a user-friendly graphical interface. The application provides the necessary functionality to add, update, and delete books, authors, and user data, ensuring easy management of library information. The system uses **SQLAlchemy** for database interactions and follows the **Repository Design Pattern** to ensure clean and maintainable data access logic.

The system supports basic CRUD operations (Create, Read, Update, Delete) for managing books, authors, user profiles, and the relationships between them. With **SQLite** as the backend database, it is efficient for local storage and retrieval of library data.

## Features

- **Books Management**: Add, update, and delete books with fields like title, genre, and year.
- **Authors Management**: Add, update, and delete authors and link them to books.
- **User Profiles**: Create and manage user profiles with personal information, including a biography.
- **Book-Author Relationship**: Easily link books and authors together.
- **Book-User Relationship**: Associate books with users in the system.
- **Database Integration**: Uses **SQLite** for storing data, which is lightweight and fast for local applications.
- **Repository Pattern**: Ensures organized and structured access to data with the Repository Design Pattern.
- **Graphical User Interface (GUI)**: Built using **Tkinter** for a seamless desktop user experience.

## Technologies Used

- **Python 3.x**: The primary programming language.
- **Tkinter**: A standard Python library for building GUI-based applications.
- **SQLAlchemy**: An ORM (Object-Relational Mapping) tool for Python that simplifies database interaction.
- **SQLite**: A lightweight database engine for managing and storing data locally.
- **Alembic**: A database migration tool for managing schema changes.
- **Repository Design Pattern**: To keep data access logic clean and maintainable.

## Installation

### Prerequisites

Make sure you have **Python 3.x** installed. You can download Python from [here](https://www.python.org/downloads/).

### Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
```

### Create a Virtual Environment

It's a good practice to use a virtual environment for managing dependencies:

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:
    ```bash
    .\venv\Scripts\activate
    ```
- On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

### Install Dependencies

Install the necessary dependencies via `pip`:

```bash
pip install -r requirements.txt
```

### Setup the Database

To initialize the SQLite database and create the necessary tables, run the following command:

```bash
python your_application.py
```

This will set up the database with the required tables (books, authors, users, profiles).

### Running the Application

After setting up everything, you can start the application by running the following command:

```bash
python main.py
```

This will launch the Tkinter GUI, where you can interact with the Library Management System.

## Database Schema

- **Books**: Store book-related information like title, genre, and year.
- **Authors**: Store author information, and associate books with authors.
- **Users**: Store user information, including usernames.
- **Profiles**: Each user can have a profile containing additional information like a biography.
- **Book-Author**: Many-to-many relationship between books and authors.
- **Book-User**: Many-to-many relationship between books and users (borrowed books, etc.).

## Structure of the Application

The application is structured into different modules to maintain separation of concerns:

- **Domain**: Contains model definitions for books, authors, users, and profiles.
- **Migrations**: Contains Alembic migration scripts for handling database schema changes.
- **Repository**: Implements the repository pattern for clean data access.
- **GUI**: Contains all Tkinter UI components and related logic for displaying and interacting with the data.

## Example Use Case

1. **Managing Books**: 
   - You can add a new book by providing its title, genre, and publication year.
   - You can update or delete a book from the system as needed.

2. **Managing Authors**:
   - Authors can be added to the system and linked to books, creating relationships between books and authors.

3. **Managing Users**:
   - Users can be added to the system with a unique username and a profile that contains additional information such as a biography.
   - Books can be associated with users, making it easy to track who has borrowed which books.

4. **Viewing Data**:
   - The GUI allows users to easily view books, authors, and user profiles.

## Contributing

If you'd like to contribute to the project, please fork the repository and submit a pull request with your changes. Contributions are welcome for bug fixes, enhancements, and feature requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
