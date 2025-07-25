import requests

res = requests.post(
    "http://10.10.1.110:8888/api/ai/post",
    json={
        "url": "http://localhost:11434/api/generate",
        "model": "kanana",
        "prompt": "프롬프트"
    }
)

print(res.json())
