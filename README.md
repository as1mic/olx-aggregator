# OLX Auto Ads Aggregator

This project is a simple scraper that automatically collects ads from [OLX Poland](https://www.olx.pl), extracts relevant information, and saves it to a MySQL database using Docker.

## Features

- Fetches all categories from OLX
- Parses ad title, price, and link
- Saves data to a MySQL database
- Uses Docker and docker-compose
- Initializes the database automatically via `init.sql`

## Tech Stack

- Python 3.11+
- BeautifulSoup
- MySQL 8.0
- Docker & docker-compose
- Requests

## Project Structure

```
.
├── scraper.py            # main scraper logic
├── db.py                 # database logic
├── init.sql              # database table initialization
├── requirements.txt      # Python dependencies
├── docker-compose.yml    # Docker configuration
└── README.md
```

## Quickstart

1. Clone the repository

```bash
git clone https://github.com/your-username/olx-aggregator.git
cd olx-aggregator
```

2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # on Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Start MySQL with Docker

```bash
docker compose up -d
```

5. Run the scraper

```bash
python scraper.py
```

## Database Schema

```sql
CREATE TABLE ads (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title TEXT,
  price TEXT,
  link TEXT
);
```

## Future Improvements

- Keyword filtering
- Web interface (FastAPI)
- HTML rendering
- Scheduling via cron

## Author

Asim Aliiev