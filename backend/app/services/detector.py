import re

HIGH_RISK_KEYWORDS = [
    "share your otp",
    "send otp",
    "tell me your otp",
    "bank account blocked",
    "account will be blocked",
    "share your password",
    "click this link immediately",
    "send your pin",
    "upi pin",
    "remote access",
    "screen sharing",
    "transfer money immediately",
    "verify your account immediately"
]

MEDIUM_RISK_KEYWORDS = [
    "urgent",
    "verify your account",
    "claim your reward",
    "prize",
    "lottery",
    "kyc update",
    "account suspended",
    "unknown link",
    "limited time",
    "act now"
]

def analyze_text(text: str):
    normalized = re.sub(r"\s+", " ", text.lower())

    high_matches = [
        word for word in HIGH_RISK_KEYWORDS
        if word in normalized
    ]

    medium_matches = [
        word for word in MEDIUM_RISK_KEYWORDS
        if word in normalized
    ]

    url_found = bool(
        re.search(r"https?://|www\.", normalized)
    )

    if high_matches or len(medium_matches) >= 2:
        risk = "HIGH"
        confidence = 90
    elif medium_matches or url_found:
        risk = "MEDIUM"
        confidence = 70
    else:
        risk = "LOW"
        confidence = 55

    reasons = high_matches + medium_matches

    if url_found:
        reasons.append("Contains a URL")

    explanation = (
        "Suspicious indicators: " + ", ".join(reasons)
        if reasons
        else "No matching suspicious indicators were detected."
    )

    recommendations = {
        "HIGH": "Do not share OTPs, PINs or passwords. Do not transfer money. Contact your bank using its official number.",
        "MEDIUM": "Do not open suspicious links. Verify the sender through an official channel.",
        "LOW": "No matching warning signs were detected. Still verify unexpected requests."
    }

    return {
        "risk_level": risk,
        "confidence": f"{confidence}%",
        "explanation": explanation,
        "recommendation": recommendations[risk]
    }
