# CSC 376 - Assignment 3: Client-Server Hangman Game

### Course: CSC 376 – Computer Networking  
### Term: Spring 2025  
### Student: Umme Athiya  
### Email: uummeath@depaul.edu  
### Language: Python 3  
### Due Date: May 14, 2025  

---

## 🔍 Overview

This project implements a classic **Hangman** game using **socket programming** in **Python** with a **Client-Server model** over **TCP**. It is fully text-based and designed to support multiple clients via multithreading on the server side.

---

## 📁 Files Included

- `depaul_UMME-server.py` — Python server program
- `depaul_UMME-client.py` — Python client program
- `words.txt` — Word list used by the server
- `writeup.pdf` — Answers to theoretical questions (Part 3)
- `screenshots/` — Folder containing deployment and execution screenshots
- `README.md` — This documentation file

---

## ⚙️ How to Run

### Server (on local machine or VM):
```bash
python depaul_UMME-server.py words.txt 8080
