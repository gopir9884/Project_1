# Contact Manager - Full Stack App

This is a full-stack contact management application with a Python Flask backend and HTML/JavaScript frontend.

## Project Structure

```
Project_1/
├── backend/
│   ├── app.py              # Flask API
│   ├── requirements.txt     # Python dependencies
│   └── contacts.csv        # Contact data (auto-generated)
├── frontend/
│   └── index.html          # Web UI
└── venv/                   # Python virtual environment
```

## Setup & Run

### 1. Backend Setup

Open PowerShell and navigate to the project:
```powershell
cd C:\Users\GOPI\Desktop\Python\Project_1
```

Activate the virtual environment:
```powershell
.\venv\Scripts\Activate.ps1
```

Install backend dependencies:
```powershell
cd backend
pip install -r requirements.txt
```

Start the Flask server:
```powershell
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

### 2. Frontend Setup

**In a new PowerShell window**, open the frontend folder and start a local server:

```powershell
cd C:\Users\GOPI\Desktop\Python\Project_1\frontend
```

Start a simple HTTP server (Python 3.7+):
```powershell
python -m http.server 8000
```

Or use any other local server (VS Code Live Server, npm http-server, etc.)

Open your browser and go to:
```
http://localhost:8000
```

## How It Works

### Backend API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/contacts` | Add a new contact |
| GET | `/api/contacts` | Get all contacts |
| GET | `/api/contacts/search?q=term` | Search contacts |
| PUT | `/api/contacts/<name>` | Update a contact |
| DELETE | `/api/contacts/<name>` | Delete a contact |

### Frontend-Backend Connection

The frontend (`index.html`) makes API calls to the backend using the Fetch API:

```javascript
const API_URL = "http://localhost:5000/api";

// Example: Adding a contact
fetch(`${API_URL}/contacts`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, phone, email })
})
```

The backend uses **CORS** (Cross-Origin Resource Sharing) to allow the frontend (port 8000) to communicate with the backend (port 5000).

## Features

✅ Add contacts  
✅ View all contacts  
✅ Search contacts by name  
✅ Delete contacts  
✅ Responsive UI  
✅ Error handling  
✅ Real-time updates  

## Troubleshooting

### "Can't connect to backend"
- Make sure Flask server is running on `http://localhost:5000`
- Check that CORS is enabled in `app.py`

### "Port already in use"
- Change port in `app.py`: `app.run(port=5001)`
- Change port in `index.html`: `const API_URL = "http://localhost:5001/api"`

### "ModuleNotFoundError: No module named 'flask'"
- Ensure venv is activated
- Run `pip install -r requirements.txt`

## Next Steps

- Add user authentication (login/register)
- Deploy to cloud (Heroku, AWS, Azure)
- Add a database (SQLite, PostgreSQL)
- Create React/Vue frontend for better UX
- Add edit functionality
