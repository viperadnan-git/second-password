<div align="center">
  <img src="https://raw.githubusercontent.com/viperadnan-git/second-password/main/src/static/favicon/android-chrome-512x512.png" alt="Second Password Logo" width="120" height="120">

  # Second Password
  
  🔐 A secure, end-to-end encrypted, cloud-synced TOTP authenticator for the web
  
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
  [![Flask](https://img.shields.io/badge/flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
</div>

## 📝 Overview

Second Password is a web-based two-factor authentication (2FA) solution that implements Time-based One-time Password (TOTP) for secure user authentication. All passwords are end-to-end encrypted and synced to the cloud, meaning your data is encrypted before it leaves your device and can only be decrypted by you. This makes your TOTP secrets accessible from any device while maintaining maximum security.

### ✨ Key Features

- 🌐 Web-based interface accessible from any device
- 🔐 End-to-end encryption of all sensitive data
- ☁️ Cloud synchronization of encrypted TOTP secrets
- 🔒 Client-side encryption of sensitive data
- 🎨 Clean and intuitive user interface
- 🔄 Automatic TOTP code updates
- 📋 One-click code copying

## 🔧 Prerequisites

- Python 3.6 or higher
- pip (Python package manager)
- PostgreSQL (optional, SQLite is used by default)

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/viperadnan-git/second-password.git
cd second-password
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up environment variables (create a `.env` file or set the variables in your system):

| Variable | Type | Default | Required | Description |
|----------|------|---------|----------|-------------|
| SECRET_KEY | string | UUID4 | No | Flask secret key used for session management |
| SITENAME | string | "Second Password" | No | Name of the site displayed in UI |
| DATABASE_URL | string | None | No | PostgreSQL database URL. If not set, SQLite will be used |
| SQLITE_PATH | string | "user.db" | No | Path to SQLite database file (only used if DATABASE_URL not set) |
| HOST | string | "0.0.0.0" | No | Host address to bind the server to |
| PORT | integer | 8000 | No | Port number to run the server on |

Example `.env` file:

## 💻 Development

To run the development server:

```bash
python -m src
```

The application will be available at `http://localhost:8000`

## 🌐 Deployment

### Using Docker

1. Build the Docker image:
```bash
docker build -t second-password .
```

2. Run the container:
```bash
docker run -p 8000:8000 -e SECRET_KEY=your_secret_key_here second-password
```

### Using CapRover

1. Make sure you have a CapRover instance set up
2. Deploy using the provided `captain-definition` file
3. Configure environment variables in CapRover dashboard

## ⚙️ Configuration

### Database Configuration

The application supports both SQLite and PostgreSQL:

- **SQLite** (default): No configuration needed, will create `user.db` in root directory
- **PostgreSQL**: Set `DATABASE_URL` environment variable:
```
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

### Security Configuration

- Set a strong `SECRET_KEY` in environment variables
- Use HTTPS in production
- Keep your database credentials secure

## 🔒 Security

- TOTP secrets are encrypted using AES before storage
- Passwords are hashed using bcrypt
- Client-side encryption of sensitive data
- Session-based authentication

## 🛠️ Tech Stack

- **Backend**: Flask, Python
- **Database**: PostgreSQL/SQLite with Peewee ORM
- **Frontend**: Bootstrap 5, JavaScript
- **Authentication**: Flask-Login
- **Encryption**: CryptoJS (client-side), bcrypt (server-side)
- **TOTP**: otplib

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

Adnan - [@viperadn](https://twitter.com/viperadn) - viperadnan@gmail.com

Project Link: [https://github.com/viperadnan-git/second-password](https://github.com/viperadnan-git/second-password)

## 🙏 Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [Peewee](http://docs.peewee-orm.com/)
- [otplib](https://github.com/yeojz/otplib)
- [CryptoJS](https://github.com/brix/crypto-js)
