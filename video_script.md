# AI-Powered Price Tracker - Video Demonstration Script

## Introduction (0:00 - 0:30)
"Hey everyone! Today I'm going to show you an AI-Powered Competitor Price Tracker that I built. This tool helps you automatically extract and clean up product prices from any website, even when the formatting is messy or inconsistent.

The app uses web scraping combined with AI to intelligently parse price information, making it perfect for competitor analysis, price monitoring, or any scenario where you need to track prices across different websites."

---

## What Makes It Special (0:30 - 1:00)
"What makes this tool unique is its AI-powered cleaning feature. Traditional scrapers often fail when prices are formatted inconsistently - like 'Rs. 1,299.99' or '$49.99 USD' or even split across multiple HTML elements. 

Our AI model understands context and can extract:
- The numeric price value
- The currency code (supporting USD, GBP, EUR, Rs, INR, LKR, and more)
- A confidence score showing how certain it is about the extraction

This means you get clean, structured data every time, regardless of how messy the source formatting is."

---

## Live Demonstration (1:00 - 3:30)

### Step 1: Opening the App
"Let me open the app. As you can see, we have a clean, simple interface with two input fields."

### Step 2: Entering the URL
"First, I'll paste the product URL I want to track. For this demo, let's use a product from surplus.lk - a popular e-commerce site. [Paste URL]"

### Step 3: Finding the CSS Selector
"Now, I need to find the CSS selector for the price element. I'll right-click on the price in the browser, inspect the element, and copy the CSS selector. This tells the scraper exactly where to look for the price on the page. [Show selector, e.g., '.price' or '#product-price']"

### Step 4: Running the Tracker
"Perfect! Now I'll click 'Run Tracker' and watch the magic happen."

### Step 5: The Process
"As you can see, the app goes through three stages:
1. **Fetching HTML** - It downloads the webpage content
2. **Extracting raw text** - It finds the price element using our CSS selector
3. **AI Cleaning** - The AI model processes the messy text and structures it"

### Step 6: Results
"Excellent! Here are the results:
- **Price**: 12,999.99
- **Currency**: LKR (Sri Lankan Rupees)
- **AI Confidence**: 95%

The app successfully extracted the price even though it might have been formatted with currency symbols, commas, or other text. Below, you can see the raw JSON output if you want to use this data programmatically."

---

## Advanced Features (3:30 - 4:00)
"Let me show you a few more things:

**Multiple Currency Support**: The AI recognizes various currency formats - from USD and GBP to regional currencies like LKR and INR.

**Confidence Scoring**: The confidence score helps you identify when the extraction might need manual verification. A score above 90% is typically very reliable.

**Error Handling**: If a website is slow or unreachable, the app gracefully handles timeouts and provides clear error messages."

---

## Use Cases (4:00 - 4:30)
"This tool is perfect for:
- **E-commerce businesses** tracking competitor prices
- **Price monitoring** for specific products over time
- **Market research** comparing prices across different platforms
- **Automated reporting** where you need structured price data

The structured JSON output makes it easy to integrate with databases, spreadsheets, or other automation tools."

---

## Closing (4:30 - 5:00)
"That's a quick walkthrough of the AI-Powered Price Tracker! The combination of web scraping and AI makes price extraction reliable and flexible, even when dealing with inconsistent website formats.

If you have any questions or want to see it work with a different website, let me know in the comments. Thanks for watching!"

---

## Tips for Recording:
- **Screen Recording**: Show the browser with the product page, then switch to the Streamlit app
- **Inspect Element**: Demonstrate how to find CSS selectors using browser DevTools
- **Multiple Examples**: Consider showing 2-3 different websites to demonstrate versatility
- **Highlight Features**: Use cursor highlights or annotations to point out key UI elements
- **Error Handling**: Optionally show what happens with an invalid selector or URL
- **Speed**: You can speed up the "spinner" sections in post-production if needed


