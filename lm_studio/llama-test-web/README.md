# Setup:
 * Start LM Studio
 * Turn on Server (developer)
 * Load model
 * Server Setting set "Enable CORS" to ON
    * Get URL e.g.: 'http://127.0.0.1:1234' 
    * Choose Endpoint from 'Supported endpoints' e.g.: '/v1/chat/completions'
    * Set 'AI_URL' in this file to {url}{endpoint} e.g.: 'http://localhost:1234/v1/chat/completions'
    * Set 'MODEL' in this file to the model name
