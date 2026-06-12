const toggle = document.querySelector(".nav-toggle");
const links = document.querySelector(".nav-links");

if (toggle && links) {
  toggle.addEventListener("click", () => {
    const isOpen = links.classList.toggle("open");
    toggle.setAttribute("aria-expanded", String(isOpen));
  });
}

const current = location.pathname.split("/").pop() || "index.html";
document.querySelectorAll(".nav-links a").forEach((link) => {
  const href = link.getAttribute("href");
  if (href === current) {
    link.classList.add("active");
  }
});

const year = document.querySelector("[data-year]");
if (year) {
  year.textContent = new Date().getFullYear();
}

const gangaReplies = [
  {
    keys: ["service", "services", "soc", "monitoring", "managed"],
    text: "UCY Aegis provides end-to-end cybersecurity services including Managed SOC, 24/7 Security Monitoring, Threat Detection & Response, Penetration Testing, Vulnerability Assessments, Incident Response, Cloud Security, Security Architecture Reviews, Compliance Support, and Employee Security Awareness Programs. To recommend the best solution, please share your industry, company size, and security objectives."
  },

  {
    keys: ["product", "products", "endpoint", "identity", "vulnerability"],
    text: "Our security solutions are designed to strengthen your organization's cyber resilience. We offer Endpoint Protection, Identity & Access Security, Vulnerability Management, Security Awareness Platforms, Compliance Evidence Tracking, Risk Assessment Tools, and SOC Automation Workflows. Let us know your requirements and we can guide you to the most suitable solution."
  },

  {
    keys: ["training", "certification", "course", "learn", "student"],
    text: "UCY Aegis offers professional cybersecurity training and certification programs for students, working professionals, and corporate teams. Popular tracks include Cyber Security Foundations, SOC Analyst Training, Ethical Hacking, Penetration Testing, Cloud Security, Governance Risk & Compliance (GRC), and Security Leadership Programs. We provide hands-on labs, practical projects, and industry-oriented learning paths. Ask for course syllabus, duration, certification details, or upcoming batches."
  },

  {
    keys: ["price", "cost", "pricing", "fees", "budget"],
    text: "Pricing varies depending on project scope, number of assets, security requirements, training batch size, support level, and compliance objectives. We provide customized quotations to ensure you receive the most cost-effective solution. Please submit your requirements through the Contact page and our team will prepare a tailored proposal."
  },

  {
    keys: ["incident", "breach", "hacked", "ransomware", "urgent"],
    text: "If your organization is currently experiencing a cyber incident, ransomware attack, unauthorized access, data breach, or suspicious activity, immediate action is critical. Isolate affected systems where possible, preserve logs and evidence, avoid deleting files, and refrain from making major system changes until the situation is assessed. Contact UCY Aegis immediately for professional incident response assistance and recovery guidance."
  },

  {
    keys: ["contact", "email", "phone", "call", "demo"],
    text: "You can reach UCY Aegis through the Contact page for consultations, product demonstrations, security assessments, training inquiries, partnership opportunities, or career-related discussions. Please include your name, organization, email address, and a brief description of your requirement so our team can respond efficiently."
  },

  {
    keys: ["compliance", "iso", "audit", "gdpr", "soc2"],
    text: "UCY Aegis assists organizations with compliance readiness, audit preparation, policy development, risk assessments, evidence collection, and security controls implementation. We support frameworks such as ISO 27001, SOC 2, GDPR, PCI DSS, HIPAA, and other regulatory requirements. Share your compliance goals and we will recommend the appropriate roadmap."
  },

  {
    keys: ["pentest", "penetration", "vapt", "assessment"],
    text: "Our Penetration Testing and VAPT services help identify vulnerabilities before attackers can exploit them. Assessments may include web applications, APIs, cloud environments, networks, mobile applications, and internal infrastructure. Detailed reports include risk ratings, proof of concept findings, and remediation recommendations."
  },

  {
    keys: ["career", "job", "internship", "hiring"],
    text: "Interested in joining UCY Aegis? We regularly explore opportunities for cybersecurity professionals, interns, researchers, trainers, and security analysts. Please submit your resume and area of interest through the Contact page or Careers section for future opportunities."
  },

  {
    keys: ["cloud", "aws", "azure", "gcp"],
    text: "Our Cloud Security services help organizations secure AWS, Azure, and Google Cloud environments through configuration reviews, identity management, vulnerability assessments, monitoring, compliance validation, and security best-practice implementation."
  },

  {
    keys: ["awareness", "employee", "phishing"],
    text: "Human error remains one of the biggest cybersecurity risks. UCY Aegis provides Security Awareness Training, Phishing Simulations, Executive Briefings, and Employee Education Programs to help organizations build a strong security culture and reduce cyber risk."
  },

  {
    keys: ["website", "web", "application"],
    text: "We provide Web Application Security Assessments, Secure Development Reviews, API Security Testing, Configuration Reviews, and Website Security Audits to help identify vulnerabilities and improve your application's security posture."
  }
];

