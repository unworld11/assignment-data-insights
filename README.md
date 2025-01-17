# README: Historical Quiz Data Analysis

## Overview
This script processes historical quiz data to analyze topic performance and user-specific insights. It uses libraries like `pandas`, `numpy`, `matplotlib`, and `colorama` to generate meaningful insights and visualizations, providing recommendations for improvement.

## Features
1. **Data Loading:** Loads historical quiz data from a JSON file.
2. **Data Cleaning:** Cleans and processes the data, including handling missing values.
3. **Analysis:**
   - Topic performance analysis.
   - User-specific insights, including weak and strong topics.
4. **Visualizations:**
   - Bar chart for average score per topic.
   - Pie chart for topic distribution.
5. **Vibrant Summary:** Displays user performance insights, recommendations, and a persona label.
6. **Export:** Saves analysis results and visualizations as CSV and PNG files.

## Requirements

### Python Packages
- `pandas`
- `json`
- `numpy`
- `colorama`
- `matplotlib`
- `groq`

Install dependencies using:
```bash
pip install pandas numpy colorama matplotlib
```

### API Configuration
The script uses the Groq API for enhanced analysis. Replace the placeholder `GROQ_API_KEY` and `GROQ_MODEL` with your credentials and model choice.

## File Structure
- `historical-quiz.json`: Input JSON file containing historical quiz data.
- `topic_performance_insights.csv`: Output CSV file with topic analysis results.
- `average_score_per_topic.png`: Bar chart visualization of topic scores.
- `topics_distribution.png`: Pie chart visualization of topic distribution.

## How to Run
1. **Prepare Data:** Ensure the `historical-quiz.json` file is in the specified path.
2. **Update Configurations:**
   - Update `HISTORICAL_QUIZ_PATH` with the path to your input JSON file.
   - Update `OUTPUT_CSV_PATH` with the desired output CSV path.
3. **Run Script:** Execute the script using:
   ```bash
   python script_name.py
   ```

## Outputs
1. **CSV File:**
   - File: `topic_performance_insights.csv`
   - Content: Contains average score, accuracy, and total questions per topic.
2. **Visualizations:**
   - Bar chart: Average score per topic (`average_score_per_topic.png`).
   - Pie chart: Topic distribution (`topics_distribution.png`).
3. **Summary:** Printed summary of user insights, recommendations, and persona.

## Key Insights
- **Average Score per Topic:** Highlights topics where users perform well or need improvement.
- **User-Specific Insights:** Provides strengths, weaknesses, and areas for improvement for a specific user.

## Recommendations for Improvement
- Focus on weak topics and analyze past mistakes.
- Practice medium-difficulty MCQs to build confidence.
- Strengthen weak areas by reviewing relevant materials and attempting quizzes.

## Notes
- The script handles missing data by dropping rows with null values for critical columns.
- Ensure that the `historical-quiz.json` file has the required fields: `quiz`, `accuracy`, `score`, `total_questions`, and `user_id`.

## Customization
- Modify `specific_user_id` to analyze insights for a different user.
- Adjust visualization styles or save paths as per requirements.

## Contact
For any questions or support, please contact the script author or contribute to the project by submitting a pull request.

