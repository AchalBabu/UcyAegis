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
🔟 Cyber Awareness
0️⃣  Exit

💬 Type option or ask normally.
"""


# =====================================
# BACK TO MENU
# =====================================

BACK_TO_MENU = "\n\n🔙 Type 'menu' for Main Menu.\n"


# =====================================
# BOT RESPONSE FUNCTION
# =====================================

def bot_response(msg, user_name="Guest"):

    msg = msg.lower().strip()


    # =====================================
    # MENU
    # =====================================

    if msg in [
        "menu",
        "main menu",
        "m",
        "back",
        "home"
    ]:

        return MAIN_MENU


    # =====================================
    # SECURITY AUDIT
    # =====================================

    elif msg in [
        "1",
        "security audit",
        "audit"
    ]:

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

📌 Protect your website from hackers before attacks happen.

{BACK_TO_MENU}
"""


    # =====================================
    # PENETRATION TESTING
    # =====================================

    elif msg in [
        "2",
        "penetration testing",
        "pentest"
    ]:

        return f"""
💻 Penetration Testing

✔ Website Pentesting
✔ API Pentesting
✔ Network Pentesting
✔ Wireless Testing
✔ Authentication Bypass
✔ Admin Panel Security

🎯 Find vulnerabilities before attackers do.

{BACK_TO_MENU}
"""


    # =====================================
    # VULNERABILITY ASSESSMENT
    # =====================================

    elif msg in [
        "3",
        "vulnerability assessment",
        "va"
    ]:

        return f"""
⚠ Vulnerability Assessment

✔ CVEs Detection
✔ Open Ports
✔ Weak Configurations
✔ Exposed Data
✔ Outdated Software
✔ Security Weaknesses

📊 Detailed security reports included.

{BACK_TO_MENU}
"""


    # =====================================
    # SOC MONITORING
    # =====================================

    elif msg in [
        "4",
        "soc",
        "soc monitoring"
    ]:

        return f"""
🖥️ SOC Monitoring

✔ Threat Detection
✔ Log Monitoring
✔ Incident Response
✔ Real-Time Analysis
✔ Security Alerts

🔐 24x7 Security Monitoring.

{BACK_TO_MENU}
"""


    # =====================================
    # CLOUD SECURITY
    # =====================================

    elif msg in [
        "5",
        "cloud security"
    ]:

        return f"""
☁ Cloud Security

✔ AWS Security
✔ Azure Security
✔ Identity Security
✔ Cloud Misconfiguration Checks
✔ Compliance Security

🚀 Secure your cloud infrastructure.

{BACK_TO_MENU}
"""


    # =====================================
    # BUG BOUNTY
    # =====================================

    elif msg in [
        "6",
        "bug bounty"
    ]:

        return f"""
🐞 Bug Bounty Assistance

✔ Recon Guidance
✔ Vulnerability Validation
✔ Report Writing
✔ Responsible Disclosure
✔ Security Research

⚡ Ethical hacking only.

{BACK_TO_MENU}
"""


    # =====================================
    # PRICING
    # =====================================

    elif msg in [
        "7",
        "pricing",
        "price"
    ]:

        return f"""
💰 Pricing

🔹 Basic Audit
Starting ₹4,999

🔹 Advanced Pentesting
Starting ₹14,999

🔹 Enterprise Security
Custom Pricing

📞 Contact support for quotation.

{BACK_TO_MENU}
"""


    # =====================================
    # CONTACT
    # =====================================

    elif msg in [
        "8",
        "contact",
        "support"
    ]:

        return f"""
📞 UcyAegis Support

📧 support@ucyaegis.com

🕒 24x7 Customer Support

🔐 Security First Approach

{BACK_TO_MENU}
"""


    # =====================================
    # ABOUT UCYAEGIS
    # =====================================

    elif msg in [
        "9",
        "about",
        "about ucyaegis"
    ]:

        return f"""
🏢 About UcyAegis

✔ Web Security
✔ Penetration Testing
✔ Cyber Defense
✔ Vulnerability Research
✔ Security Monitoring

🎯 Protecting organizations from cyber threats.

{BACK_TO_MENU}
"""


    # =====================================
    # CYBER AWARENESS
    # =====================================

    elif msg in [
        "10",
        "cyber awareness",
        "awareness",
        "cyber tips",
        "security tips"
    ]:

        return f"""
🛡️ Cyber Awareness Guide

━━━━━━━━━━━━━━━━━━━━━━
🔐 PASSWORD SECURITY
━━━━━━━━━━━━━━━━━━━━━━

✔ Use strong passwords
✔ Never reuse passwords
✔ Enable 2FA Authentication
✔ Use password managers

━━━━━━━━━━━━━━━━━━━━━━
📧 EMAIL SAFETY
━━━━━━━━━━━━━━━━━━━━━━

✔ Avoid suspicious links
✔ Verify sender emails
✔ Avoid unknown attachments
✔ Beware of phishing scams

━━━━━━━━━━━━━━━━━━━━━━
🌐 INTERNET SAFETY
━━━━━━━━━━━━━━━━━━━━━━

✔ Use HTTPS websites
✔ Avoid unsafe downloads
✔ Never share OTPs
✔ Update your browser

━━━━━━━━━━━━━━━━━━━━━━
📱 MOBILE SECURITY
━━━━━━━━━━━━━━━━━━━━━━

✔ Install trusted apps only
✔ Avoid cracked APKs
✔ Keep phone updated
✔ Use screen lock

━━━━━━━━━━━━━━━━━━━━━━
🏦 BANKING SECURITY
━━━━━━━━━━━━━━━━━━━━━━

✔ Never share OTP
✔ Verify UPI requests
✔ Beware of fake calls
✔ Use official apps only

━━━━━━━━━━━━━━━━━━━━━━
💻 COMPUTER SECURITY
━━━━━━━━━━━━━━━━━━━━━━

✔ Update Windows regularly
✔ Use antivirus software
✔ Backup important files
✔ Avoid pirated software

━━━━━━━━━━━━━━━━━━━━━━
🎯 SOCIAL MEDIA SAFETY
━━━━━━━━━━━━━━━━━━━━━━

✔ Avoid oversharing
✔ Beware of fake profiles
✔ Use privacy settings
✔ Avoid unknown DMs

━━━━━━━━━━━━━━━━━━━━━━
🚨 COMMON CYBER ATTACKS
━━━━━━━━━━━━━━━━━━━━━━

✔ Phishing
✔ Malware
✔ Ransomware
✔ Keyloggers
✔ Fake Websites
✔ Social Engineering

━━━━━━━━━━━━━━━━━━━━━━
🧠 SMART SECURITY HABITS
━━━━━━━━━━━━━━━━━━━━━━

✔ Think before clicking
✔ Verify before trusting
✔ Stay updated on scams
✔ Learn cyber hygiene

🔐 Stay Safe Online
🌸 UcyAegis Security Awareness Program

{BACK_TO_MENU}
"""


    # =====================================
    # WHO IS ACHAL
    # =====================================

    elif any(w in msg for w in [
        "who is achal",
        "achal kaun hai",
        "achal",
        "founder",
        "ucyaegis founder"
    ]):

        return f"""
👑 Achal Babu

Founder of UcyAegis 🔐

✔ Ethical Hacker
✔ Cybersecurity Researcher
✔ AI Security Builder
✔ Founder of U&S Empire

🎯 Mission:
Building advanced cyber defense systems.

🚀 Future-focused cybersecurity innovation.

{BACK_TO_MENU}
"""


    # =====================================
    # PYTHON
    # =====================================

    elif "python" in msg:

        return f"""
🐍 Python

✔ Automation
✔ Cybersecurity
✔ AI Development
✔ Web Development
✔ Ethical Hacking

🚀 Powerful and beginner friendly.

{BACK_TO_MENU}
"""


    # =====================================
    # LINUX
    # =====================================

    elif "linux" in msg:

        return f"""
🐧 Linux

✔ Fast
✔ Secure
✔ Terminal Power
✔ Best for Hackers

💻 Kali Linux is widely used in cybersecurity.

{BACK_TO_MENU}
"""


    # =====================================
    # CEH
    # =====================================

    elif "ceh" in msg:

        return f"""
🎓 CEH

CEH = Certified Ethical Hacker

✔ Web Hacking
✔ Network Security
✔ Exploitation
✔ Reconnaissance
✔ Vulnerability Analysis

🚀 Popular cybersecurity certification.

{BACK_TO_MENU}
"""


    # =====================================
    # CYBER SECURITY
    # =====================================

    elif "cyber security" in msg or "cybersecurity" in msg:

        return f"""
🔐 Cyber Security

Cybersecurity protects systems,
networks, and data from attacks.

✔ Web Security
✔ Cloud Security
✔ Malware Protection
✔ Ethical Hacking

🌐 Digital protection is essential today.

{BACK_TO_MENU}
"""


    # =====================================
    # PHISHING
    # =====================================

    elif "phishing" in msg:

        return f"""
🎣 Phishing Attack

Phishing is a fake message or website
used to steal passwords, OTPs,
or banking details.

⚠ Never click suspicious links.

{BACK_TO_MENU}
"""


    # =====================================
    # MALWARE
    # =====================================

    elif "malware" in msg:

        return f"""
☠ Malware

Malware is harmful software that can:

✔ Steal data
✔ Damage systems
✔ Spy on users
✔ Encrypt files

⚠ Avoid downloading unknown files.

{BACK_TO_MENU}
"""


    # =====================================
    # OTP SCAM
    # =====================================

    elif "otp" in msg:

        return f"""
📲 OTP Scam Alert

Never share your OTP with anyone.

⚠ Banks never ask for OTPs.

✔ Verify calls
✔ Avoid fake payment links
✔ Beware of scam messages

{BACK_TO_MENU}
"""


    # =====================================
    # GREETING
    # =====================================

    elif any(w in msg for w in [
        "hello",
        "hi",
        "hey",
        "namaste"
    ]):

        return f"""
Hello {user_name} 👋

I'm Ganga,
your AI Security Guide 🌸

How can I help you today?

{BACK_TO_MENU}
"""


    # =====================================
    # THANK YOU
    # =====================================

    elif "thank" in msg:

        return f"""
You're welcome {user_name} 😊

🌸 Always here to help.

{BACK_TO_MENU}
"""


    # =====================================
    # TIME
    # =====================================

    elif "time" in msg:

        current_time = datetime.now().strftime("%H:%M:%S")

        return f"""
⏰ Current Time

{current_time}

{BACK_TO_MENU}
"""


    # =====================================
    # GANGA
    # =====================================

    elif "ganga" in msg:

        return f"""
🌸 Hi {user_name}

I am Ganga,
your UcyAegis AI Assistant.

Ask me anything 😊

{BACK_TO_MENU}
"""


    # =====================================
    # EXIT
    # =====================================

    elif msg in [
        "0",
        "bye",
        "exit"
    ]:

        return f"""
Goodbye {user_name} 👋

Stay Secure 🔐

🌸 Ganga: Take care 😊
"""


    # =====================================
    # DEFAULT RESPONSE
    # =====================================

    else:

        return f"""
🤖 Sorry, I didn't understand that.

🌸 Please choose an option:

1️⃣  Security Audit
2️⃣  Penetration Testing
3️⃣  Vulnerability Assessment
4️⃣  SOC Monitoring
5️⃣  Cloud Security
6️⃣  Bug Bounty Support
7️⃣  Pricing
8️⃣  Contact Support
9️⃣  About UcyAegis
🔟 Cyber Awareness
0️⃣  Exit

💡 Type 'menu' anytime.
"""