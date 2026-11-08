import re

HIGH_RISK_KEYWORDS = [
    "share your otp",
    "send your otp",
    "tell me your otp",
    "share your password",
    "share your pin",
    "bank account blocked",
    "account will be blocked",
    "upi pin",
    "transfer money immediately",
    "remote access",
    "screen sharing",
    "send your banking details"
]

MEDIUM_RISK_KEYWORDS = [
    "urgent",
    "verify your account",
    "claim your reward",
    "you won a prize",
    "lottery",
    "kyc update",
    "account suspended",
    "limited time",
    "act now",
    "click this link"
]

def analyze_text(text: str):
    normalized = re.sub(r"\s+", " ", text.lower())

    high_matches = [
        keyword for keyword in HIGH_RISK_KEYWORDS
        if keyword in normalized
    ]

    medium_matches = [
        keyword for keyword in MEDIUM_RISK_KEYWORDS
        if keyword in normalized
    ]

    url_found = bool(
        re.search(r"https?://|www\.", normalized)
    )

    score = (
        len(high_matches) * 35
        + len(medium_matches) * 15
        + (20 if url_found else 0)
    )

    score = min(score, 100)

    if score >= 35:
        risk = "HIGH"
    elif score >= 15:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    reasons = high_matches + medium_matches

    if url_found:
        reasons.append("Contains a URL")

    if reasons:
        explanation = (
            "Suspicious indicators detected: "
            + ", ".join(reasons)
        )
    else:
        explanation = (
            "No matching suspicious keywords or URL indicators "
            "were detected."
        )

    recommendations = {
        "HIGH": (
            "Do not share OTPs, PINs, passwords, or transfer money. "
            "Contact your bank through its official channel."
        ),
        "MEDIUM": (
            "Avoid clicking unknown links. Verify the sender "
            "independently before taking action."
        ),
        "LOW": (
            "No matching warning indicators were found. "
            "Still verify unexpected requests."
        )
    }

    return {
        "risk_level": risk,
        "confidence": f"{score}%",
        "risk_score": score,
        "explanation": explanation,
        "recommendation": recommendations[risk]
    }
