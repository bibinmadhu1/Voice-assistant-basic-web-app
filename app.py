from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your DeepSeek API key
DEEPSEEK_API_KEY = "your_deepseek_api_key_here"
DEEPSEEK_ENDPOINT = "https://api.deepseek.com/v1/query"  # Replace with actual endpoint

@app.route("/query", methods=["POST"])
def query_deepseek():
    user_input = request.json.get("query")
    if not user_input:
        return jsonify({"error": "No query provided"}), 400

    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "query": user_input
    }
    response = requests.post(DEEPSEEK_ENDPOINT, headers=headers, json=data)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch data from DeepSeek"}), 500

if __name__ == "__main__":
    app.run(debug=True)
