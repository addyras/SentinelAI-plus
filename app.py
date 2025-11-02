from flask import Flask, jsonify, render_template
from log_analyzer import parse_logs, detect_anomalies, summarize_logs_text
from llm_agent import summarize_findings

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['GET'])
def analyze_logs():
    df = parse_logs()
    detection = detect_anomalies(df)
    report = summarize_logs_text(df, detection)
    summary = summarize_findings(report)
    total_logs = len(df)
    alert_count = int(len(df[df['type'] == 'alert'])) if total_logs>0 else 0
    return jsonify({
        "detection": detection,
        "summary": summary,
        "total_logs": total_logs,
        "alert_count": alert_count
    })

if __name__ == '__main__':
    app.run(debug=True)
