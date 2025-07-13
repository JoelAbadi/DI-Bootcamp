import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Fetch the GitHub Topics page
url = "https://github.com/topics"
response = requests.get(url)
print("Status code:", response.status_code)

# Step 2: Parse HTML
soup = BeautifulSoup(response.text, 'html.parser')
topic_cards = soup.select('div.py-4.border-bottom.d-flex.flex-justify-between')

print("Number of topics found:", len(topic_cards))

# Step 3: Extract info
topic_titles = []
topic_descriptions = []
topic_urls = []

for card in topic_cards:
    title_tag = card.select_one('p.f3.lh-condensed')
    desc_tag = card.select_one('p.color-fg-muted')
    link_tag = card.select_one('a')

    if title_tag and desc_tag and link_tag:
        title = title_tag.text.strip()
        description = desc_tag.text.strip()
        url = f"https://github.com{link_tag['href']}"

        topic_titles.append(title)
        topic_descriptions.append(description)
        topic_urls.append(url)

# Step 4: Create DataFrame and save
df = pd.DataFrame({
    'Topic': topic_titles,
    'Description': topic_descriptions,
    'URL': topic_urls
})

print(df.head())
df.to_csv('github_topics.csv', index=False)
print("✅ CSV file saved as github_topics.csv")

# Optional: install seaborn if not done
# pip install seaborn

import seaborn as sns
import matplotlib.pyplot as plt

# Select first 10 topics (or any metric you want)
top_topics = df.head(10)

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(x=top_topics['Topic'], y=top_topics['Description'].str.len())
plt.xticks(rotation=45)
plt.title('Length of Topic Descriptions (Top 10 Topics)')
plt.xlabel('Topic')
plt.ylabel('Description Length')
plt.tight_layout()

plt.savefig("topic_bar_chart.png")  # Save the chart first
plt.show()  # Then display the chart


