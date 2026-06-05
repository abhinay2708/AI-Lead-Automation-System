from llm import classify_lead


message = """
Need help automating onboarding workflow.
Budget 50k/month.
Can we schedule a call?
"""

result = classify_lead(message)

print(result)