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
    keys: ["product", "products", "platform", "phisaegis", "endpoint", "identity", "vulnerability"],
    text: "UcyAegis is a products, platform & services company. Our first product, PhisAegis, is launching soon — real-time phishing and email threat defense, running on the UcyAegis Platform: one console, one detection engine, built to host every product we ship next. Share what you're trying to protect and we can point you to the right fit."
  },

  {
    keys: ["service", "services", "vapt", "pentest", "penetration", "retainer", "maintenance", "audit"],
    text: "UcyAegis offers hands-on security services: Website Security Audit, Website Security Maintenance (Monthly), Web Application VAPT, Incident Response, and Security Retainers. Each is delivered by senior practitioners with a clear scope and evidence-backed report. Tell us what you need protected and we'll recommend the right service."
  },

  {
    keys: ["training", "certification", "course", "learn", "student"],
    text: "UcyAegis offers professional cybersecurity training and certification programs for students, working professionals, and corporate teams. Popular tracks include Cyber Security Foundations, SOC Analyst Training, Ethical Hacking, Cloud Security, Governance Risk & Compliance (GRC), and Security Leadership Programs, all with hands-on labs and practical projects. Ask for syllabus, duration, certification details, or upcoming batches."
  },

  {
    keys: ["price", "cost", "pricing", "fees", "budget"],
    text: "Pricing depends on whether you need a product, a service engagement, or training — plus scope, number of seats or mailboxes, and batch size. We provide customized quotations to make sure you get the most cost-effective fit. Please submit your requirements through the Contact page and our team will prepare a tailored proposal."
  },

  {
    keys: ["incident", "breach", "hacked", "ransomware", "urgent"],
    text: "If your organization is currently experiencing a cyber incident, ransomware attack, unauthorized access, data breach, or suspicious activity, immediate action is critical. Isolate affected systems where possible, preserve logs and evidence, avoid deleting files, and refrain from making major system changes until the situation is assessed. Contact UcyAegis immediately for urgent guidance — our Incident Response service is built for exactly this."
  },

  {
    keys: ["contact", "email", "phone", "call", "demo"],
    text: "You can reach UcyAegis through the Contact page for PhisAegis early access, a platform demo, a service request, training inquiries, partnership opportunities, or career-related discussions. Please include your name, organization, email address, and a brief description of your requirement so our team can respond efficiently."
  },

  {
    keys: ["compliance", "iso", "gdpr", "soc2"],
    text: "The UcyAegis Platform is built to make compliance evidence easier to produce — clear, executive-ready reporting across every product, mapped toward frameworks such as ISO 27001, SOC 2, GDPR, PCI DSS, and HIPAA. Our services team can also help with audit-readiness work directly. Share your compliance goals and we will point you to the right fit."
  },

  {
    keys: ["career", "job", "internship", "hiring"],
    text: "Interested in joining UcyAegis? We regularly look for product engineers, cybersecurity professionals, interns, researchers, trainers, and security analysts. Please submit your resume and area of interest through the Contact page or Careers section for future opportunities."
  },

  {
    keys: ["awareness", "employee", "phishing"],
    text: "Human error remains one of the biggest cybersecurity risks. PhisAegis includes integrated employee awareness signals alongside real-time phishing detection, so your team gets protection and better instincts at the same time."
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
        <div class="ganga-message bot">Hi, I am Ganga AI. I can help with PhisAegis, the UcyAegis Platform, our security services, training, pricing, and urgent incident guidance.</div>
        <div class="ganga-chips">
          <button class="ganga-chip" type="button" data-question="I want product details">Products</button>
          <button class="ganga-chip" type="button" data-question="I need a security service">Services</button>
          <button class="ganga-chip" type="button" data-question="Tell me about training and certification">Training</button>
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
    return "I can help with PhisAegis, the UcyAegis Platform, our security services, training, certifications, incidents, and contact guidance. Please share a little more detail, or use the Contact page for a direct enquiry.";
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

