from ai.fetch_data import get_insights
from ai.prompt_builder import make_prompt
from ai.llm import ai_insights
from ai.give_insights import save_insight

def run_ai_pipeline():
    crypto = get_insights()
    prompt = make_prompt(crypto)
    insight = ai_insights(prompt)
    save_insight(insight)
    return insight

if __name__ == "__main__":
    
    print(run_ai_pipeline())
