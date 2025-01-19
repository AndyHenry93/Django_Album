# Photo Management Django Application

This Django application allows users to create accounts, manage their uploaded photos, organize them into albums, and share them with friends.

## Key Features

### User Accounts & Authentication
- Secure sign-up and log-in functionality.
- Profile management for personalized user experience.

### Album Management
- Organize and categorize photos into custom albums.
- Easy access and seamless browsing through user-created albums.

### Sharing & Social Features
- Share albums or individual photos with friends for collaboration and enjoyment.

## Performance and Scalability
To ensure optimal performance and scalability, this application leverages:

### WhiteNoise
- Efficient handling of static files for fast and reliable delivery.

### AWS S3 Buckets
- Secure and scalable media storage.
- Allows users to upload, store, and manage photos seamlessly in the cloud.

## Technical Stack
- **Backend**: Django
- **Storage**: AWS S3 Buckets
- **Static Files**: WhiteNoise

## Getting Started

### Prerequisites
- Python 3.9
- Django 4.0
- AWS account with access to S3
- SQLite

### Installation

1. Clone the repository:
   ```bash
   https://github.com/AndyHenry93/Django_Album.git
   cd Django_Album
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure your environment variables:
   - Create a `.env` file in the project root.
   - Add the necessary keys for AWS S3, database settings, and Django secret key.

5. Run database migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

Special thanks to the Django and AWS communities for their excellent documentation and support.


