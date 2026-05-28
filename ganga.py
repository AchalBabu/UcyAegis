from datetime import datetime

# =====================================
# MAIN MENU
# =====================================

MAIN_MENU = """
━━━━━━━━━━━━━━━━━━━━━━
🔐 UcyAegis Main Menu
━━━━━━━━━━━━━━━━━━━━━━

1️⃣  Security Audit
2️⃣  Penetration Testing
3️⃣  Vulnerability Assessment
4️⃣  SOC Monitoring
5️⃣  Cloud Security
6️⃣  Bug Bounty Support
7️⃣  Pricing
8️⃣  Contact Support
9️⃣  About UcyAegis
0️⃣  Exit

💬 Type option or ask normally.
"""

BACK_TO_MENU = "\n\n🔙 Type 'menu' for Main Menu.\n"

# =====================================
# BOT RESPONSE
# =====================================

def bot_response(msg, user_name="Guest"):

    msg = msg.lower().strip()

    # =========================
    # MENU
    # =========================

    if msg in ["menu", "main menu", "m", "back", "home"]:

        return MAIN_MENU

    # =========================
    # SECURITY AUDIT
    # =========================

    elif msg in ["1", "security audit", "audit"]:

        return f"""
🛡️ Web Security Audit

✔ SQL Injection Testing
✔ XSS Testing
✔ Authentication Testing
✔ Session Security Review
✔ API Security Testing
✔ Server Misconfiguration
✔ Weak Password Testing
✔ Security Headers Analysis
✔ OWASP Top 10 Testing

📌 Protect your website from
hackers before attacks happen.

{BACK_TO_MENU}
"""

    # =========================
    # PENTEST
    # =========================

    elif msg in ["2", "penetration testing", "pentest"]:

        return f"""
💻 Penetration Testing

Real-world attack simulation
to find system vulnerabilities.

🔍 Testing Areas:

• Website Pentesting
• API Pentesting
• Network Pentesting
• Wireless Testing
• Authentication Bypass
• Admin Panel Security

🎯 Find vulns before attackers do.

{BACK_TO_MENU}
"""

    # =========================
    # VULNERABILITY ASSESSMENT
    # =========================

    elif msg in ["3", "vulnerability assessment", "va"]:

        return f"""
⚠ Vulnerability Assessment

We scan systems for:

✔ CVEs
✔ Outdated Software
✔ Open Ports
✔ Weak Configurations
✔ Exposed Sensitive Data
✔ Security Weaknesses

📊 Detailed reports included.

{BACK_TO_MENU}
"""

    # =========================
    # SOC
    # =========================

    elif msg in ["4", "soc", "soc monitoring"]:

        return f"""
🖥️ SOC Monitoring

24x7 Security Monitoring.

✔ Threat Detection
✔ Suspicious Activity Alerts
✔ Log Monitoring
✔ Incident Response
✔ Real-Time Analysis

🔐 Always protected.

{BACK_TO_MENU}
"""

    # =========================
    # CLOUD SECURITY
    # =========================

    elif msg in ["5", "cloud security"]:

        return f"""
☁ Cloud Security

✔ AWS Security
✔ Azure Security
✔ Cloud Misconfiguration
✔ Identity & Access Security
✔ Cloud Compliance Checks

🚀 Secure your cloud infra.

{BACK_TO_MENU}
"""

    # =========================
    # BUG BOUNTY
    # =========================

    elif msg in ["6", "bug bounty"]:

        return f"""
🐞 Bug Bounty Assistance

✔ Recon Guidance
✔ Vulnerability Validation
✔ Report Writing
✔ Responsible Disclosure
✔ Web Security Research

⚡ Ethical hacking only.

{BACK_TO_MENU}
"""

    # =========================
    # PRICING
    # =========================

    elif msg in ["7", "pricing", "price"]:

        return f"""
💰 Pricing

🔹 Basic Website Audit:
    Starting ₹4,999

🔹 Advanced Pentesting:
    Starting ₹14,999

🔹 Enterprise Security:
    Custom Pricing

📞 Contact support for quote.

{BACK_TO_MENU}
"""

    # =========================
    # CONTACT
    # =========================

    elif msg in ["8", "contact", "support"]:

        return f"""
📞 UcyAegis Support

📧 Email:
    support@ucyaegis.com

🕒 Availability:
    24x7 Customer Support

🔐 Security First Approach.

{BACK_TO_MENU}
"""

    # =========================
    # ABOUT
    # =========================

    elif msg in ["9", "about", "about ucyaegis"]:

        return f"""
🏢 About UcyAegis

Cybersecurity company focused on:

✔ Web Security
✔ Penetration Testing
✔ Cyber Defense
✔ Vulnerability Research
✔ Security Monitoring

🎯 Protect organizations from
modern cyber threats.

{BACK_TO_MENU}
"""

    # =========================
    # EXIT
    # =========================

    elif msg in ["0", "bye", "exit"]:

        return f"""
Goodbye {user_name} 👋

Stay Secure 🔐

🌸 Ganga: Take care! 😊
"""

    # =========================
    # GREETING
    # =========================

    elif any(w in msg for w in ["hello", "hi", "hey", "namaste"]):

        return f"""
Hello {user_name} 👋

I'm Ganga,
your AI Security Guide 🌸

How can I help you today?

{BACK_TO_MENU}
"""

    # =========================
    # THANK YOU
    # =========================

    elif "thank" in msg:

        return f"""
You're welcome {user_name} 😊

🌸 Always here to help!

{BACK_TO_MENU}
"""

    # =========================
    # TIME
    # =========================

    elif "time" in msg:

        current_time = datetime.now().strftime("%H:%M:%S")

        return f"""
⏰ Current Time:

{current_time}

{BACK_TO_MENU}
"""

    # =========================
    # GANGA
    # =========================

    elif "ganga" in msg:

        return f"""
🌸 Hi {user_name}!

I am Ganga,
your UcyAegis AI Care Guide.

Ask me anything 😊

{BACK_TO_MENU}
"""

    # =========================
    # DEFAULT
    # =========================

    else:

        return f"""
🤖 Didn't understand that.

🌸 Please choose:

1️⃣  Security Audit
2️⃣  Penetration Testing
3️⃣  Vulnerability Assessment
4️⃣  SOC Monitoring
5️⃣  Cloud Security
6️⃣  Bug Bounty Support
7️⃣  Pricing
8️⃣  Contact Support
9️⃣  About UcyAegis
0️⃣  Exit

💡 Type 'menu' anytime.
"""