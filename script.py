import pandas as pd
import json
import numpy as np
from colorama import Fore, Style, Back
import matplotlib.pyplot as plt
from groq import Groq

# -------------------------------
# Configuration
# -------------------------------

# File paths
HISTORICAL_QUIZ_PATH = 'historical-quiz.json'
OUTPUT_CSV_PATH = 'topic_performance_insights.csv'

# Groq API configuration
GROQ_API_KEY = "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"
GROQ_MODEL = "llama-3.3-70b-versatile"

# -------------------------------
# Load Data
# -------------------------------

def load_json(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        print(f"{Fore.GREEN}✔ Loaded data from {file_path}{Style.RESET_ALL}")
        return data
    except Exception as e:
        print(f"{Fore.RED}✘ Error loading data: {e}{Style.RESET_ALL}")
        return {}

historicalquiz_data = load_json(HISTORICAL_QUIZ_PATH)

# -------------------------------
# Process Historical Quiz Data
# -------------------------------

historicalquiz_df = pd.DataFrame(historicalquiz_data)

# Extract topic information and clean data
historicalquiz_df["topic"] = historicalquiz_df["quiz"].apply(
    lambda x: x.get("topic") if isinstance(x, dict) else None
)
historicalquiz_df["accuracy_numeric"] = pd.to_numeric(
    historicalquiz_df["accuracy"].str.rstrip('%'), errors='coerce'
)
historicalquiz_df = historicalquiz_df.dropna(subset=["topic", "score", "accuracy_numeric", "total_questions", "user_id"])

# -------------------------------
# Analysis
# -------------------------------

# Topic Performance Analysis
topic_analysis = (
    historicalquiz_df.groupby("topic")
    .agg(
        average_score=("score", "mean"),
        average_accuracy=("accuracy_numeric", "mean"),
        total_questions=("total_questions", "sum"),
    )
    .reset_index()
)

# Save topic analysis as CSV
topic_analysis.to_csv(OUTPUT_CSV_PATH, index=False)
print(f"{Fore.CYAN}✔ Topic performance analysis saved to {OUTPUT_CSV_PATH}{Style.RESET_ALL}")

# User-Specific Analysis
user_performance = historicalquiz_df.groupby("user_id").agg(
    total_score=("score", "sum"),
    average_accuracy=("accuracy_numeric", "mean"),
    topics_covered=("topic", "nunique"),
    total_questions_attempted=("total_questions", "sum"),
    weak_topic=("topic", lambda x: x.value_counts().idxmin()),
    strong_topic=("topic", lambda x: x.value_counts().idxmax()),
).reset_index()

specific_user_id = user_performance["user_id"].iloc[0]
specific_user_insights = user_performance[user_performance["user_id"] == specific_user_id].iloc[0]

# Extract and convert insights
def convert_to_native(obj):
    if isinstance(obj, (np.integer, int)):
        return int(obj)
    elif isinstance(obj, (np.floating, float)):
        return float(obj)
    elif isinstance(obj, (np.str_, str)):
        return str(obj)
    else:
        return obj

insights = {key: convert_to_native(value) for key, value in specific_user_insights.items()}

# -------------------------------
# Visualization
# -------------------------------

# Bar Chart: Topic Analysis
plt.figure(figsize=(10, 6))
plt.bar(topic_analysis["topic"], topic_analysis["average_score"], color="skyblue")
plt.title("Average Score per Topic", fontsize=16)
plt.xlabel("Topic", fontsize=14)
plt.ylabel("Average Score", fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("/content/average_score_per_topic.png")
plt.show()

# Pie Chart: Topics Covered
topics_counts = historicalquiz_df["topic"].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(topics_counts, labels=topics_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title("Topics Distribution", fontsize=16)
plt.savefig("/content/topics_distribution.png")
plt.show()

# -------------------------------
# Vibrant Summary
# -------------------------------

print("\n" + "=" * 50)
print(f"{Back.BLUE}{Fore.WHITE} User Performance Insights {Style.RESET_ALL}")
print("=" * 50)
print(f"👤 User ID: {Fore.YELLOW}{insights['user_id']}{Style.RESET_ALL}")
print(f"📊 Total Score: {Fore.GREEN}{insights['total_score']}{Style.RESET_ALL}")
print(f"🎯 Average Accuracy: {Fore.CYAN}{insights['average_accuracy']:.2f}%{Style.RESET_ALL}")
print(f"📚 Topics Covered: {Fore.MAGENTA}{insights['topics_covered']}{Style.RESET_ALL}")
print(f"🛠️ Weak Topic: {Fore.RED}{insights['weak_topic']}{Style.RESET_ALL}")
print(f"🏆 Strong Topic: {Fore.GREEN}{insights['strong_topic']}{Style.RESET_ALL}")
print("=" * 50)

# Recommendations
print(f"\n{Back.GREEN}{Fore.BLACK} Recommendations {Style.RESET_ALL}")
print(f"👉 Focus more on: {Fore.RED}{insights['weak_topic']}{Style.RESET_ALL}")
print(f"📝 Practice MCQs with medium difficulty")
print(f"📅 Plan: Strengthen {insights['weak_topic']} by analyzing past mistakes.")

# Persona
print(f"\n{Back.YELLOW}{Fore.BLACK} Persona {Style.RESET_ALL}")
print(f"🎭 Label: {Fore.BLUE}Diligent Learner{Style.RESET_ALL}")
print(f"💪 Strengths: Excels in {Fore.GREEN}{insights['strong_topic']}{Style.RESET_ALL}")
print(f"📉 Weaknesses: Needs improvement in {Fore.RED}{insights['weak_topic']}{Style.RESET_ALL}")

# -------------------------------
# Export Insights and Visuals
# -------------------------------

print("\nExported visualizations to:")
print(f"✔ {Fore.BLUE}/content/average_score_per_topic.png{Style.RESET_ALL}")
print(f"✔ {Fore.BLUE}/content/topics_distribution.png{Style.RESET_ALL}")

# -------------------------------
# End of Script
# -------------------------------
