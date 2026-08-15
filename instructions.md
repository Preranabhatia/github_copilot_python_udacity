# 🧩 Modern Sudoku Web Application — Project Guidelines

> **Project Overview:** A fully responsive Sudoku web application built with **Python Flask** and **Vanilla JavaScript**. It features unique-solution puzzle generation, live tracking, hints, theme toggling, and client-side leaderboard persistence.

---

## 🛠️ Tech Stack & Environment
* **Backend:** Python 3 & Flask
* **Frontend:** HTML5, CSS3 (with CSS Variables), Vanilla JavaScript
* **Data Persistence:** Browser `localStorage` (No server-side database required)
* **Dependencies:** Keep external dependencies to an absolute minimum.

---

## 📁 Project Architecture
* `app.py` — Flask application routing and server-side coordination.
* `sudoku_logic.py` — Core puzzle generation, validation, and backtracking engine.
* `templates/` — HTML template files.
* `static/` — CSS stylesheets and client-side JavaScript assets.
* `instructions.md` — Reference configuration guide for development.

---

## 📐 Coding Conventions
* **Naming Standards:** Use `snake_case` for Python variables/functions and `camelCase` for JavaScript.
* **Modularity:** Keep functions small, focused on a single responsibility, and avoid code duplication.
* **Error Handling:** Gracefully catch exceptions and provide useful, clear feedback to the user.
* **Code Clarity:** Add comments sparingly—only where they explain non-obvious logic.

---

## 🎲 Sudoku Rules & Generation Engine
* **Grid Layout:** Standard 9x9 grid broken into nine 3x3 sub-grids.
* **Core Constraints:** Rows, columns, and 3x3 boxes must contain numbers 1–9 without duplicates. Empty cells are represented internally as `0`.
* **Puzzle Uniqueness:** 
  * Generated puzzles must have *at least one valid solution* and **exactly one unique solution**.
  * Use robust backtracking algorithms for generation and validation.
* **Prefilled Cells:** Initial puzzle cells must be locked and non-editable by the user.
* **Difficulty Scaling:** Support **Easy**, **Medium**, and **Hard** levels by altering the number of prefilled clues while preserving uniqueness.

---

## ⚡ Game Features & Functionality
* **Dynamic Interaction:** Immediate validation of user input with real-time conflict/error highlighting.
* **Assistance Tools:** 
  * Live solving timer.
  * Hint system with a hint counter and unique cell styling.
  * "Check Puzzle" option to verify current user entries against the solution.
* **Completion & Leaderboard:** 
  * Detects puzzle completion and triggers a congratulatory modal/message.
  * Prompts for the player's name and saves the **Top 10 scores** in `localStorage` (sorted by fastest time).
  * Score records include: *Player Name, Completion Time, Hints Used,* and *Difficulty Level*.

---

## 🎨 UI/UX & Theme Requirements
* **Visual Grid Structure:** Clear 3x3 box borders with visually distinct alternating background colors for odd/even sub-grids.
* **Responsiveness:** Flawless scaling across desktop, tablet, and mobile screens without layout shifts.
* **Dark & Light Mode:** 
  * Implemented using CSS variables.
  * Affects the entire application and remains persistent across page reloads via `localStorage`.
  * Guarantees high contrast and accessibility for values and error feedback.

---

## 🛑 Guardrails (What NOT To Do)
* ❌ Do not remove or break existing working functionality.
* ❌ Do not introduce jQuery, heavy frontend frameworks, or unnecessary libraries.
* ❌ Do not use global mutable state for data belonging to an individual game instance.
* ❌ Do not hard-code a single static Sudoku puzzle.
* ❌ Do not claim a puzzle is unique without verifying it through algorithmic validation.
* ❌ Do not permit modification of prefilled cells.
* ❌ Do not store sensitive personal data.