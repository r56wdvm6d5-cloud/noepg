#!/bin/bash

# Setup GitHub Gist for EPG hosting
# Public gists work even with private repos

REPO_DIR="/Users/ah/CascadeProjects/windsurf-project"
GIST_ID=""  # Set this after creating your gist

cd "$REPO_DIR"

echo "Setting up GitHub Gist for EPG hosting..."
echo ""
echo "Steps:"
echo "1. Go to: https://gist.github.com"
echo "2. Create new gist"
echo "3. Upload your epg.xml file"
echo "4. Make it public"
echo "5. Copy the raw URL"
echo ""
echo "Your raw URL will look like:"
echo "https://gist.githubusercontent.com/YOUR_USERNAME/GIST_ID/raw/epg.xml"
echo ""

# Create script to update gist
cat > update_gist.sh << 'EOF'
#!/bin/bash
# Update GitHub Gist with latest EPG data
# Requires: gh CLI (GitHub CLI)

cd "/Users/ah/CascadeProjects/windsurf-project"

if command -v gh &> /dev/null; then
    # Update gist (you need to set GIST_ID first)
    if [ -n "$GIST_ID" ]; then
        gh gist edit "$GIST_ID" --filename epg.xml epg.xml
        echo "Gist updated successfully!"
    else
        echo "Please set GIST_ID variable in this script"
        echo "Create a gist first and copy its ID"
    fi
else
    echo "Please install GitHub CLI: brew install gh"
    echo "Then authenticate: gh auth login"
fi
EOF

chmod +x update_gist.sh

echo "Created update_gist.sh for automation"
echo "After creating your gist, edit this script and set GIST_ID"
