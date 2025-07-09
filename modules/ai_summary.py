from groq import Groq

def summarize_trends(insights):
    client = Groq(api_key=("GROQ_API_KEY"))


    prompt = f"""
You are an expert airline industry analyst. Analyze this flight search data and extract key trends:

1. Top 2 most searched flight routes and possible reasons (e.g., tourism, business, seasonal demand).
2. Whether flight demand is increasing, decreasing, or stable in recent days.
3. Weekly or monthly demand trends or seasonality.
4. Actionable recommendations for airline booking managers and planners.

--- ROUTE DATA ---
{insights['popular_routes'].to_string(index=False)}

--- SEARCH TRENDS (Last 5 days) ---
{insights['price_trends'].tail(5).to_string(index=False)}
"""

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful data analyst."},
                {"role": "user", "content": prompt}
            ],
            model="llama3-70b-8192" 
        )

        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"Failed to generate summary:\n\n{e}"
