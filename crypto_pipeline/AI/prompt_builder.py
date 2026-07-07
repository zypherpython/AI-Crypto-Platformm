from ai.fetch_data import get_insights

def make_prompt(crypto):
    prompt = f"""
        You are a crypto market analyst. You are in the interview. Your whole life depends on it. You need to crack this and the HR asks:

        Analyze the following data and give a short 2–3 sentence insight:

        Coin: {crypto['coin']}
        Price: {crypto['price']}
        Market Cap: {crypto['market_cap']}
        Volume: {crypto['volume']}
        Volatility: {crypto['volatility']}
        Risk: {crypto['risk']}
        Timestamp: {crypto['timestamp']}

        Focus on trend interpretation and risk insight.
        """

    return prompt

