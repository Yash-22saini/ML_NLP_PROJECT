def assign_priority(sentiment: str, issue_category: str) -> str:
    sentiment = sentiment.upper()
    issue_category = issue_category.upper()

    if sentiment == "NEGATIVE" and issue_category in ["PAYMENT", "ACCESS"]:
        return "HIGH"

    if sentiment == "NEGATIVE":
        return "MEDIUM"

    if sentiment == "NEUTRAL":
        return "MEDIUM"

    return "LOW"


def recommend_action(priority: str) -> str:
    actions = {
        "HIGH": "Immediate support intervention required",
        "MEDIUM": "Review and respond within 24 hours",
        "LOW": "No immediate action required"
    }

    return actions.get(priority, "No action defined")

