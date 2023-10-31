import React, { useState } from 'react';
import './App.css';
import MessageInput from './MessageInput';

function App() {
  var compressedMessage;
  var response = null;

  const handleCompress = async () => {
    let message = document.getElementById("text_input").value;
    response = await fetch('http://localhost:8000/compress', {
      method: 'POST',
      headers: {
        'Content-Type' : 'text/plain'
      },
      body: message,
    })
      .then((response) => response.json());
      compressedMessage = response.compressed_message;
      console.log(response);
      setCompressedMessage();
  };

  const setCompressedMessage = () => {
    console.log(compressedMessage);
    document.getElementById("compressedMessageText").innerHTML = compressedMessage;
  }

  return (
    <div className="App">
      <h1>Huffman Compression</h1>
      <div>
      <textarea
        rows="4"
        cols="50"
        id = "text_input"
      />
      <button onClick={handleCompress}>Compress</button>
    </div>
      
        <div>
          <h2>Compressed Message:</h2>
          <p id="compressedMessageText"></p>
        </div>

    </div>
  );
}

export default App;