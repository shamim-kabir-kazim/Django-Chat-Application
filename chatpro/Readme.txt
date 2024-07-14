Django Firebase Chat Application 💬

This is a simple chat application built using Django for the backend and Firebase for real-time messaging.

Setup Instructions 🚀

1. Clone the repository:
   git clone <repository_url>
   cd chatpro

2. Install dependencies:
   pip install -r requirements.txt

3. Firebase Setup:
   - Create a Firebase project at Firebase Console.
   - Generate a new private key in Project settings > Service accounts.
   - Save the JSON key file securely.
   - Replace 'your_firebase_admin_sdk.json' in 'chatpro/settings.py' with your Firebase Admin SDK JSON file path.

4. Database Setup:
   - The application uses SQLite by default ('chatpro/settings.py'). Modify DATABASES setting if using another database.

5. Run Migrations:
   python manage.py migrate

6. Start the Django Development Server:
   python manage.py runserver

7. Access the Application:
   - Open your web browser and go to http://localhost:8000/ to access the chat application.

Project Structure 📁

- 'chat/': Django app directory containing views, models, and templates.
- 'chatpro/': Django project settings and configuration.

Contributing 🤝

Contributions are welcome! Please fork the repository and submit pull requests with improvements or new features.

License 📄

This project is licensed under the MIT License - see the LICENSE file for details.
