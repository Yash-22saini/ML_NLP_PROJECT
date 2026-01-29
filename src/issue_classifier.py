def detect_issue_category(text: str) -> str:
    text = text.lower()

    payment_keywords = [
        "payment", "refund", "deducted", "charged", "money"
    ]

    access_keywords = [
        "login", "locked", "access", "unable", "password"
    ]

    technical_keywords = [
        "crash", "error", "bug", "slow", "issue", "not loading"
    ]

    for word in payment_keywords:
        if word in text:
            return "PAYMENT"

    for word in access_keywords:
        if word in text:
            return "ACCESS"

    for word in technical_keywords:
        if word in text:
            return "TECHNICAL"

    return "GENERAL"
