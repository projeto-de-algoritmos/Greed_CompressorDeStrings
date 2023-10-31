import React, { useState } from 'react';

function MessageInput({ onCompress }) {
  const [message, setMessage] = useState('');

  const handleCompress = () => {
    onCompress(message);
  };

  return (
    <div>
      <textarea
        rows="4"
        cols="50"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <button onClick={handleCompress}>Compress</button>
    </div>
  );
}

export default MessageInput;