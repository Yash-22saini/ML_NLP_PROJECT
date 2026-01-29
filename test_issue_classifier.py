from src.issue_classifier import detect_issue_category

print(detect_issue_category("Payment was deducted but course not unlocked"))
print(detect_issue_category("Unable to login after update"))
print(detect_issue_category("App crashes frequently"))
print(detect_issue_category("Nice course overall"))
