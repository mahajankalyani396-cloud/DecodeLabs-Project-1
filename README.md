# DecodeLabs-Project-1
# Project 1: Rule-Based AI Chatbot
**Batch:** 2026 | Powered by DecodeLabs

## Overview
This repository contains the foundation phase of the Artificial Intelligence Engineering track at DecodeLabs. Before constructing systems that rely on probabilistic deep learning, this project demonstrates absolute control over deterministic logic, control flow, and input sanitization.

## Key Features
* **IPO Model Architecture:** Implements a strict Input-Process-Output design flow.
* **Input Sanitization:** Uses explicit string normalization methods (`.lower().strip()`) to process raw user feeds cleanly before logical matching.
* **Deterministic Guardrails:** Operates entirely as a "White Box" model with 100% hard-coded rules, eliminating hallucination risks.
* **Continuous Execution Loop:** Runs infinitely until a specific exit command (`exit` or `bye`) is captured.

## How To Run
Ensure you have Python 3.x installed, then run the script via your terminal:
```bash
python chatbot.py
