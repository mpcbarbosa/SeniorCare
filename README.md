# SeniorCare Backend API

A FastAPI backend for the SeniorCare mobile app, designed to be deployed on Render.

## Features

- User management with roles (senior, caregiver)
- PostgreSQL database integration
- RESTful API endpoints
- Ready for deployment on Render

## Local Development

1. Clone or set up the project.

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Update the values, especially `DATABASE_URL` for your local PostgreSQL database.

5. Run the application:
   ```
   python run.py
   ```

   The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /` - Welcome message
- `POST /api/users/` - Create a new user
- `GET /api/users/{user_id}` - Get user by ID
- `GET /api/users/` - List all users

## Deployment to Render

1. Push this code to a Git repository (e.g., GitHub).

2. In your Render dashboard, create a new Web Service from your repository.

3. Render will use the `render.yaml` file for configuration.

4. Set the `DATABASE_URL` environment variable in Render to point to your PostgreSQL database (you can use Render's managed PostgreSQL or an external one).

5. Deploy the service.

## Database

The app uses SQLAlchemy with PostgreSQL. Tables are created automatically on startup.

For production, ensure your database is properly configured and secured.

## Notes

- Password hashing is not implemented; add proper security for production.
- Add authentication middleware as needed.
- Expand models and routes based on app requirements.