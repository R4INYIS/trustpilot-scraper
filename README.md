## ⭐ Trustpilot Review Scraper

This project is a bot designed to scrape public reviews from Trustpilot for a certain company. It uses an undetected Chrome driver to avoid bot detection and extracts review titles, descriptions, ratings, review dates, and experience dates from multiple pages. All the collected data is saved to a CSV file for analysis or record-keeping.

---

### 📦 Features

* Stealthy scraping using `undetected-chromedriver`.
* Navigates through all review pages.
* Extracts review title, text, star rating, date of experience, and review date.
* Simulates scrolling behavior to mimic human interaction.
* Saves all reviews to a UTF-8 encoded CSV file.

---

### ✅ Requirements

* Python 3.8+
* Google Chrome
* Chromedriver (auto-handled by `undetected-chromedriver`)

#### Python Libraries

Install the required libraries using:

```bash
pip install beautifulsoup4 undetected-chromedriver
```

---

### ⚙️ Setup

1. **Clone the repository:**

```bash
git clone https://github.com/R4INYIS/trustpilot-scraper/
cd trustpilot-scraper
```

2. **Review the configuration:**

Update the `URL` and `TOTAL_PAGES` in `main.py` if you want to scrape a different Trustpilot profile or adjust the number of pages.

---

### ▶️ How to Run

To start the scraper, simply run:

```bash
python main.py
```

The script will:

* Open a stealth Chrome browser
* Loop through all Trustpilot review pages
* Extract review data from each page
* Store it into a CSV file named `"website"_trustpilot.csv`

---

### 📝 Notes

* The scraper uses randomized scrolling to simulate real user behavior.
* Intended for personal, educational, or analytical use—please respect Trustpilot’s terms of service.
* Some reviews may be skipped if data is incomplete or loading fails.
