<div align="center">

```
 █████╗ ████████╗███╗   ███╗
██╔══██╗╚══██╔══╝████╗ ████║
███████║   ██║   ██╔████╔██║
██╔══██║   ██║   ██║╚██╔╝██║
██║  ██║   ██║   ██║ ╚═╝ ██║
╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝
  S I M U L A T I O N
```

**A command-line ATM banking experience built with Python**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-22c55e?style=for-the-badge)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-f59e0b?style=for-the-badge)](CONTRIBUTING.md)

</div>

---

## 📸 Preview

```
╔══════════════════════════════════╗
║     🏧  WELCOME TO ATM MENU     ║
╠══════════════════════════════════╣
║  [1]  💰  Display Balance        ║
║  [2]  📥  Deposit Money          ║
║  [3]  📤  Withdraw Money         ║
║  [4]  📋  Statement / History    ║
║  [5]  🚪  Exit ATM               ║
╚══════════════════════════════════╝
          Enter choice: _
```

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| 💰 **Check Balance** | View your real-time account balance |
| 📥 **Deposit** | Add funds to your account instantly |
| 📤 **Withdraw** | Safely withdraw with balance protection |
| 📋 **Statement** | Full transaction history at a glance |
| 🛡️ **Validation** | Robust input handling — no crashes |

---

## 📁 Project Structure

```
ATM-Simulation/
│
├── 🚀 main.py               ← Entry point & menu loop
├── 🗄️  utils.py              ← Shared in-memory state
├── 💰 display_balance.py    ← Balance viewer
├── 📥 deposit_balance.py    ← Deposit handler
├── 📤 withdraw_balance.py   ← Withdrawal handler
└── 📋 Statement_balance.py  ← Transaction summary
```

---

## ⚡ Quick Start

### 1 · Clone the repo

```bash
git clone https://github.com/BOT9315/ATM-Simulation.git
cd ATM-Simulation
```

### 2 · Run (no dependencies needed!)

```bash
python main.py
```

> **Requirements:** Python 3.x — that's it. No pip installs, no virtual environments.

---

## 🎮 How to Use

Once the program starts, navigate with number keys:

```
Enter choice: 2
→ Enter amount to deposit into your account: 500
→ ✅ Deposit successful in your account.

Enter choice: 1
→ Current balance of your account: 500.0

Enter choice: 3
→ Enter amount to withdraw from your account: 200
→ ✅ Withdrawal successful from your account.

Enter choice: 4
─────────────────────────────
  Account Statement/History
─────────────────────────────
  Total Deposited  :  500.0
  Total Withdrawn  :  200.0
  Current Balance  :  300.0
─────────────────────────────
```

---

## 🏗️ Architecture

```
main.py  ──imports──▶  display_balance.py
    │    ──imports──▶  deposit_balance.py
    │    ──imports──▶  withdraw_balance.py
    │    ──imports──▶  Statement_balance.py
    │
    └── all modules ──read/write──▶  utils.py
                                      ├── deposits[]
                                      ├── withdrawals[]
                                      └── balance_history[]
```

State is shared via `utils.py` — a lightweight in-memory store that all modules import.

---

## 📌 Notes & Limitations

> ⚠️ **No persistence** — All data resets when the program exits. Each session starts fresh.

> 💱 **No currency unit** — Amounts are plain floats. Treat them as your preferred currency.

> 👤 **Single user** — No login/PIN system. One session, one virtual account.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. **Fork** the project
2. **Create** your feature branch (`git checkout -b feature/PinAuthentication`)
3. **Commit** your changes (`git commit -m 'Add PIN authentication'`)
4. **Push** to the branch (`git push origin feature/PinAuthentication`)
5. **Open** a Pull Request

### 💡 Ideas for improvements

- [ ] PIN/password login system
- [ ] Persistent storage with JSON or SQLite
- [ ] Multiple user accounts
- [ ] Currency formatting (₹, $, £)
- [ ] Individual transaction logs with timestamps

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

---

<div align="center">

Made with ❤️ and Python

⭐ **Star this repo if you found it helpful!** ⭐

</div>
