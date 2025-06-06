import streamlit as st

# שלב 1: בחירת שפה
lang = st.selectbox("Choose language / בחר שפה", ["English", "עברית"])

# שלב 2: בחירת מטבע
currency = st.selectbox("Currency / מטבע", ["₪", "$", "€", "£"])

# שלב 3: מילון טקסטים
translations = {
    "English": {
        "title": "🧾 Tip Calculator",
        "description": "Split your bill easily with friends!",
        "bill": "💵 What was the total bill?",
        "placeholder": "0.00",
        "tip": "💰 What percentage tip would you like to give?",
        "people": "👥 How many people to split the bill?",
        "calculate": "Calculate",
        "result": f"Each person should pay: {currency}{{:.2f}}",
        "error": "Please enter a valid bill amount and number of people."
    },
    "עברית": {
        "title": "🧾 מחשבון טיפ",
        "description": "פצל את החשבון שלך עם חברים בקלות!",
        "bill": "💵 כמה יצא החשבון הכולל?",
        "placeholder": "0.00",
        "tip": "💰 איזה אחוז טיפ תרצה להוסיף?",
        "people": "👥 כמה אנשים מתחלקים בחשבון?",
        "calculate": "חשב",
        "result": f"כל אחד צריך לשלם: {currency}{{:.2f}}",
        "error": "אנא הזן סכום חשבון תקין ומספר אנשים."
    }
}

# שלב 4: קביעת RTL אם עברית
rtl_style = """
    <style>
    div[data-testid="stApp"] {
        direction: RTL;
        text-align: right;
    }
    </style>
""" if lang == "עברית" else ""

st.markdown(rtl_style, unsafe_allow_html=True)

# שלב 5: תרגום לפי השפה שנבחרה
T = translations[lang]

st.title(T["title"])
st.write(T["description"])

bill_input = st.text_input(T["bill"], placeholder=T["placeholder"])

try:
    bill = float(bill_input)
except ValueError:
    bill = 0.0

tip = st.selectbox(T["tip"], [10, 12, 15, 18, 20])
people = st.number_input(T["people"], min_value=1, step=1)

if st.button(T["calculate"]):
    if bill > 0 and people > 0:
        total = bill + (bill * tip / 100)
        per_person = total / people
        st.success(T["result"].format(per_person))
    else:
        st.warning(T["error"])
