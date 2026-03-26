#!/bin/bash

# Setup Netlify Drop for free EPG hosting
# This works with private GitHub repos

REPO_DIR="/Users/ah/CascadeProjects/windsurf-project"
EPG_FILE="epg.xml"

cd "$REPO_DIR"

echo "Setting up Netlify hosting for EPG XML..."
echo ""
echo "Instructions:"
echo "1. Go to: https://app.netlify.com/drop"
echo "2. Drag and drop your EPG file: $EPG_FILE"
echo "3. Copy the URL provided by Netlify"
echo "4. Use that URL in IPTVNator"
echo ""
echo "Your EPG file location: $REPO_DIR/$EPG_FILE"
echo ""

# Create a script to auto-upload to Netlify
cat > upload_to_netlify.sh << 'EOF'
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
EOF

chmod +x upload_to_netlify.sh

echo "Created upload_to_netlify.sh for future automation"
echo ""
echo "Quick start - Drag this file to Netlify Drop:"
echo "📁 $REPO_DIR/$EPG_FILE"
