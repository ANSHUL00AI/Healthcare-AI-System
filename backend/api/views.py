from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# 🔹 Simple Knowledge Base (RAG Simulation)
knowledge_base = {
    "fever cough": {
        "diagnosis": "Viral Infection",
        "treatment": "Take rest, drink fluids, and use paracetamol"
    },
    "headache": {
        "diagnosis": "Migraine or Stress",
        "treatment": "Rest, hydration, and pain relief medication"
    },
    "chest pain": {
        "diagnosis": "Possible Heart Issue",
        "treatment": "Immediate medical attention, ECG recommended"
    },
    "stomach pain": {
        "diagnosis": "Gastritis or Infection",
        "treatment": "Light diet, hydration, and antacids"
    }
}

# 🔹 Function to simulate RAG retrieval
def get_response(summary):
    summary = summary.lower()

    for key in knowledge_base:
        words = key.split()
        if all(word in summary for word in words):
            return knowledge_base[key]

    return {
        "diagnosis": "General illness",
        "treatment": "Consult a doctor for proper diagnosis"
    }


@csrf_exempt
def process_summary(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            summary = data.get("summary", "")

            result = get_response(summary)

            return JsonResponse({
                "input_summary": summary,
                "diagnosis": result["diagnosis"],
                "treatment": result["treatment"]
            })

        except Exception as e:
            return JsonResponse({"error": str(e)})

    return JsonResponse({"error": "Only POST method allowed"})