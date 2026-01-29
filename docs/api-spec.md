# CampusLite API Specification

**Base URL**  
`http://localhost:5000`

**Content-Type**  
All JSON responses: `application/json`  
POST requests with data: `application/json` (except file uploads)

**Authentication**  
None implemented yet (public endpoints).  
Future: Add JWT or session-based auth for creator endpoints.

## Endpoints Overview

| Method | Endpoint                  | Description                          | Auth required? | Main consumer | Main creator |
|--------|---------------------------|--------------------------------------|----------------|---------------|--------------|
| GET    | `/episodes`               | List episodes (paginated)            | No             | ✓             |              |
| GET    | `/episode/{id}`           | Get single episode details           | No             | ✓             |              |
| GET    | `/stream/{id}`            | Stream audio file (HTML5 audio)      | No             | ✓             |              |
| POST   | `/upload-audio`           | Upload audio file → get file_path    | Yes (future)   |               | ✓            |
| POST   | `/episode`                | Create new episode (metadata)        | Yes (future)   |               | ✓            |
| PUT    | `/episode/{id}`           | Update episode metadata              | Yes (future)   |               | ✓            |
| DELETE | `/episode/{id}`           | Delete episode                       | Yes (future)   |               | ✓            |

## Detailed Endpoint Specification

### 1. List Episodes  

**GET** `/episodes`  

**Query parameters** (all optional)  
- `page`     int    default: 1  
- `limit`    int    default: 10, max ~50  

**Response** 200 OK  
```json
{
  "episodes": [
    {
      "id": 1,
      "title": "Pink Floyd - Time",
      "description": "Classic track discussion",
      "file_path": "abc123-4567.mp3"
    },
    ...
  ],
  "total": 42,
  "pages": 5,
  "current_page": 1
}
```

### 2. Get Single Episode

GET `/episode/{id}`
Response 200 OK
JSON{
  "id": 1,
  "title": "Pink Floyd - Time",
  "description": "Classic track discussion",
  "file_path": "abc123-4567.mp3"
}
404 if not found

### 3. Stream Audio

GET `/stream/{id}`
Usage
Use directly in <audio> tag:
HTML<audio controls src="http://localhost:5000/stream/1"></audio>
Headers

Supports Range requests → seeking works
Content-Type: audio/mpeg (or detected mime)
Accept-Ranges: bytes

Response

200 OK or 206 Partial Content
Binary audio stream (not downloadable as file)

404 if episode or file missing

### 4. Upload Audio File

POST `/upload-audio`
Content-Type
multipart/form-data
Form field

file    binary file (mp3, wav, m4a, ogg)

Example (curl)
Bashcurl -X POST http://localhost:5000/upload-audio \
  -F "file=@C:/path/to/Pink_Floyd_Time.mp3"
Response 201 Created
JSON{
  "file_path": "550e8400-e29b-41d4-a716-446655440000.mp3",
  "file_url": "/stream-file/550e8400-e29b-41d4-a716-446655440000.mp3"
}
400 if no file / wrong type

### 5. Create Episode

POST `/episode`
Content-Type : application/json
Body
```JSON
{
  "title": "Pink Floyd - Time",
  "description": "Discussion about the song structure",
  "file_path": "550e8400-e29b-41d4-a716-446655440000.mp3"
}
```
Response 201 Created

```JSON
{
  "id": 3,
  "title": "Pink Floyd - Time",
  "description": "Discussion about the song structure",
  "file_path": "550e8400-e29b-41d4-a716-446655440000.mp3"
}
```
400 if missing title/file_path or file not found on disk



curl -X POST http://localhost:5000/episode -H "Content-Type: application/json" -d "{\"title\": \"Test Episode 1\", \"description\": \"My test wav file\", \"file_path\": \"cbefcd9a-c475-41dc-81a7-d819d4058897.wav\", \"show_id\": 1}"
curl -X POST http://localhost:5000/episode -H "Content-Type: application/json" -d "{\"title\": \"Test Episode 1\", \"description\": \"My test wav file\", \"file_path\": \"cbefcd9a-c475-41dc-81a7-d819d4058897.wav\", \"show_id\": 1}"