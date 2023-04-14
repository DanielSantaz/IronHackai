async function summarizeText(lectureText) {
    const response = await fetch('http://localhost:5000/summarize', {
      method: 'POST',
      headers: {
        'Content-Type': 'text/plain',
      },
      body: lectureText,
    });
  
    if (!response.ok) {
      throw new Error('API call failed: ' + response.statusText);
    }
  
    const jsonResponse = await response.json();
    return jsonResponse.summary;
  }
  
  document.getElementById('summarize-form').addEventListener('submit', async (event) => {
    event.preventDefault();
  
    const lectureText = document.getElementById('lecture-text').value;
    const summaryElement = document.getElementById('summary');
  
    try {
      const summary = await summarizeText(lectureText);
      summaryElement.textContent = summary;
    } catch (error) {
      summaryElement.textContent = 'Error: ' + error.message;
    }
  });
  