import os
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
from dotenv import load_dotenv
import json
import streamlit as st

# --- CONFIGURATION & SETUP ---
# Load environment variables for local testing.
# On Railway, these will be loaded from the "Variables" tab automatically.
load_dotenv()

# Initialize OpenAI Client
# We use st.secrets for secure cloud deployment, falling back to os.getenv for local
try:
    api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
except:
    api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("❌ OpenAI API Key is missing. Please set it in .env or Streamlit secrets.")
    st.stop()

client = OpenAI(api_key=api_key)

# --- BACKEND FUNCTIONS (The Logic) ---
# These are the exact same functions from before, just moved here.

def get_raw_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        # Increased timeout to 30 seconds for slower websites
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return response.text
    except requests.exceptions.Timeout:
        st.error(f"⏱️ Request timed out. The website took too long to respond. Try again or check if the website is accessible.")
        return None
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching URL: {e}")
        return None

def extract_element_text(html, selector):
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.select(selector)
    if elements:
        # Join all found text in case the price is split across multiple tags
        return " ".join([el.get_text(strip=True) for el in elements])
    return None

def ai_clean_price(raw_text):
    prompt = f"""
    I have scraped a price string from a website. It is formatted messily: "{raw_text}".
    
    Please extract:
    1. The numeric value (float).
    2. The currency code (USD, GBP, EUR,Rs,INR,LKR, etc).
    3. A confidence score (0-100) indicating how sure you are this is a price.
    
    Return ONLY a valid JSON object. Do not add markdown formatting.
    Example output: {{"price": 49.99, "currency": "GBP", "confidence": 95}}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a data extraction assistant that outputs only JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )
        content = response.choices[0].message.content.strip()
        if content.startswith("```json"):
            content = content.replace("```json", "").replace("```", "")
        return json.loads(content)
    except Exception as e:
        st.error(f"AI Error: {e}")
        return None

# --- FRONTEND (The UI) ---

st.set_page_config(page_title="AI Price Tracker", page_icon="🤖")

st.title("🤖 AI-Powered Competitor Price Tracker")
st.write("Enter a product URL and a CSS selector to grab its price, even if the formatting is messy.")

# Input Form
with st.form("scrape_form"):
    col1, col2 = st.columns(2)
    with col1:
        url_input = st.text_input("Product URL", value="[http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html](http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html)")
    with col2:
        selector_input = st.text_input("CSS Selector for Price", value=".price_color")
    
    submitted = st.form_submit_button("🚀 Run Tracker")

# Logic handles submitting the form
if submitted:
    if not url_input or not selector_input:
        st.warning("Please provide both a URL and a CSS Selector.")
    else:
        with st.spinner("Fetching HTML..."):
            html = get_raw_html(url_input)
        
        if html:
            with st.spinner("Extracting raw text..."):
                raw_text = extract_element_text(html, selector_input)
            
            if raw_text:
                st.success(f"Found Raw Text: **{raw_text}**")
                
                with st.spinner("🤖 AI is cleaning and structuring the data..."):
                    clean_data = ai_clean_price(raw_text)
                
                if clean_data:
                    st.subheader("✅ Final Structured Data")
                    
                    # Display metrics visually
                    m1, m2, m3 = st.columns(3)
                    m1.metric("Price", clean_data.get("price", "N/A"))
                    m2.metric("Currency", clean_data.get("currency", "N/A"))
                    m3.metric("AI Confidence", f"{clean_data.get('confidence', 0)}%")
                    
                    # Show the raw JSON below
                    with st.expander("View Raw JSON Output"):
                        st.json(clean_data)
            else:
                st.error(f"Could not find any text using selector: `{selector_input}`. Please check the page source.")