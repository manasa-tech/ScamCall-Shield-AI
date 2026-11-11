import re
from urllib.parse import urlparse


SUSPICIOUS_KEYWORDS = [
    "urgent",
    "verify your account",
    "account suspended",
    "claim your prize",
    "free gift",
    "lottery winner",
    "send otp",
    "share otp",
    "bank details",
    "password",
    "click immediately",
    "limited offer",
    "investment guaranteed",
    "double your money",
    "send money",
    "upi pin",
    "kyc update",
    "account blocked",
    "win cash",
    "claim reward"
]

URL_SHORTENERS = [
    "bit.ly",
    "tinyurl.com",
    "t.co",
    "is.gd",
    "cutt.ly"
]


def extract_urls(text):
    pattern = r'https?://[^\s<>"\']+|www\.[^\s<>"\']+'
    return re.findall(pattern, text, re.IGNORECASE)


def check_url(url):
    score = 0
    reasons = []

    if url.startswith("www."):
        url = "https://" + url

    try:
        parsed = urlparse(url)
        hostname = parsed.hostname or ""
        domain = hostname.lower()

        if parsed.scheme != "https":
            score += 15
            reasons.append("Website does not use HTTPS")

        if "@" in parsed.netloc:
            score += 25
            reasons.append("URL contains suspicious @ symbol")

        if len(url) > 100:
            score += 10
            reasons.append("Unusually long URL")

        if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", domain):
            score += 25
            reasons.append("Website uses an IP address")

        if domain in URL_SHORTENERS:
            score += 20
            reasons.append("URL uses a shortened link")

        if domain.count("-") >= 3:
            score += 15
            reasons.append("Domain contains multiple hyphens")

        if domain.startswith("xn--") or ".xn--" in domain:
            score += 20
            reasons.append("Domain uses encoded international characters")

        if not hostname or "." not in hostname:
            score += 30
            reasons.append("Invalid or unusual domain")

    except Exception:
        score += 30
        reasons.append("Invalid URL format")

    return min(score, 100), reasons


def detect_scam(content, content_type="message"):

    score = 0
    reasons = []

    text = content.lower()

    # Suspicious keyword detection
    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in text:
            score += 12
            reasons.append(
                f"Suspicious phrase detected: {keyword}"
            )

    # URL analysis
    urls = extract_urls(content)

    for url in urls:
        url_score, url_reasons = check_url(url)

        score += url_score

        for reason in url_reasons:
            reasons.append(f"{url}: {reason}")

    # Sensitive information requests
    if re.search(
        r"\b(otp|upi pin|cvv|password)\b",
        text
    ):
        score += 20
        reasons.append(
            "Potential request for sensitive information"
        )

    # Excessive punctuation
    if text.count("!") >= 4:
        score += 5
        reasons.append("Excessive urgency or punctuation")

    score = min(score, 100)

    if score >= 60:
        status = "SCAM"
        risk_level = "High"

    elif score >= 30:
        status = "SUSPICIOUS"
        risk_level = "Medium"

    else:
        status = "SAFE"
        risk_level = "Low"

    if not reasons:
        reasons.append(
            "No known suspicious patterns detected"
        )

    return {
        "status": status,
        "risk_level": risk_level,
        "risk_score": score,
        "explanation": "; ".join(reasons),
        "detected_urls": urls,
        "content_type": content_type
    }
