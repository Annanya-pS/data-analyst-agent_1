# Troubleshooting Guide

## Common Issues and Solutions

### 1. "Not Found" Error (404)

**Problem**: Getting 404 when accessing the API endpoint

**Solutions**:
- ✅ Check your URL format: `https://your-app.herokuapp.com/api/` (note the trailing slash)
- ✅ Try both `/api/` and `/api` endpoints
- ✅ Test the root endpoint first: `https://your-app.herokuapp.com/`
- ✅ Check if your app is actually deployed and running

**Test commands**:
```bash
# Test root endpoint
curl https://your-app.herokuapp.com/

# Test health endpoint
curl https://your-app.herokuapp.com/health

# Test API endpoint
curl -X POST https://your-app.herokuapp.com/api/ \
  -F "questions.txt=@questions.txt"
```

### 2. Local Development Issues

**Problem**: Can't run locally

**Solutions**:
```bash
# Install Python dependencies
pip install -r requirements.txt

# Run the app
python app.py

# Test it's working
python test_local.py
```

**Common local errors**:
- `ModuleNotFoundError`: Run `pip install -r requirements.txt`
- `Port already in use`: Change port or kill existing process
- `Permission denied`: Check file permissions

### 3. Heroku Deployment Issues

**Problem**: App crashes or won't start on Heroku

**Check logs**:
```bash
heroku logs --tail -a your-app-name
```

**Common fixes**:
```bash
# Restart the app
heroku restart -a your-app-name

# Check dyno status
heroku ps -a your-app-name

# Scale up if needed
heroku ps:scale web=1 -a your-app-name

# Check environment variables
heroku config -a your-app-name
```

**Requirements issues**:
- Ensure `requirements.txt` has all dependencies
- Check Python version in `runtime.txt`
- Verify `Procfile` syntax

### 4. Timeout Errors

**Problem**: Requests timing out

**Solutions**:
- Increase timeout in `Procfile`: `web: gunicorn app:app --timeout 300`
- Optimize data processing code
- Add progress indicators for long operations
- Break large tasks into smaller chunks

### 5. Memory Issues

**Problem**: Out of memory errors

**Solutions**:
- Process data in chunks
- Clean up temporary files
- Use memory-efficient data structures
- Add garbage collection calls

### 6. Image/Plot Issues

**Problem**: Base64 images too large or corrupted

**Solutions**:
```python
# Compress images
if len(img_data) > 100000:  # 100KB limit
    img = Image.open(buffer)
    img = img.resize((800, 600), Image.Resampling.LANCZOS)
    img.save(buffer, format='PNG', optimize=True, quality=85)
```

### 7. Web Scraping Issues

**Problem**: Can't scrape Wikipedia or other sites

**Solutions**:
- Add user agent headers
- Handle rate limiting
- Add error handling for network issues
- Use fallback data when scraping fails

```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
response = requests.get(url, headers=headers, timeout=30)
```

### 8. JSON Response Issues

**Problem**: Invalid JSON responses

**Solutions**:
- Always return valid JSON structure
- Handle exceptions properly
- Validate response format before returning
- Use `jsonify()` in Flask

```python
try:
    result = process_data()
    return jsonify(result)
except Exception as e:
    return jsonify({"error": str(e)}), 500
```

## Testing Your Deployment

### Quick Test Script
```bash
# Create test file
echo "Test question" > questions.txt

# Test your API
curl -X POST https://your-app.herokuapp.com/api/ \
  -F "questions.txt=@questions.txt" \
  --max-time 300

# Check response
echo $?  # Should be 0 for success
```

### Detailed Testing

Use the provided `test_api.py` script:
```bash
python test_api.py
# Enter your API URL when prompted
```

## Debugging Steps

1. **Start simple**: Test with basic questions first
2. **Check logs**: Always check application logs for errors
3. **Test locally**: Reproduce issues in local development
4. **Verify dependencies**: Ensure all packages are installed
5. **Check timeouts**: Increase timeout values if needed
6. **Monitor resources**: Check memory and CPU usage

## Platform-Specific Issues

### Heroku
- **Dyno sleeping**: Free tier sleeps after 30 minutes of inactivity
- **Build timeouts**: Large dependencies may timeout during build
- **Ephemeral filesystem**: Files are deleted after dyno restart

### Railway
- **Build failures**: Check build logs in dashboard
- **Memory limits**: Monitor memory usage
- **Environment variables**: Set via Railway dashboard

### Render
- **Static files**: May need to configure static file serving
- **Build commands**: Verify build and start commands
- **Port binding**: Ensure app binds to `0.0.0.0:$PORT`

## Getting Help

1. **Check logs** first - most issues are visible in logs
2. **Test locally** - reproduce the issue in development
3. **Search error messages** - Google the exact error
4. **Check documentation** for your deployment platform
5. **Use the testing scripts** provided in this repository

## Emergency Fixes

If your API is failing during evaluation:

1. **Quick restart**:
   ```bash
   heroku restart -a your-app-name
   ```

2. **Revert to working version**:
   ```bash
   git revert HEAD
   git push heroku main
   ```

3. **Scale up resources**:
   ```bash
   heroku ps:scale web=2 -a your-app-name
   ```

4. **Check and fix obvious issues**:
   - Syntax errors
   - Missing imports
   - Incorrect endpoints
   - Wrong response format
