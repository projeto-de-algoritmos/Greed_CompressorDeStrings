import React, { useState } from "react";
import styles from "./styles.module.css";

export default function App() {
  const [message, setMessage] = useState("");
  const [compressedMessage, setCompressedMessage] = useState("");

  async function handleCompress(e) {
    e.preventDefault();

    const response = await fetch(`http://localhost:8000/compress/${message}`);

    if (response.status === 200) {
      setCompressedMessage(await response.json());
    } else {
      alert("Ocorreu um erro ao acessar o servidor.");
    }
  }

  return (
    <div className={styles.container}>
      <h1>Huffman Compression</h1>

      <form onSubmit={handleCompress} className={styles.form}>
        <textarea
          rows="4"
          cols="50"
          required
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />
        <button type="submit">Compress</button>
      </form>

      <div className={styles.result}>
        <h2>Compressed Message:</h2>
        <p>{compressedMessage}</p>
      </div>
    </div>
  );
}
