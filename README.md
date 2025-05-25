
# 📚 Library Management System

A cross-platform desktop application for managing a library’s collection of books, authors, and user profiles.  
Built with **Python 3**, **Kivy** for the GUI, and **SQLite** via **SQLAlchemy** for data persistence.  
Follows the Repository Design Pattern for clean separation of concerns.

---

## 🧐 Code Review Summary

- **Modular & OOP-based**  
  – Classes for `Book`, `Author`, `User`, and a separate `Repository` layer keep business logic neatly encapsulated.  
- **SQLAlchemy ORM**  
  – Smooth integration with SQLite; sessions are managed appropriately in each repository.  
- **Kivy GUI**  
  – Declarative `.kv` layout files paired with well-named Python callbacks; screens are organized via a `ScreenManager`.  
- **Areas for Improvement**  
  1. **Error Handling & Validation**  
     – Validate user input (e.g. non-empty strings, numeric fields). Wrap DB commits in try/except.  
  2. **Packaging & CLI**  
     – Consider a `setup.py` or `pyproject.toml` so users can `pip install .` and run via a console entry-point.  
  3. **Tests**  
     – Add a `tests/` folder with unit tests for each repository using `pytest` and an in-memory SQLite DB.  
  4. **Logging**  
     – Integrate Python’s `logging` module to capture runtime errors and user actions.

---

## ✨ Features

- ➕ Add, edit, and delete books  
- 👤 Manage authors and user profiles  
- 🔍 Search and filter the book collection  
- 💾 Persistent storage using SQLite (no external DB server needed)  
- 🖥️ Modern, touch-friendly GUI built with Kivy  
- 🗂️ Clean data access via Repository Pattern

---

## 🛠️ Tech Stack

- **Language:** Python 3.7+  
- **GUI:** Kivy  
- **Database:** SQLite (via SQLAlchemy ORM)  
- **Architecture:** OOP + Repository Pattern  

---

## 📂 Project Structure

```plaintext
Library_Managment/
├── src/
│   ├── models/                # SQLAlchemy ORM models
│   │   ├── book.py
│   │   ├── author.py
│   │   └── user.py
│   ├── repositories/          # Repository classes wrapping session & CRUD
│   │   ├── book_repo.py
│   │   ├── author_repo.py
│   │   └── user_repo.py
│   ├── gui/                   # Kivy app code & KV layout files
│   │   ├── main.py            # App entry point and ScreenManager setup
│   │   ├── library.kv         # Kivy language file defining screens & widgets
│   │   ├── book_screen.py
│   │   ├── author_screen.py
│   │   └── user_screen.py
│   ├── database.py            # Engine & session factory (with init_db())
│   └── main.py                # Top-level launcher (imports and runs gui/main.py)
├── requirements.txt           # SQLAlchemy, Kivy, etc.
├── library.db                 # (auto-created) SQLite data file
├── LICENSE
└── README.md
````

---

## 💾 Installation

1. **Clone this repository**

   ```bash
   git clone https://github.com/PariCoderDeveloper/Library_Managment.git
   cd Library_Managment
   ```

2. **Create & activate a virtual environment** (recommended)

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   > *requirements.txt* should include at least:
   >
   > ```
   > kivy
   > SQLAlchemy
   > ```

---

## ▶️ Usage

1. **Initialize the database** (first run only)

   ```bash
   python -c "from database import init_db; init_db()"
   ```
2. **Launch the application**

   ```bash
   python src/gui/main.py
   ```

The Kivy window will open, letting you switch between **Books**, **Authors**, and **Users** screens. All changes persist to `library.db` in the project root.

---

## 🛠️ Development

* **Run tests** (once you add them)

  ```bash
  pytest
  ```
* **Lint & format**

  ```bash
  black src
  flake8 src
  ```

---

## 🚀 Future Improvements

* ✅ Add user authentication & roles (e.g. Admin vs. Member)
* ✅ Export/import book data as CSV
* 🌈 Theme support (using Kivy’s styles or third-party themes)
* 🧪 Comprehensive unit & integration tests
* 📦 Build distributable packages (e.g. via PyInstaller or Buildozer)

---

## 🤝 Contributing

1. **Fork** this repo
2. **Create** your feature branch:

   ```bash
   git checkout -b feature/my-feature
   ```
3. **Commit** your changes:

   ```bash
   git commit -m "Add my feature"
   ```
4. **Push** to your branch:

   ```bash
   git push origin feature/my-feature
   ```
5. **Open** a Pull Request here on GitHub.

---

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## 📬 Contact

**Pari Coder**

* GitHub: [@PariCoderDeveloper](https://github.com/PariCoderDeveloper)
* Email: [your-email@example.com](mailto:parisaalizadeh13821382@gmail.com)

Feel free to open an issue if you run into any problems or have suggestions!


