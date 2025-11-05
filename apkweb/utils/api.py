import requests
import json

# ========== DRIBBBLE API ==========
def get_dribbble_designs(query, access_token):
    url = f"https://api.dribbble.com/v2/search/shots?query={query}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("shots", [])
    else:
        return []

# ========== FIGMA API ==========
def get_figma_templates(query, figma_token, file_id):
    url = f"https://api.figma.com/v1/files/{file_id}/search?q={query}"
    headers = {"X-Figma-Token": figma_token}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("meta", {}).get("nodes", [])
    else:
        return []

# ========== GLM.AI / NLP API ==========
def chat_with_glm(prompt, api_key):
    url = "https://api.glm.ai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    data = {
        "model": "glm-4",  
        "messages": [{"role": "user", "content": prompt}],
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.text}"
