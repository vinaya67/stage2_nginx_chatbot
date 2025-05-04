import React, { useState } from 'react';
import axios from 'axios';

interface AnalysisResult {
  filename: string;
  lines: number;
  message: string;
  rally_ticket?: {
    status: string;
    reference?: string;
    details?: string;
  };
}

const App: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [result, setResult] = useState<AnalysisResult | null>(null);
  const [loading, setLoading] = useState<boolean>(false);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      setFile(e.target.files[0]);
    }
  };

  const handleUpload = async () => {
    if (!file) return;
    setLoading(true);
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post<AnalysisResult>(
        'http://localhost:8000/analyze/',
        formData,
        { headers: { 'Content-Type': 'multipart/form-data' } }
      );
      setResult(response.data);
    } catch (error) {
      alert('Error analyzing log file');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'Arial' }}>
      <h1>Jenkins Log Analyzer</h1>
      <input type="file" accept=".log,.txt" onChange={handleFileChange} />
      <button onClick={handleUpload} disabled={!file || loading} style={{ marginLeft: '1rem' }}>
        {loading ? 'Analyzing...' : 'Upload & Analyze'}
      </button>

      {result && (
        <div style={{ marginTop: '2rem' }}>
          <h2>Analysis Result</h2>
          <p><strong>Filename:</strong> {result.filename}</p>
          <p><strong>Total Lines:</strong> {result.lines}</p>
          <p><strong>Message:</strong> {result.message}</p>

          {result.rally_ticket && (
            <div style={{ marginTop: '1rem' }}>
              <h3>Rally Ticket</h3>
              <p><strong>Status:</strong> {result.rally_ticket.status}</p>
              {result.rally_ticket.reference && (
                <p><strong>Reference:</strong> {result.rally_ticket.reference}</p>
              )}
              {result.rally_ticket.details && (
                <pre>{result.rally_ticket.details}</pre>
              )}
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default App;
