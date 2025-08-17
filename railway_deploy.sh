#!/bin/bash

# Railway Quick Deployment Script for Data Analyst Agent
echo "🚂 Railway Deployment Script"
echo "============================"

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "❌ Not a git repository. Initializing..."
    git init
fi

# Check if files exist
required_files=("app.py" "requirements.txt" "Dockerfile" "LICENSE")
missing_files=()

for file in "${required_files[@]}"; do
    if [ ! -f "$file" ]; then
        missing_files+=("$file")
    fi
done

if [ ${#missing_files[@]} -gt 0 ]; then
    echo "❌ Missing required files:"
    for file in "${missing_files[@]}"; do
        echo "   - $file"
    done
    echo ""
    echo "Please ensure all project files are in this directory."
    exit 1
fi

echo "✅ All required files found"

# Create .gitignore if it doesn't exist
if [ ! -f ".gitignore" ]; then
    echo "📝 Creating .gitignore..."
    cat > .gitignore << EOF
__pycache__/
*.pyc
*.pyo
*.pyd
.env
venv/
.venv/
*.log
.DS_Store
node_modules/
EOF
fi

# Get GitHub username and repo name
read -p "Enter your GitHub username: " GITHUB_USERNAME
read -p "Enter repository name (default: data-analyst-agent): " REPO_NAME
REPO_NAME=${REPO_NAME:-data-analyst-agent}

# Commit all files
echo ""
echo "📤 Committing files to git..."
git add .
git commit -m "Deploy to Railway: Data Analyst Agent" || echo "No changes to commit"

# Check if remote exists
if ! git remote get-url origin >/dev/null 2>&1; then
    echo "🔗 Adding GitHub remote..."
    git remote add origin "https://github.com/$GITHUB_USERNAME/$REPO_NAME.git"
fi

# Push to GitHub
echo "📤 Pushing to GitHub..."
git branch -M main
git push -u origin main || echo "⚠️ Push failed. Make sure your GitHub repo exists and you have access."

echo ""
echo "🚂 Railway Deployment Options:"
echo "=============================="

echo ""
echo "Option 1: Railway Dashboard (Recommended)"
echo "----------------------------------------"
echo "1. Go to https://railway.app"
echo "2. Click 'Start a New Project'"
echo "3. Sign in with GitHub"
echo "4. Select 'Deploy from GitHub repo'"
echo "5. Choose: $GITHUB_USERNAME/$REPO_NAME"
echo "6. Click 'Deploy Now'"
echo ""

echo "Option 2: Railway CLI"
echo "-------------------"
echo "If you have Railway CLI installed:"
echo "   railway login"
echo "   railway init"
echo "   railway up"
echo ""

echo "Option 3: Install Railway CLI"
echo "---------------------------"
if command -v npm >/dev/null 2>&1; then
    echo "Installing Railway CLI..."
    npm install -g @railway/cli
    echo ""
    echo "Now run:"
    echo "   railway login"
    echo "   railway init"
    echo "   railway up"
else
    echo "Install Node.js first, then run:"
    echo "   npm install -g @railway/cli"
    echo "Or download from: https://railway.app/cli"
fi

echo ""
echo "🔗 Your GitHub Repository:"
echo "https://github.com/$GITHUB_USERNAME/$REPO_NAME"

echo ""
echo "📊 After deployment, your API will be at:"
echo "https://your-app-name.railway.app/api/"

echo ""
echo "🧪 Test your deployment:"
echo "curl https://your-app-name.railway.app/health"
echo ""

echo "✅ Ready for Railway deployment!"
echo ""
echo "📋 Next steps:"
echo "1. Go to railway.app and deploy from GitHub"
echo "2. Wait for build to complete"
echo "3. Test your API endpoint"
echo "4. Submit your Railway URL"

# Make script executable
chmod +x railway_deploy.sh

echo ""
echo "💡 Tip: Keep your Railway service running until evaluation is complete!"
