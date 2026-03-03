def categorize(text):
    text = text.lower()

    hr_keywords = ["employee", "salary", "recruitment", "leave", "hr"]
    finance_keywords = ["invoice", "tax", "payment", "balance", "amount"]
    operations_keywords = ["logistics", "delivery", "operations", "supply"]
    legal_keywords = ["contract", "agreement", "legal", "compliance"]

    if any(word in text for word in hr_keywords):
        return "HR"
    elif any(word in text for word in finance_keywords):
        return "Finance"
    elif any(word in text for word in operations_keywords):
        return "Operations"
    elif any(word in text for word in legal_keywords):
        return "Legal"
    else:
        return "Unknown"