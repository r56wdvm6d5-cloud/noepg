const repo = 'r56wdvm6d5-cloud/epguk';
const file = 'tvshow_epg.xml';

// Function to purge jsdelivr cache
async function refreshJsdelivrCache() {
  try {
    // Method 1: Jsdelivr purge endpoint
    const purgeResponse = await fetch(`https://purge.jsdelivr.net/gh/${repo}@main/${file}`);
    console.log('Purge response:', purgeResponse.status);
    
    // Method 2: Force refresh by requesting with timestamp
    const refreshResponse = await fetch(`https://cdn.jsdelivr.net/gh/${repo}@main/${file}?refresh=${Date.now()}`);
    console.log('Refresh response:', refreshResponse.status);
    
  } catch (error) {
    console.error('Cache refresh failed:', error);
  }
}

// Run every 5 minutes
setInterval(refreshJsdelivrCache, 300000); // 5 minutes = 300000ms

// Run immediately on start
refreshJsdelivrCache();
