# 🤖 WhatsApp Gemini AI Chatbot

A production-ready Flask application that connects the **Meta WhatsApp Business Cloud API** with **Gemini AI (Google’s generative AI)** to create a smart WhatsApp chatbot that responds intelligently to user messages.

---

## 📚 Table of Contents

1. [🌐 Meta Developer Setup](#1-🌐-meta-developer-setup)
2. [🔐 WhatsApp API Setup](#2-🔐-whatsapp-api-setup)
3. [📁 Project Configuration](#3-📁-project-configuration)
4. [📦 Installation & Running the App](#4-📦-installation--running-the-app)
5. [🧪 Testing the Bot](#5-🧪-testing-the-bot)
6. [🛠️ Tech Stack](#6-🛠️-tech-stack)
7. [📂 Project Structure](#7-📂-project-structure)
8. [📌 Notes & Troubleshooting](#8-📌-notes--troubleshooting)

---

## 1. 🌐 Meta Developer Setup

### Step 1: Create a Facebook Developer Account

* Go to [https://developers.facebook.com](https://developers.facebook.com)
* Log in with your Facebook account.
* Navigate to **My Apps → Create App**
* Choose **"Business"** as the app type.
* Give your app a name, email, and click **Create App**.

---

## 2. 🔐 WhatsApp API Setup

### Step 1: Add WhatsApp Product to App

* In your app dashboard, select **+ Add Product**.
* Find **WhatsApp**, and click **Set Up**.

### Step 2: Generate Required Credentials

Go to the **WhatsApp > Getting Started** section and note:

| Item                   | Where to find it                            |
| ---------------------- | ------------------------------------------- |
| `Access Token`         | "Temporary access token" from the dashboard |
| `Phone Number ID`      | Directly visible on the dashboard           |
| `WhatsApp Business ID` | At the top of the WhatsApp Settings         |
| `From Number`          | Sandbox or business number                  |
| `Recipient Number`     | Your registered phone number with opt-in    |

> ⚠️ Access token is short-lived unless you configure long-lived tokens.

---

## 3. 📁 Project Configuration

### Step 1: Clone and Set Up Environment

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
cp .env.example .env
```

### Step 2: Fill in `.env`

```
ACCESS_TOKEN=your_whatsapp_access_token
PHONE_NUMBER_ID=your_whatsapp_phone_number_id
GEMINI_API_KEY=your_google_gemini_api_key
VERIFY_TOKEN=verify_me_abc123
MAX_WHATSAPP_TEXT_LENGTH
```

---

## 4. 📦 Installation & Running the App

### Step 1: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### requirements.txt

```txt
Flask
requests
google-genai
python-dotenv
```

### Step 3: Start Flask App

```bash
python app.py
```

---

## 5. 🧪 Testing the Bot

### 1. Start Ngrok to expose Flask

```bash
ngrok http 8000
```

### 2. Copy the HTTPS URL (e.g., `https://xxxx.ngrok-free.app`)

### 3. Set Webhook in Meta Developer Console

* Navigate to **WhatsApp > Configuration**
* Set Callback URL: `https://xxxx.ngrok-free.app/webhook`
* Set Verify Token: `verify_me_abc123`

### 4. Subscribe to `messages` under Webhook fields.

### 5. Send a message (e.g., "hi") to your WhatsApp number.

---

## 6. 🛠️ Tech Stack

| Component       | Stack                           |
| --------------- | ------------------------------- |
| Backend         | Flask (Python)                  |
| Messaging API   | WhatsApp Business Cloud API     |
| AI Response     | Gemini 2.5 (via `google-genai`) |
| Env Handling    | `python-dotenv`                 |
| Hosting/Testing | Ngrok (for webhook tunneling)   |

---

## 7. 📂 Project Structure

```
whatsapp-gemini-chatbot/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env.example           # Sample environment config
├── README.md              # You're reading this!
```

---

## 8. 📌 Notes & Troubleshooting

* **Token expired?** Go to Meta > WhatsApp > Tools to regenerate.
* **Webhook not receiving messages?**

  * Ensure your Ngrok tunnel is running.
  * Ensure the correct fields (`messages`) are subscribed.
* **400 Error on reply?** WhatsApp limits messages to **4096 characters**. The app truncates longer messages automatically.

---

## 📫 Questions?

Feel free to open an issue or reach out on LinkedIn if you're stuck. Happy hacking! ✨

---

Would you like a logo + badge setup or deployment option (like Render or Railway) added too?
