🧠 SentinelAI-plus

AI-powered Log Analysis and Threat Detection Dashboard
Built with Flask, LangChain, and optional local LLMs (Ollama) for privacy-friendly cybersecurity analytics.

🚀 Overview

SentinelAI-plus is a lightweight AI-powered security analysis tool designed to detect potential cyber threats from server logs.
It uses local AI models to summarize and analyze suspicious login attempts and generate human-readable threat insights — all within a clean web dashboard.

⚙️ Features

🔍 Log Analysis Dashboard — Interactive UI to upload and analyze logs in real time.

🧩 AI Detection Engine — Uses Python + LangChain to detect repeated login failures or brute-force indicators.

🧠 Local LLM Support (Ollama) — Keeps data private by running on-device AI inference.

📊 Visualization Ready — Simple JSON-driven detection summary for quick reporting.

🛡️ Privacy Focused — No external APIs; works entirely offline for sensitive environments.

🧰 Tech Stack
Category	Tools Used
Backend	Flask, Python
AI Integration	LangChain, Local LLMs (Ollama)
Frontend	HTML, TailwindCSS
Utilities	Pandas, JSON, CLI integration
Deployment	Localhost / Docker-ready
🧑‍💻 Setup Instructions
# Clone the repository
git clone https://github.com/addyraS/SentinelAI-plus.git

# Navigate into the folder
cd SentinelAI-plus

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
python app.py


Then visit 👉 http://127.0.0.1:5000/
 in your browser.

📸 Dashboard Preview

🧩 Example Use Case

Upload your server log (e.g., system_logs.txt) to:

Detect repeated failed login attempts

Get AI-generated security summaries

View total log counts and alerts in the dashboard

🧠 Learning Goals / Internship Relevance

This project demonstrates:

Hands-on understanding of AI integration in cybersecurity tools

Use of LangChain, Python APIs, and LLMs (Ollama)

Tool testing, AI workflow creation, and documentation, aligning with DRDO’s internship requirements

📜 License

This project is licensed under the MIT License — see the LICENSE
 file for details.

👤 Author

Aditya Rastogi
📧 adityarastogiind@gmail.com
🎓 BCA 
🏫 Pt. Deen Dayal Upadhyay Management College,Meerut
