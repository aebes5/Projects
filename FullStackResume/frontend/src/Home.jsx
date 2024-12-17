import React, { useState } from "react";
import FileUploadForm from "./FileUploadForm"; // Assuming this is your file upload component

const Home = () => {
  const [uploadResponse, setUploadResponse] = useState(null); // Store file upload response
  const [latexCode, setLatexCode] = useState(""); // Store LaTeX code in the editor
  const [pdfBlob, setPdfBlob] = useState(null); // Store compiled PDF as a Blob
  const [isUploading, setIsUploading] = useState(false); // Track upload state

  // Handle upload complete and set LaTeX code from the upload response
  const handleUploadComplete = (data) => {
    setUploadResponse(data);
    if (data.template) {
      setLatexCode(data.template); // Set LaTeX content in the editor
    }
    setIsUploading(false); // Hide file upload form once upload is complete
  };

  // Handle LaTeX code change in the editor
  const handleLatexChange = (e) => {
    setLatexCode(e.target.value);
  };

  // Function to compile LaTeX into a PDF using backend
  const handleCompileLatex = async () => {
    try {
      const response = await fetch("http://localhost:5000/compile", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ latexCode }),
      });

      if (!response.ok) {
        const errorDetails = await response.text();
        throw new Error(`Server error: ${errorDetails}`);
      }

      // Handle the PDF Blob returned from the server
      const blob = await response.blob();
      setPdfBlob(blob); // Store the blob in state
      alert("PDF compiled successfully!");
    } catch (error) {
      console.error("Error compiling LaTeX:", error);
      alert(`Failed to compile LaTeX: ${error.message}`);
    }
  };

  // Function to download the compiled PDF
  const handleDownloadPDF = () => {
    if (!pdfBlob) return;

    // Create a temporary URL for the PDF Blob and trigger download
    const url = URL.createObjectURL(pdfBlob);
    const link = document.createElement("a");
    link.href = url;
    link.download = "compiled_document.pdf"; // Default filename
    link.click();
    URL.revokeObjectURL(url); // Revoke the URL after download
  };

  return (
    <div>
      <h1>Welcome!</h1>
      <h2>Generate a Resume and Feedback</h2>
      
      {/* Keep the FileUploadForm always visible */}
      <FileUploadForm onUploadComplete={handleUploadComplete} />
      
      {/* Once the upload is complete, show the editor and compile buttons */}
      {uploadResponse && (
        <div>
          <h2>Generated Resume and Feedback:</h2>
          <p>Overall Similarity Before Tailoring: {uploadResponse.overall_sim}</p>
          <p>Generated Feedback:</p>
        </div>
      )}

      {/* Only show the LaTeX editor after file is uploaded */}
      {uploadResponse && (
        <div style={{ display: "flex", flexDirection: "row", gap: "20px", alignItems: "flex-start" }}>
          {/* Container for buttons above the editor */}
          <div style={{ width: "100%", marginBottom: "20px" }}>
            <button onClick={handleCompileLatex}>Compile LaTeX</button>
            {pdfBlob && (
              <button
                onClick={handleDownloadPDF}
                style={{ marginLeft: "10px" }}
              >
                Download PDF
              </button>
            )}
          </div>

          {/* LaTeX Editor - Wider layout */}
          <div style={{ width: "60%", padding: "10px", display: "flex", flexDirection: "column" }}>
            <textarea
              value={latexCode}
              onChange={handleLatexChange}
              placeholder="Edit LaTeX content here..."
              style={{
                width: "100%",
                height: "90vh",
                fontFamily: "monospace",
                padding: "10px",
                border: "1px solid #ccc",
                borderRadius: "5px",
                resize: "none", // Prevent resizing the textarea
              }}
            />
          </div>

          {/* PDF Preview next to the LaTeX editor */}
          {pdfBlob && (
            <div style={{ width: "35%", padding: "10px", display: "flex", flexDirection: "column" }}>
              <h3>Preview PDF:</h3>
              <embed
                src={URL.createObjectURL(pdfBlob)}
                width="100%"
                height="90vh"
                type="application/pdf"
              />
              <p>Overall Similarity After Tailoring: </p>
            </div>
            
          )}
        </div>
      )}
    </div>
  );
};

export default Home;
