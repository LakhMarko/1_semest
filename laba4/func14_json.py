"""Вбудований модуль json."""
import json

def demo_json():
    student = {"name": "Олена", "grade": 10}
    encoded = json.dumps(student, ensure_ascii=False)
    print("JSON:", encoded)
    print("Після читання:", json.loads(encoded))
