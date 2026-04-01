// Super Simple Cloudflare Worker - Just Limit Characters
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
    
    // Super simple: just return first 50,000 characters
    const truncatedXML = xmlContent.substring(0, 50000)
    
    // Find last complete programme tag to avoid breaking XML
    const lastProgrammeIndex = truncatedXML.lastIndexOf('</programme>')
    const cleanXML = truncatedXML.substring(0, lastProgrammeIndex + 12) + '</tv>'
    
    return new Response(cleanXML, {
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
