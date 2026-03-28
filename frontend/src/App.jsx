import { useState } from "react";

function App() {
  const [summary, setSummary] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true); // loading will start when we search anything
    const res = await fetch("http://127.0.0.1:8000/process/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text: summary }),
    });

    const data = await res.json();
    setResult(data);
    setLoading(false);  // it will stop the loading .
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.heading}>Healthcare AI System</h1>

      <textarea
        placeholder="Enter patient discharge summary..."
        value={summary}
        onChange={(e) => setSummary(e.target.value)}
        style={styles.textarea}
      />

      <button onClick={handleSubmit} style={styles.button}>
        {loading ? "Analyzing..." : "Generate Diagnosis"}
        
      </button>

      {result && (
        <div style={styles.resultBox}>
          <h2>Diagnosis:</h2>
          <p>{result.diagnosis}</p>
          <h3>Severity:</h3>
          <p>{result.severity}</p>

          <h3>Confidence:</h3>
           <p>{result.confidence}</p>

          <h3>Treatment:</h3>
          <ul>
            {result.recommendations &&
              result.recommendations.map((item, index) => (
                <li key={index}>{item}</li>
              ))}
          </ul>
        </div>
      )}
    </div>
  );
}

const styles = {
  container: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    padding: "40px",
    fontFamily: "Arial",
  },
  heading: {
    fontSize: "32px",
    marginBottom: "20px",
  },
  textarea: {
    width: "500px",
    height: "150px",
    padding: "10px",
    marginBottom: "20px",
  },
  button: {
    padding: "10px 20px",
    backgroundColor: "#007bff",
    color: "white",
    border: "none",
    cursor: "pointer",
  },
  resultBox: {
    marginTop: "20px",
    width: "500px",
    padding: "20px",
    border: "1px solid #ccc",
  },
};

export default App;
