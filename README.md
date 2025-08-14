# Data Analyst Agent

A Flask-based API service that performs data analysis, visualization, and web scraping tasks.

## Features

- Web scraping (Wikipedia, APIs)
- Data processing and analysis
- Statistical computations
- Data visualization with charts
- Database queries (DuckDB)
- File processing (CSV, Excel, etc.)

## Quick Start

### Local Development

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd data-analyst-agent
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

The API will be available at `http://localhost:5000/api/`

### Testing the API

```bash
# Create a test question file
echo "Scrape the list of highest grossing films from Wikipedia..." > questions.txt

# Test the endpoint
curl -X POST http://localhost:5000/api/ \
  -F "questions.txt=@questions.txt"
```

## Deployment Options

### Option 1: Heroku (Recommended for beginners)

1. **Install Heroku CLI**
   - Download from https://devcenter.heroku.com/articles/heroku-cli

2. **Deploy to Heroku**
```bash
# Login to Heroku
heroku login

# Create Heroku app
heroku create your-app-name

# Deploy
git add .
git commit -m "Initial commit"
git push heroku main

# Your API will be at: https://your-app-name.herokuapp.com/api/
```

### Option 2: Railway

1. **Go to railway.app**
2. **Connect your GitHub repo**
3. **Deploy automatically**
4. **Get your URL from Railway dashboard**

### Option 3: Render

1. **Go to render.com**
2. **Connect GitHub and select your repo**
3. **Choose "Web Service"**
4. **Set:**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app --workers 4 --timeout 300`

### Option 4: Docker (Local/Cloud)

```bash
# Build Docker image
docker build -t data-analyst-agent .

# Run container
docker run -p 5000:5000 data-analyst-agent

# For cloud deployment, push to Docker Hub and deploy
```

## API Usage

### Endpoint
```
POST https://your-domain.com/api/
```

### Request Format
```bash
curl "https://your-domain.com/api/" \
  -F "questions.txt=@questions.txt" \
  -F "data.csv=@data.csv" \
  -F "image.png=@image.png"
```

### Response Format
- JSON array for multiple answers: `[answer1, answer2, ...]`
- JSON object for named answers: `{"question1": "answer1", ...}`

## Sample Questions

The agent can handle various types of analysis:

1. **Web Scraping + Analysis**
```
Scrape the list of highest grossing films from Wikipedia.
1. How many $2 bn movies were released before 2000?
2. Which is the earliest film that grossed over $1.5 bn?
```

2. **Database Analysis**
```
Query the Indian High Court dataset and find:
1. Which high court disposed the most cases from 2019-2022?
2. Calculate regression slope of delays by year.
```

3. **Data Visualization**
```
Draw a scatterplot of X vs Y with regression line.
Return as base64 encoded PNG under 100KB.
```

## Development

### Project Structure
```
data-analyst-agent/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Procfile           # Heroku deployment config
├── runtime.txt        # Python version
├── Dockerfile         # Docker config
├── LICENSE           # MIT License
└── README.md         # This file
```

### Key Components

1. **DataAnalystAgent Class**: Core analysis logic
2. **Flask Routes**: API endpoints
3. **Data Processing**: Pandas, NumPy operations
4. **Visualization**: Matplotlib, Seaborn charts
5. **Web Scraping**: BeautifulSoup, requests
6. **Database**: DuckDB for large datasets

### Adding New Features

1. **Add new analysis method to DataAnalystAgent class**
2. **Update the route handler in app.py**
3. **Add any new dependencies to requirements.txt**
4. **Test locally before deploying**

## Troubleshooting

### Common Issues

1. **Timeout Errors**: Increase timeout in Procfile/gunicorn config
2. **Memory Issues**: Reduce data processing batch sizes
3. **Import Errors**: Ensure all dependencies are in requirements.txt
4. **Image Size**: Compress images to stay under 100KB limit

### Debugging

```bash
# Local debugging
export FLASK_DEBUG=1
python app.py

# Check logs on Heroku
heroku logs --tail -a your-app-name
```

## Performance Tips

1. **Use efficient data processing** (vectorized operations)
2. **Compress images** for base64 encoding
3. **Clean up temporary files** after processing
4. **Use appropriate timeout settings**
5. **Cache frequently accessed data** if needed

## License

MIT License - see LICENSE file for details.