function createGangaAi() {
  if (document.querySelector(".ganga-ai")) return;

  const widget = document.createElement("section");
  widget.className = "ganga-ai";
  widget.setAttribute("aria-label", "Ganga AI 24/7 support");
  widget.innerHTML = `
    <div class="ganga-panel" role="dialog" aria-label="Ganga AI support chat">
      <div class="ganga-head">
        <div class="ganga-profile">
          <img class="ganga-avatar" src="assets/ganga-ai.jpeg" alt="Ganga AI assistant">
          <div>
            <span class="ganga-title">Ganga AI</span>
            <span class="ganga-status">24/7 UCY Aegis support</span>
          </div>
        </div>
        <button class="ganga-close" type="button" aria-label="Close Ganga AI">&times;</button>
      </div>
      <div class="ganga-body" aria-live="polite">
        <div class="ganga-message bot">Hi, I am Ganga AI. I can help with cyber security services, products, training, certification, pricing questions, and urgent incident guidance.</div>
        <div class="ganga-chips">
          <button class="ganga-chip" type="button" data-question="I need cyber security services">Services</button>
          <button class="ganga-chip" type="button" data-question="Tell me about training and certification">Training</button>
          <button class="ganga-chip" type="button" data-question="I want product details">Products</button>
          <button class="ganga-chip" type="button" data-question="I need urgent incident support">Incident help</button>
        </div>
      </div>
      <form class="ganga-foot">
        <input class="ganga-input" name="ganga-message" type="text" autocomplete="off" placeholder="Ask Ganga AI..." aria-label="Message for Ganga AI">
        <button class="ganga-send" type="submit" aria-label="Send message">Send</button>
        <span class="ganga-note">For real-time human response, submit details on the Contact page.</span>
      </form>
    </div>
    <button class="ganga-launch" type="button" aria-label="Open Ganga AI support">
      <img src="assets/ganga-ai.jpeg" alt="">
      <span><strong>Ganga AI</strong><span>24/7 support</span></span>
    </button>
  `;

  document.body.appendChild(widget);

  const panelBody = widget.querySelector(".ganga-body");
  const form = widget.querySelector(".ganga-foot");
  const input = widget.querySelector(".ganga-input");
  const launch = widget.querySelector(".ganga-launch");
  const close = widget.querySelector(".ganga-close");

  const addMessage = (text, type) => {
    const message = document.createElement("div");
    message.className = `ganga-message ${type}`;
    message.textContent = text;
    panelBody.appendChild(message);
    panelBody.scrollTop = panelBody.scrollHeight;
  };

  const getReply = (question) => {
    const lower = question.toLowerCase();
    const match = gangaReplies.find((reply) => reply.keys.some((key) => lower.includes(key)));
    if (match) return match.text;
    return "I can help with UCY Aegis services, products, training, certifications, incidents, and contact guidance. Please share a little more detail, or use the Contact page for a direct enquiry.";
  };

  const ask = (question) => {
    const clean = question.trim();
    if (!clean) return;
    addMessage(clean, "user");
    input.value = "";
    window.setTimeout(() => addMessage(getReply(clean), "bot"), 260);
  };

  launch.addEventListener("click", () => {
    widget.classList.add("open");
    input.focus();
  });

  close.addEventListener("click", () => {
    widget.classList.remove("open");
  });

  widget.querySelectorAll(".ganga-chip").forEach((chip) => {
    chip.addEventListener("click", () => ask(chip.dataset.question || chip.textContent));
  });

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    ask(input.value);
  });
}

createGangaAi();

const slides = document.querySelectorAll('.testimonial-slide');

let currentSlide = 0;

setInterval(() => {
  slides[currentSlide].classList.remove('active');

  currentSlide = (currentSlide + 1) % slides.length;

  slides[currentSlide].classList.add('active');
}, 4000);

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector('form[name="contact"]');

    if (form) {
        form.addEventListener("submit", function () {
            setTimeout(() => {
                form.innerHTML = `
                    <div class="success-box">
                        <h3>✅ Thank You!</h3>
                        <p>Your enquiry has been submitted successfully.</p>
                        <p>Our team will contact you shortly.</p>
                    </div>
                `;
            }, 500);
        });
    }
});