import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Daily Habit",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 DAILY HABIT")
st.subheader("AI Market Analysis Robot")
st.caption("Analyze • Confirm • Manage Risk")

st.divider()

# SIDEBAR
st.sidebar.header("⚙️ Market Settings")

asset = st.sidebar.selectbox(
    "Asset",
    [
        "EUR/USD",
        "GBP/USD",
        "XAU/USD",
        "BTC/USD",
        "Crash 1000",
        "Crash 500",
        "Boom 1000",
        "Boom 500"
    ]
)

higher_tf = st.sidebar.selectbox(
    "Higher Timeframe",
    ["1H", "4H", "15M", "30M"]
)

entry_tf = st.sidebar.selectbox(
    "Entry Timeframe",
    ["1M", "5M", "15M"]
)

# MARKET ANALYSIS
st.header("📊 Market Analysis")

col1, col2 = st.columns(2)

with col1:
    trend = st.selectbox(
        "Market Trend",
        ["Bullish", "Bearish", "Sideways", "Unclear"]
    )

    structure = st.selectbox(
        "Market Structure",
        [
            "Bullish BOS",
            "Bearish BOS",
            "Bullish CHoCH",
            "Bearish CHoCH",
            "Higher High / Higher Low",
            "Lower High / Lower Low",
            "Range",
            "Unclear"
        ]
    )

with col2:
    liquidity = st.selectbox(
        "Liquidity",
        [
            "Sell-side swept",
            "Buy-side swept",
            "Liquidity nearby",
            "No clear sweep"
        ]
    )

    fvg = st.selectbox(
        "Fair Value Gap",
        [
            "Bullish FVG",
            "Bearish FVG",
            "No FVG",
            "Unclear"
        ]
    )

confirmation = st.selectbox(
    "Entry Confirmation",
    [
        "Confirmed",
        "Waiting for confirmation",
        "Rejected",
        "No confirmation"
    ]
)

# PRICE LEVELS
st.header("🎯 Trade Levels")

col1, col2, col3 = st.columns(3)

with col1:
    entry = st.number_input(
        "Entry Price",
        min_value=0.0,
        value=0.0
    )

with col2:
    stop_loss = st.number_input(
        "Stop Loss",
        min_value=0.0,
        value=0.0
    )

with col3:
    take_profit = st.number_input(
        "Take Profit",
        min_value=0.0,
        value=0.0
    )

# ANALYSIS
if st.button("🤖 ANALYZE MARKET", use_container_width=True):

    bullish = 0
    bearish = 0
    reasons = []

    # Trend
    if trend == "Bullish":
        bullish += 3
        reasons.append("The selected trend is bullish.")

    elif trend == "Bearish":
        bearish += 3
        reasons.append("The selected trend is bearish.")

    # Structure
    if structure in [
        "Bullish BOS",
        "Bullish CHoCH",
        "Higher High / Higher Low"
    ]:
        bullish += 3
        reasons.append("Market structure provides bullish evidence.")

    elif structure in [
        "Bearish BOS",
        "Bearish CHoCH",
        "Lower High / Lower Low"
    ]:
        bearish += 3
        reasons.append("Market structure provides bearish evidence.")

    # Liquidity
    if liquidity == "Sell-side swept":
        bullish += 2
        reasons.append("Sell-side liquidity has been swept.")

    elif liquidity == "Buy-side swept":
        bearish += 2
        reasons.append("Buy-side liquidity has been swept.")

    # FVG
    if fvg == "Bullish FVG":
        bullish += 2
        reasons.append("A bullish FVG is present.")

    elif fvg == "Bearish FVG":
        bearish += 2
        reasons.append("A bearish FVG is present.")

    # Decision
    if confirmation != "Confirmed":
        decision = "🟡 WAIT"

    elif bullish >= bearish + 3:
        decision = "🟢 BULLISH SETUP"

    elif bearish >= bullish + 3:
        decision = "🔴 BEARISH SETUP"

    else:
        decision = "🟡 WAIT"

    # Risk/reward
    risk = abs(entry - stop_loss)
    reward = abs(take_profit - entry)

    if risk > 0:
        rr = reward / risk
    else:
        rr = 0

    st.divider()

    st.header("🤖 DAILY HABIT RESULT")

    st.subheader(decision)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Bullish Score", bullish)

    with c2:
        st.metric("Bearish Score", bearish)

    with c3:
        st.metric("Risk / Reward", f"1:{rr:.2f}")

    st.header("🧠 Robot Reasoning")

    for reason in reasons:
        st.write("• " + reason)

    if confirmation != "Confirmed":
        st.warning(
            "Daily Habit recommends WAIT because confirmation "
            "has not been completed."
        )

    if rr >= 2:
        st.success("Risk/reward is at least 1:2.")
    elif rr > 0:
        st.warning("Risk/reward is below 1:2.")
    else:
        st.info(
            "Enter valid Entry, Stop Loss and Take Profit "
            "levels to calculate risk/reward."
        )

    st.header("📋 Analysis")

    data = {
        "Asset": asset,
        "Higher Timeframe": higher_tf,
        "Entry Timeframe": entry_tf,
        "Trend": trend,
        "Structure": structure,
        "Liquidity": liquidity,
        "FVG": fvg,
        "Confirmation": confirmation,
        "Entry": entry,
        "Stop Loss": stop_loss,
        "Take Profit": take_profit,
        "Decision": decision
    }

    st.dataframe(
        pd.DataFrame(
            data.items(),
            columns=["Factor", "Result"]
        ),
        use_container_width=True,
        hide_index=True
    )

st.divider()

st.caption(
    "Daily Habit provides technical analysis assistance. "
    "It does not guarantee profits or future market movement."
)
