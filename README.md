# 💳 AAVE Wallet Credit Scoring System

Welcome! This project builds a **credit score model (0–1000)** for wallets interacting with the **AAVE V2 DeFi Protocol**, based on historical transaction behavior like deposits, borrows, repayments, and liquidations.

> 🧠 Purpose: Detect reliable vs risky DeFi users  
> 🛠️ Tools: Python, Pandas, Matplotlib, Scikit-learn  
> 📊 Output: Score CSV + Histogram of wallet behavior

---

## 📂 Project Overview

aave_credit_score/
├── user-wallet-transactions.json # ⛔ Raw input data (not on GitHub)
├── wallet_credit_score.py # ✅ Main script for scoring
├── wallet_scores.csv # ✅ Output credit scores
├── score_distribution.png # ✅ Wallet score histogram
└── README.md # 📘 Project documentation

---

## 🚀 Quick Start

### 🔹 Step 1: Setup Environment (Optional)

```bash
python -m venv venv
venv\Scripts\activate
```

### 🔹Step 2: Install Dependencies

```bash
pip install pandas matplotlib seaborn scikit-learn
```

### 🔹Step3: Run the Script
python wallet_credit_score.py
📝 Output:
i.wallet_scores.csv → Wallet addresses with credit scores
ii.score_distribution.png → Histogram of credit scores

### ⚙️ Credit Score Logic
| 🧠 Feature              | 📘 Description                         | 🎯 Impact   |
| ----------------------- | -------------------------------------- | ----------- |
| `num_deposit`           | How many times user deposited          | 📈 Positive |
| `num_repay`             | How many times user repaid             | 📈 Positive |
| `avg_amount`            | Average USD value per transaction      | 📈 Positive |
| `active_days`           | Number of days user was active         | 📈 Positive |
| `borrow_to_repay_ratio` | Borrow vs Repay ratio (lower = better) | 📉 Negative |
| `liquidation_ratio`     | Ratio of liquidation calls             | 📉 Negative |


### 💡 Final score is scaled between 0 and 1000, higher is better.

### 📸 Output Preview
This script automatically creates:
<img width="1280" height="216" alt="Screenshot 2025-07-16 143643" src="https://github.com/user-attachments/assets/2749b285-a53e-48e5-b0d0-3a4f411aeec4" />

<img width="1292" height="180" alt="Screenshot 2025-07-16 143657" src="https://github.com/user-attachments/assets/4bdf144c-a595-4a24-9997-43c4a7c8a50b" />


✅ wallet_scores.csv — Wallet addresses with scores

📊 score_distribution.png — Credit score histogram

<img width="1274" height="705" alt="Screenshot 2025-07-16 143626" src="https://github.com/user-attachments/assets/b0b44b3b-d00e-402f-9c99-1e0146bbc0a0" />

💬 Terminal output logs for progress & debugging

📷 You can view screenshots attached in the repo.

### 📊 Score Range Breakdown

Score Range     | Description
----------------|-----------------------------
800 - 1000      | 🟢 Highly trusted wallets
600 - 800       | 🟡 Responsible users
400 - 600       | ⚠️  Average behavior
200 - 400       | 🔴 Risk-prone or new users
0 - 200         | 🚨 Suspicious or bot-like

### 🌟 Future Possibilities
📊 Interactive dashboard with Streamlit

🔄 Real-time wallet tracking using APIs

🧠 ML-based clustering for anomaly detection

🔗 Extend to other protocols like Compound/Uniswap

---

### 👨‍💻 Author

**Achyut Shiel**  
📎 GitHub: [@achyutshiel](https://github.com/achyutshiel)  
📁 Repository: [aave-credit-score](https://github.com/achyutshiel/aave-credit-score)


#### ⚠️ Notes

- `user-wallet-transactions.json` is ~87MB and **not uploaded to GitHub**
- Please place the file manually inside your project folder before running the script
- 📁 Download JSON file here: [Google Drive Link](https://drive.google.com/file/d/1ISFbAXxadMrt7Zl96rmzzZmEKZnyW7FS/view?usp=sharing)
- Optionally, use a compressed version or host it via your own cloud storage


⭐ If you like this project, don’t forget to give it a Star!

