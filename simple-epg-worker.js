// Simple Cloudflare Worker - Basic EPG Proxy with Limits
addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
  // Your full EPG source
  const epgUrl = 'https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/epg_combined.xml'
  
  try {
    const response = await fetch(epgUrl)
    if (!response.ok) {
      return new Response('EPG file not found', { status: 404 })
    }
    
    const xmlContent = await response.text()
    
    // Simple approach: just truncate the XML
    const truncatedXML = truncateXML(xmlContent)
    
    return new Response(truncatedXML, {
      status: 200,
      headers: {
        'Content-Type': 'application/xml; charset=utf-8',
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Pragma': 'no-cache',
        'Expires': '0',
        'Access-Control-Allow-Origin': '*'
      }
    })
  } catch (error) {
    return new Response('Error: ' + error.message, { 
      status: 500,
      headers: { 'Content-Type': 'text/plain' }
    })
  }
}

function truncateXML(xmlContent) {
  // Find all channel and programme tags
  const channelRegex = /<channel[^>]*>[\s\S]*?<\/channel>/g
  const programmeRegex = /<programme[^>]*>[\s\S]*?<\/programme>/g
  
  const channels = xmlContent.match(channelRegex) || []
  const programmes = xmlContent.match(programmeRegex) || []
  
  // Take first 10 channels and first 200 programmes
  const limitedChannels = channels.slice(0, 10)
  const limitedProgrammes = programmes.slice(0, 200)
  
  // Extract XML header and footer
  const xmlStart = xmlContent.indexOf('<tv')
  const xmlHeader = xmlContent.substring(0, xmlStart)
  const xmlFooter = '</tv>'
  
  // Build new XML
  return xmlHeader + '\n' + 
         limitedChannels.join('\n') + '\n' + 
         limitedProgrammes.join('\n') + '\n' + 
         xmlFooter
}
