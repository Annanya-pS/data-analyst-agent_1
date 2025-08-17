#!/bin/bash

# Data Analyst Agent Deployment Script
echo "🚀 Data Analyst Agent Deployment Script"
echo "========================================"

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install git first."
    exit 1
fi

# Get repository name from user
read -p "Enter your GitHub username: " GITHUB_USERNAME
read -p "Enter repository name (default: data-analyst-agent): " REPO_NAME
REPO_NAME=${REPO_NAME:-data-analyst-agent}

echo ""
echo "📁 Setting up local repository..."

# Create directory and initialize git
mkdir -p $REPO_NAME
cd $REPO_NAME

# Initialize git if not already a repo
if [ ! -d ".git" ]; then
    git init
    echo "✅ Git repository initialized"
fi

# Create files (assuming they're in current directory)
echo "📝 Creating project files..."

# Note: In actual deployment, you would copy the files from artifacts
echo "⚠️  Make sure to copy all the following files to this directory:"
echo "   - app.py"
echo "   - requirements.txt" 
echo "   - Dockerfile"
echo "   - README.md"
echo "   - LICENSE"

# Stage and commit files
echo ""
echo "📤 Committing files to git..."
git add .
git commit -m "Initial commit: Data Analyst Agent API"

# Create GitHub repository (requires GitHub CLI)
echo ""
echo "🔗 Setting up GitHub repository..."
if command -v gh &> /dev/null; then
    gh repo create $REPO_NAME --public --source=. --remote=origin --push
    echo "✅ GitHub repository created and pushed"
else
    echo "⚠️  GitHub CLI not found. Please:"
    echo "   1. Go to https://github.com/new"
    echo "   2. Create a repository named: $REPO_NAME"
    echo "   3. Run these commands:"
    echo "      git remote add origin https://github.com/$GITHUB_USERNAME/$REPO_NAME.git"
    echo "      git branch -M main"
    echo "      git push -u origin main"
fi

echo ""
echo "🌐 Deployment Options:"
echo "======================"

# Heroku deployment
echo ""
echo "1️⃣  HEROKU DEPLOYMENT"
echo "   Prerequisites: Install Heroku CLI"
echo "   Commands:"
echo "   heroku create your-app-name"
echo "   heroku container:push web"
echo "   heroku container:release web"
echo "   heroku open"

# Railway deployment  
echo ""
echo "2️⃣  RAILWAY DEPLOYMENT"
echo "   Prerequisites: Install Railway CLI"
echo "   Commands:"
echo "   railway login"
echo "   railway init"
echo "   railway up"

# Google Cloud Run
echo ""
echo "3️⃣  GOOGLE CLOUD RUN"
echo "   Prerequisites: Install gcloud CLI"
echo "   Commands:"
echo "   gcloud builds submit --tag gcr.io/PROJECT-ID/data-analyst-agent"
echo "   gcloud run deploy --image gcr.io/PROJECT-ID/data-analyst-agent --platform managed"

# Render deployment
echo ""
echo "4️⃣  RENDER DEPLOYMENT"
echo "   Steps:"
echo "   1. Go to https://render.com"
echo "   2. Create new Web Service"
echo "   3. Connect your GitHub repo: $GITHUB_USERNAME/$REPO_NAME"
echo "   4. Use these settings:"
echo "      - Environment: Docker"
echo "      - Build Command: (leave empty)"
echo "      - Start Command: (leave empty - uses Dockerfile)"

# ngrok for testing
echo ""
echo "5️⃣  NGROK (For Testing)"
echo "   Prerequisites: Install ngrok"
echo "   Commands:"
echo "   python app.py  # In one terminal"
echo "   ngrok http 5000  # In another terminal"
echo "   Use the https URL from ngrok"

echo ""
echo "🧪 Testing your deployment:"
echo "=========================="
echo "curl -X POST \"https://your-app-url.com/api/\" \\"
echo "  -F \"questions.txt=@questions.txt\""

echo ""
echo "✅ Setup complete!"
echo "📋 Next steps:"
echo "   1. Copy all project files to this directory"
echo "   2. Choose a deployment method above"
echo "   3. Test your API endpoint"
echo "   4. Submit your URL for evaluation"

echo ""
echo "🔍 Health Check:"
echo "   GET https://your-app-url.com/health"
echo "   Should return: {\"status\": \"healthy\"}"

echo ""
echo "📊 Sample Test:"
echo "   Create a questions.txt file with:"
echo "   'Scrape the list of highest grossing films from Wikipedia...'"
echo ""

# Make script executable
chmod +x deploy.sh

echo "🎉 Deployment script ready!"
echo "Run: ./deploy.sh"
