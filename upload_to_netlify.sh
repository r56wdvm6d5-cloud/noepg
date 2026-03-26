#!/bin/bash
# Auto-upload EPG to Netlify Drop
# You'll need to install netlify-cli: npm install -g netlify-cli

cd "/Users/ah/CascadeProjects/windsurf-project"

# Upload to Netlify (requires netlify-cli)
if command -v netlify &> /dev/null; then
    netlify deploy --prod --dir=. --site=your-site-name.netlify.app
else
    echo "Please install netlify-cli: npm install -g netlify-cli"
    echo "Or manually upload to: https://app.netlify.com/drop"
fi
