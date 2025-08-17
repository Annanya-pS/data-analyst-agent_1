#!/bin/bash

echo "🚀 Deploying Data Analyst Agent to Railway..."

# Check if railway CLI is installed
if ! command -v railway &> /dev/null; then
    echo "❌ Railway CLI not found. Please install it first:"
    echo "npm install -g @railway/cli"
    exit 1
fi

# Login to Railway (if not already logged in)
echo "🔐 Checking Railway authentication..."
railway login

# Check if railway.toml exists, if not -> init new project
if [ ! -f "railway.toml" ]; then
    echo "📝 No Railway project linked. Creating a new one..."
    railway init --name "data-analyst-agent"
else
    echo "🔗 Railway project already linked."
fi

# Set environment variables
echo "⚙️ Setting environment variables..."
railway variables -s PORT=5000 -s PYTHONUNBUFFERED=1

# Deploy
echo "🚢 Deploying to Railway..."
railway up

echo "✅ Deployment complete!"
echo "🌐 Check your Railway dashboard for the deployment URL"
