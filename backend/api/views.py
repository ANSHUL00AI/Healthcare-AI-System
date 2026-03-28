from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def process_summary(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        text = data.get('text', '').lower()

        diagnosis = ""
        severity = ""
        confidence = ""
        recommendations = []
        warning = ""

        if "fever" in text and "cough" in text:
            diagnosis = "Likely Viral Respiratory Infection"
            severity = "Mild to Moderate"
            confidence = "High"
            recommendations = [
                "Take paracetamol for fever",
                "Stay hydrated",
                "Use cough syrup if needed",
                "Get adequate rest"
            ]
            warning = "Consult a doctor if symptoms persist beyond 3-5 days"

        elif "chest pain" in text:
            diagnosis = "Possible Cardiac Issue"
            severity = "Severe"
            confidence = "High"
            recommendations = [
                "Seek immediate medical attention",
                "Avoid physical exertion"
            ]
            warning = "This may be a serious condition. Do not delay medical help."

        elif "headache" in text:
            diagnosis = "Migraine or Stress-related Headache"
            severity = "Mild"
            confidence = "Medium"
            recommendations = [
                "Take rest in a quiet room",
                "Use mild pain relievers",
                "Stay hydrated"
            ]
            warning = "If headache is severe or frequent, consult a doctor"

        elif "fever" in text:
            diagnosis = "General Fever (Possible Infection)"
            severity = "Mild"
            confidence = "Medium"
            recommendations = [
                "Take paracetamol",
                "Drink plenty of fluids",
                "Monitor temperature regularly"
            ]
            warning = "Consult doctor if fever exceeds 102°F or lasts more than 2 days"

        else:
            diagnosis = "Symptoms are unclear"
            severity = "Unknown"
            confidence = "Low"
            recommendations = [
                "Consult a healthcare professional for proper diagnosis"
            ]
            warning = "More detailed information is required"

        return JsonResponse({
            "diagnosis": diagnosis,
            "severity": severity,
            "confidence": confidence,
            "recommendations": recommendations,
            "warning": warning
        })

    return JsonResponse({"error": "Only POST method allowed"})