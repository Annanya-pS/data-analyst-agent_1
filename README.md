# Data Analyst Agent

A Flask-based API service that uses AI and data analysis tools to source, prepare, analyze, and visualize data automatically.

## Features

- **Web Scraping**: Automatically scrapes data from Wikipedia and other sources
- **Database Queries**: Executes DuckDB queries for large-scale data analysis
- **Data Visualization**: Creates plots and charts encoded as base64 data URIs
- **Multi-format Support**: Handles CSV, JSON, and other data formats
- **Statistical Analysis**: Performs correlation analysis, regression, and other statistical computations

## API Endpoint

The service exposes a single POST endpoint at `/api/` that accepts:
- `questions.txt` (required): Contains the analysis questions/tasks
- Additional data files (optional): CSV, JSON, or other data files

### Example Usage

```bash
curl -X POST "https://your-app-url.com/api/" \
  -F "questions.txt=@questions.txt" \
  -F "data.csv=@data.csv" \
  -F "image.png=@image.png"
```

## Supported Analysis Types

### 1. Wikipedia Film Analysis
Scrapes highest-grossing films data and answers questions about:
- Films grossing over specific amounts before certain years
- Earliest films reaching milestones
- Correlation analysis between rankings
- Scatter plots with regression lines

### 2. Court Data Analysis
Analyzes Indian High Court judgment data using DuckDB:
- Case disposal statistics by court and time period
- Time delay analysis between registration and decision
- Regression analysis and visualization

### 3. Generic Data Analysis
Handles CSV and JSON files for custom analysis tasks.

## Response Formats

### Array Format (Film Analysis)
```json
[1, "Titanic", 0.485782, "data:image/png;base64,iVBORw0KG..."]
```

### Object Format (Court Analysis)
```json
{
  "Which high court disposed the most cases from 2019 - 2022?": "33_10",
  "What's the regression slope...": 0.123456,
  "Plot the year and # of days...": "data:image/png;base64,..."
}
```

## Installation & Deployment

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/your-username/data-analyst-agent.git
cd data-analyst-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

The API will be available at `http://localhost:5000/api/`

### Docker Deployment

1. Build the Docker image:
```bash
docker build -t data-analyst-agent .
```

2. Run the container:
```bash
docker run -p 5000:5000 data-analyst-agent
```

### Cloud Deployment Options

#### Heroku
```bash
heroku create your-app-name
heroku container:push web
heroku container:release web
```

#### Railway
```bash
railway login
railway init
railway up
```

#### Google Cloud Run
```bash
gcloud builds submit --tag gcr.io/PROJECT-ID/data-analyst-agent
gcloud run deploy --image gcr.io/PROJECT-ID/data-analyst-agent --platform managed
```

## Dependencies

- **Flask**: Web framework
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **matplotlib/seaborn**: Data visualization
- **requests**: HTTP library for web scraping
- **BeautifulSoup**: HTML parsing
- **DuckDB**: Analytical database for large datasets
- **scipy**: Scientific computing and statistics

## File Structure

```
data-analyst-agent/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
├── README.md          # This file
├── LICENSE            # MIT license
└── tests/             # Test files (optional)
```

## Health Check

The service includes a health check endpoint:
```bash
GET /health
```

Returns: `{"status": "healthy"}`

## Error Handling

The API includes comprehensive error handling and will return appropriate error responses while maintaining the expected response structure for partial credit.

## Performance Considerations

- 5-minute timeout per request
- Images optimized to stay under 100KB
- Efficient memory usage with pandas and DuckDB
- Docker containerization for consistent deployment

## License

MIT License - see LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Support

For issues and questions, please open a GitHub issue or contact the maintainer.