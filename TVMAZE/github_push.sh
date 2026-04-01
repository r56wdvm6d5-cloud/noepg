#!/bin/bash

# TVMAZE EPG GitHub Push Script
# Pushes generated EPG files to GitHub repository

# Configuration
REPO_URL="https://github.com/r56wdvm6d5-cloud/noepg"
REPO_DIR="noepg_repo"
EPG_FILE="epg.xml"
BRANCH="main"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== TVMAZE EPG GitHub Push Script ===${NC}"
echo

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if git is installed
if ! command -v git &> /dev/null; then
    print_error "Git is not installed. Please install git first."
    exit 1
fi

# Check if EPG file exists
if [ ! -f "$EPG_FILE" ]; then
    print_error "EPG file '$EPG_FILE' not found. Please generate it first with:"
    echo "python3 tvmaze_epg.py"
    exit 1
fi

print_status "EPG file found: $EPG_FILE"

# Create or update repository directory
if [ ! -d "$REPO_DIR" ]; then
    print_status "Cloning repository..."
    git clone "$REPO_URL" "$REPO_DIR"
    if [ $? -ne 0 ]; then
        print_error "Failed to clone repository. Please check the URL and your permissions."
        exit 1
    fi
else
    print_status "Repository directory exists, updating..."
    cd "$REPO_DIR"
    git pull origin "$BRANCH"
    cd ..
fi

# Copy EPG file to repository
print_status "Copying EPG file to repository..."
cp "$EPG_FILE" "$REPO_DIR/"

cd "$REPO_DIR"

# Check if there are changes to commit
if git diff --quiet "$EPG_FILE"; then
    print_status "No changes detected in EPG file. Force pushing anyway..."
    git add "$EPG_FILE"
    git commit -m "Force update EPG data - $TIMESTAMP [NO CHANGES]"
else
    print_status "Changes detected in EPG file."
    git add "$EPG_FILE"
    git commit -m "$COMMIT_MESSAGE"
fi

# Push to GitHub with force
print_status "Force pushing to GitHub..."
git push --force-with-lease origin "$BRANCH"

if [ $? -eq 0 ]; then
    print_status "✅ Successfully pushed EPG file to GitHub!"
    echo
    echo -e "${BLUE}Repository URL:${NC} $REPO_URL"
    echo -e "${BLUE}File pushed:${NC} $EPG_FILE"
    echo -e "${BLUE}Branch:${NC} $BRANCH"
    echo -e "${BLUE}Commit message:${NC} $COMMIT_MESSAGE"
else
    print_error "Failed to push to GitHub. Please check your credentials and permissions."
    print_error "You may need to configure git authentication:"
    echo "git config --global user.name 'Your Name'"
    echo "git config --global user.email 'your.email@example.com'"
    echo "Or use a personal access token for authentication."
fi

cd ..

echo
echo -e "${GREEN}=== Script completed ===${NC}"
