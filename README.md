# 🤖 Facebook Content Poster Bot (Python + Pyppeteer)

## 🧠 Overview
The **Facebook Content Poster Bot** is a complete **Python-based automation system** that automatically posts your **text and image content** directly to **Facebook** — without manual typing or clicking.  

It reads your **content details (text and image paths)** from a simple **CSV file**, logs in using your **saved Chrome profile**, and posts everything just like a human user would.  

This project was developed by **Ezee Kits**, and it’s designed for **creators, marketers, and developers** who want to automate daily or bulk Facebook content posting safely and efficiently.

It runs on **Windows**, **Linux**, or **Android (Termux)** using **Pyppeteer**, a headless Chrome automation library for Python.

---

## ⚡ Features
- ✅ Fully automated posting on **Facebook web** (desktop version)
- 🖼️ Supports both **text posts** and **image uploads**
- 🔄 Reads data from a **CSV file** (content + image path)
- 👤 Uses **real Chrome profiles** for persistent login (no need to log in again)
- 🧠 Uses **Pyppeteer with stealth configuration** to avoid bot detection
- 📱 Compatible with **Android (via Termux)**, **Windows**, and **Linux**
- 📊 Easily extendable to **Facebook pages**, **groups**, or **multiple accounts**
- 🧩 Clean, modular code with reusable functions (from `func.py`)
- 🧮 Optional **delay configuration** for human-like interaction
- 💾 Automatically saves your data logs for reference

---
Facebook-Content-Poster/
│
├── facebook.py # Main bot logic (handles posting text + images)
├── posting.py # Entry point script (launches browser + starts bot)
├── func.py # Reusable automation helper functions
├── posts.csv # User CSV file (contains text and image paths)
└── README.md # Documentation (this file)



---

## 🧩 How It Works

1. Reads your **content details** (text and image path) from a CSV file.
2. Launches **Chrome** (or Chromium) using your saved **user profile**.
3. Opens **Facebook Web**.
4. Locates the “What’s on your mind?” input field.
5. Uploads your image(s) automatically.
6. Pastes your text content using clipboard simulation.
7. Clicks the **Post** button.
8. Logs completion and moves to the next content (if added).

---

## 🧮 Example CSV Format

Save your content details in a CSV file (`posts.csv`) like this:

| text_content | image_path |
|---------------|-------------|
| “Good morning everyone! 🌞” | `C:\Users\HP\Pictures\morning.jpg` |
| “Our new product launch 🚀 is here!” | `C:\Users\HP\Pictures\launch.png` |

Each row represents one post. The bot will automatically process each one.

---

## ⚙️ Setup Guide (Windows, Linux, or Android)

### 🪟 Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/Facebook-Content-Poster.git
cd Facebook-Content-Poster

🧩 Step 2: Install Dependencies

Make sure you have Python 3.9+ installed.
Then install the required libraries:

pip install pyppeteer pandas bs4 lxml pyperclip asyncio
💻 Step 3: Chrome Setup
You must use your existing Chrome profile to keep your login session active.
This means you don’t need to log in every time.

Go to Chrome → Settings → Manage Profiles

Copy your profile path. For example:

sql
Copy code
C:\Users\HP\AppData\Local\Google\Chrome\User Data\Profile 1
Paste that path inside posting.py:

python
Copy code
'userDataDir': r"C:\Users\HP\Desktop\ChromeProfileClone"
This ensures the bot uses your saved session.

🧠 Step 4: Set Your Post Data
Edit facebook.py to set your image and text manually or provide a posts.csv file.
Example:

python
Copy code
img = r'C:\Users\HP\Pictures\front cover.PNG'   # Path to image
text_content = """
#### WRITE YOUR CONTENT/TEXT HERE
"""
You can automate multiple posts by looping through CSV rows.

▶️ Step 5: Run the Script
bash
Copy code
python posting.py
It will:

Launch Chrome

Go to Facebook

Wait for login (if needed)

Start posting automatically

🧱 Code Architecture
1️⃣ facebook.py
Handles all Facebook automation logic:

Opens the posting dialog

Uploads image(s)

Pastes text

Clicks the “Post” button

2️⃣ func.py
Contains reusable functions such as:

css_click_center() → Clicks element using CSS selector

xpath_click_center() → Clicks element using XPath

saving_files() → Saves logs and combines CSV data

drop_duplicate() → Removes duplicate rows in CSV

create_dir() → Creates directories safely

delet_dir_cont() → Deletes all contents in a folder

3️⃣ posting.py
Launches the browser

Loads your saved Chrome profile

Navigates to Facebook

Calls the main bot function (Facebook_Bot)

Closes browser when done

🧠 Example Post Flow
csharp
Copy code
[1] Opening Facebook...
[2] Logged in successfully.
[3] Clicking "What's on your mind..."
[4] Uploading image: C:\Users\HP\Pictures\front cover.PNG
[5] Typing post content...
[6] Clicking "Post" button...
[7] ✅ Post uploaded successfully!
The bot mimics human-like delays using asyncio.sleep() and randomized pauses.



| Component             | Description                                     |
| --------------------- | ----------------------------------------------- |
| **Language**          | Python 3.9+                                     |
| **Automation Engine** | Pyppeteer                                       |
| **Libraries Used**    | asyncio, pandas, pyperclip, lxml, bs4, requests |
| **Browser**           | Chrome / Chromium                               |
| **Data Format**       | CSV                                             |
| **Environment**       | Works on Windows, Linux, or Android (Termux)    |


## 🧰 Folder Structure

📱 Android (Termux) Usage

You can also run this project on Android using Termux.

pkg update && pkg upgrade -y
pkg install python git chromium -y
pip install pyppeteer pandas bs4 lxml pyperclip
git clone https://github.com/yourusername/Facebook-Content-Poster.git
cd Facebook-Content-Poster
python posting.py


Use a Chromium-compatible user data folder for Facebook login persistence.

💾 Output and Logs

All posts are saved and tracked automatically (if you extend with saving_files()).
You can create daily logs like:

Date,Time,Content,Image,Status
2025-11-05,15:00,"Good morning everyone!","morning.jpg","Posted"

🧩 Expandable Ideas

You can easily extend this bot to:

Post on Facebook Pages

Post in Groups

Schedule posts at specific times

Read content from Google Sheets instead of CSV

Integrate with other social platforms (Twitter, Instagram, TikTok)

🎥 Full Video Tutorial

A complete step-by-step setup and demo video will be available on:
👉 Ezee Kits YouTube Channel

Subscribe, Like, and Comment ❤️ to support more automation projects.

👨‍💻 Author

Ezee Kits (PETER)
🎓 Electrical & Electronics Engineer | 🇳🇬 Nigeria
💡 Passionate about Automation, Bots, and AI-driven Systems
📧 Email: ezeekits@gmail.com

📺 YouTube: Ezee Kits

📜 License

MIT License

This project is open-source for educational and automation learning purposes.
You can modify and distribute it with proper credit to the author.


Automate Facebook posting using Python and Pyppeteer. Supports text + image uploads, reads from CSV, and works on Windows, Linux, or Android (Termux). Developed by Ezee Kits.
