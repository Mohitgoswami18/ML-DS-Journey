import { useState } from "react";
import axios from 'axios'

export default function App() {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleClick = (filePath) =>  {
    // Create a form and then send it int he body of the request.
    axios.post('/this is the routing path for the backend', {
      file
    })
  }

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
            onClick={() => handleClick(file.name)}
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
