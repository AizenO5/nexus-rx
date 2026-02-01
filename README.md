# NexusRx: The Silent Guardian of the Pharmacy

### *A High-Stakes Agentic AI Marketplace*

---

## 🎭 The Pitch: "The Prescription Paradox"

**The Scene:** London. 11:43 PM. A flickering neon sign outside a chemist. 

You hold a scrap of paper—a prescription—worth more than your monthly rent. You open an app. You upload the photo. You wait. 

Suddenly, your telephone rings. An unknown number. A cold voice on the other end starts interrogating you. *“Why do you need this? What is your ailment?”* You feel like a suspect in your own life. You look at the price: **£320.00**. You know the shop around the corner sells it for **£240.00**, but they don’t have an app. You’re trapped. And if you buy it and your doctor changes the dose tomorrow? **No returns. No refunds. Case closed.**

**The Antagonist:** A digital monopoly that treats patients like barcodes and logistics like an afterthought.

**Enter: NexusRx.** We have engineered a programme not just to deliver, but to **think**. NexusRx deploys a triple-threat of AI Agents—The Hunter, The Verifier, and The Inspector—to dismantle the grey markets and return power to the patient. We don't just find your medicine; we orchestrate a masterpiece of pharmaceutical transparency.

---

## 🛠️ The Architecture (The Blueprint)

NexusRx is a modular, Multi-Agent system designed for clinical precision and hyper-local efficiency.

### 1. The Price-Hunter Agent (Status: Operational)
* **The Mission:** To scan the digital horizon. It scrapes the behemoths (1mg, Amazon) and cross-references them with our secret weapon: **The Local Inventory Database.**
* **The Result:** Users find the 25% "offline-only" discount that the giants want to keep hidden.

### 2. The Verification Agent (Status: In Development)
* **The Mission:** To silence the tele-callers. Using high-fidelity OCR and Medical NLP, it validates prescriptions in milliseconds.
* **The Result:** It identifies banned substances and expiry dates instantly, firing off notifications instead of intrusive phone calls.

### 3. The Integrity Agent (Status: Classified)
* **The Mission:** To solve the "Non-Returnable" deadlock. Using Computer Vision, it inspects a 10-second video of your medicine. 
* **The Result:** It detects broken seals or tampered foil. If the medicine is pristine, the return is authorised. The £320 mistake is no longer a life sentence.

---

## 🚀 Technical Setup (The Briefing)

To deploy NexusRx into your local environment, follow these instructions to the letter.

### I. Prerequisites
* **Python 3.10+** (The backbone of our operation)
* **Tesseract OCR** (For the Verifier's vision)
* **A Google Gemini API Key** (The 'Brain' of the agents)

### II. Initialisation
1. **Project Structure:**
    NexusRx/
    ├── app.py              # The Main Entry Point (Streamlit UI)
    ├── agents/             # Folder containing Agent Logic
    │   ├── __init__.py
    │   ├── price_agent.py  # Level 1: Price-Hunter Agent
    │   ├── verify_agent.py # Level 2: Verification Agent
    │   └── integrity_agent.py # Level 3: Integrity Agent
    ├── data/               # Folder for Dummy Data
    │   ├── local_inventory.csv
    │   └── banned_drugs.json
    ├── utils/              # Helper functions (OCR, Scraping, etc.)
    │   ├── scraper.py
    │   └── vision_helper.py
    ├── requirements.txt    # List of libraries to install
    └── README.md           # Your Pitch & Setup Instructions
2. **Clone the Intelligence:**
   ```bash
   git clone [https://github.com/your-username/NexusRx.git](https://github.com/your-username/NexusRx.git)
   cd NexusRx