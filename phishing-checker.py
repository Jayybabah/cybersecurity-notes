# Phishing Email Checker - by Aliyu Abdulkadir Baba
# @Jayybabah | Baze University Cybersecurity + iSoftDev
# This tool helps users detect suspicious phishing emails/links

print("=" * 50)
print("  PHISHING EMAIL CHECKER 🛡️")
print("  By Aliyu Abdulkadir Baba")
print("=" * 50)
print()

email_text = input("Paste the email or link here: ").lower()

# Suspicious words scammers use
suspicious_words = [
    "urgent",
    "verify your account",
    "suspended",
    "free money",
    "click here",
    "winner",
    "congratulations you won",
    "update your password",
    "confirm your bvn",
    "your account will be blocked"
]

# Suspicious links / domains
suspicious_links = [
    "bit.ly",
    "tinyurl",
    "free-",
    "login-verify",
    "moniepoint-verify",
    "opay-secure"
]

score = 0
reasons = []

# Check for suspicious words
for word in suspicious_words:
    if word in email_text:
        score += 2
        reasons.append(f"Found suspicious phrase: '{word}'")

# Check for suspicious links
for link in suspicious_links:
    if link in email_text:
        score += 3
        reasons.append(f"Found suspicious link: '{link}'")

# Check for @ with strange domain
if "@" in email_text and "gmail.com" not in email_text and "yahoo.com" not in email_text:
    # Just for learning - many phishing emails use fake domains
    pass

print()
print("=" * 50)
print("  RESULT")
print("=" * 50)

if score == 0:
    print("✅ SAFE: No phishing signs found.")
    print("But still be careful - always check the sender.")
elif score <= 3:
    print("⚠️  SUSPICIOUS: Be careful!")
    print(f"Risk Score: {score}/10")
else:
    print("🚨 HIGH RISK: This looks like PHISHING!")
    print(f"Risk Score: {score}/10")
    print("DO NOT click any link. DO NOT send money or BVN.")

print()
if reasons:
    print("Why we flagged it:")
    for r in reasons:
        print(f" - {r}")

print()
print("Tip: Real banks will NEVER ask for your BVN, PIN, or OTP by email/WhatsApp.")
print("Stay safe - Aliyu")
