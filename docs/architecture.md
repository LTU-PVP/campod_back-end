# Architecture - CampusLite Website Backend

## Overview
Simple Flask-based REST API backend for a podcast website.  
Focus:  
- Browse episode list  
- Stream audio server-side (no client download)  
- Allow creators to upload audio + add metadata  

Two main user roles:  
- **Listener** (public): browse + play  
- **Creator** (future auth): upload + manage episodes  

## Tech Stack
- **Language**: Python 3  
- **Framework**: Flask  
- **Database**: SQLite (via Flask-SQLAlchemy)  
- **File storage**: Local folder (`./media/`)  
- **Streaming**: Flask `send_file` with range support (HTTP 206)  
- **File upload**: Multipart form-data (`werkzeug`)  
- **Run locally**: `python app.py` → http://localhost:5000  

## Folder Structure (current)
```
campuspodcastlite/
├── app.py               # Main Flask app + all routes
├── podcasts.db          # SQLite database (auto-created)
├── media/               # Audio files (gitignored)
│   └── *.mp3 / *.m4a
├── API-spec.md          # API documentation for frontend team
└── Architecture.md      # This file
```

## Core Components

1. **Database** (SQLite)
   - Table: `Episode`
   - Fields: id (PK), title, description, file_path (just filename, e.g. "uuid.mp3")

3. **Streaming Mechanism**
- Uses `send_file(..., conditional=True, as_attachment=False)`
- Browser sends `Range: bytes=...` → Flask returns partial content (206)
- Supports seek, pause, resume natively in `<audio controls>`

4. **File Handling**
- Uploads saved to `./media/` with UUID filename
- Only filename stored in DB (not full path)
- Allowed extensions: mp3, wav, m4a, ogg