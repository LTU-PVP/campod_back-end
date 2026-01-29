## Creator workflow:

POST /show → create "The Space Podcast"
POST /upload-audio → upload file
POST /episode with "show_id": 1 + title + file_path


Homepage: collections list (/collections) → **click** → see episodes of that show (/show/1 or /episodes?show_id=1)
Episode detail: includes show_name in response

GET /episodes                        → all episodes, newest first, page 1
GET /episodes?show_id=3              → only episodes from show #3
GET /episodes?show_id=3&limit=20     → 20 episodes from show #3
GET /episodes?search=pink&page=2     → episodes containing "pink" in title/desc, page 2
GET /episodes?sort=title             → all episodes sorted A–Z by title

- #### collection Id specified by frontend?


## Listener workflow:

GET /episodes       → list titles + metadata
↓
GET /episode/{id}   → details
↓
GET /stream/{id}    → HTML5 <audio> plays file from disk (range requests)