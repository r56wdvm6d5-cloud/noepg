// Ultra Simple Cloudflare Worker - Just Stream with Basic Limits
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
    
    // Ultra simple: just return first part of the XML
    const truncatedXML = simpleTruncate(xmlContent)
    
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

function simpleTruncate(xmlContent) {
  // Find first 10 channels
  const channels = []
  let channelMatch
  const channelRegex = /<channel[^>]*>[\s\S]*?<\/channel>/g
  
  while ((channelMatch = channelRegex.exec(xmlContent)) !== null && channels.length < 10) {
    channels.push(channelMatch[0])
  }
  
  // Find first 200 programmes
  const programmes = []
  let programmeMatch
  const programmeRegex = /<programme[^>]*>[\s\S]*?<\/programme>/g
  
  while ((programmeMatch = programmeRegex.exec(xmlContent)) !== null && programmes.length < 200) {
    programmes.push(programmeMatch[0])
  }
  
  // Get XML declaration and tv tag
  const xmlDeclMatch = xmlContent.match(/<\?xml[^>]*\?>/)
  const tvTagMatch = xmlContent.match(/<tv[^>]*>/)
  
  const xmlDecl = xmlDeclMatch ? xmlDeclMatch[0] : '<?xml version="1.0" encoding="UTF-8"?>'
  const tvTag = tvTagMatch ? tvTagMatch[0] : '<tv>'
  
  // Build clean XML
  return xmlDecl + '\n' + 
         tvTag + '\n' + 
         channels.join('\n') + '\n' + 
         programmes.join('\n') + '\n' + 
         '</tv>'
}
