import { useState } from "react";
import axios from "axios";

export default function App() {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleClick = async () => {
    if (!file) return;

    // Create FormData and append the file name as 'file_path'
    const formData = new FormData();
    formData.append("file_path", file.name);

    try {
      const res = await axios.post("http://127.0.0.1:8000/classify", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      console.log("✅ Response:", res.data);
      alert("File path sent successfully!");
    } catch (err) {
      console.error("❌ Upload error:", err);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-6">
      <div className="bg-white shadow-lg rounded-2xl p-8 w-full max-w-md text-center">
        <h1 className="text-2xl font-semibold text-gray-800 mb-6">
          🧠 Resume Classifier
        </h1>

        <div className="border-2 border-dashed border-gray-300 rounded-xl p-6 hover:border-blue-500 transition cursor-pointer w-full">
          <input
            type="file"
            accept="application/pdf"
            id="fileInput"
            onChange={handleFileChange}
            className="hidden"
          />
          <label htmlFor="fileInput" className="block text-gray-600">
            {file ? (
              <p className="font-medium text-gray-800">{file.name}</p>
            ) : (
              <p>Click to upload your resume (PDF)</p>
            )}
          </label>
        </div>

        {file && (
          <button
            className="mt-6 bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded-xl transition"
            onClick={handleClick}
          >
            Upload
          </button>
        )}
      </div>

      <p className="text-gray-400 text-sm mt-6">
        Built with ❤️ using React + TailwindCSS
      </p>
    </div>
  );
}
