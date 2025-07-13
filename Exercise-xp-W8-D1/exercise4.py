# from selenium import webdriver
# from bs4 import BeautifulSoup
# from collections import defaultdict
# from datetime import datetime
# import chromedriver_autoinstaller
# import time

# # Automatically install ChromeDriver
# chromedriver_autoinstaller.install()

# # Launch browser
# driver = webdriver.Chrome()

# # Go to BBC Innovation Technology page
# driver.get("https://www.bbc.com/innovation/technology")

# # Wait for content to fully load
# time.sleep(5)

# # Parse HTML after JavaScript has rendered it
# soup = BeautifulSoup(driver.page_source, "html.parser")

# # Close the browser
# driver.quit()

# # Extract articles
# articles = []
# for article in soup.find_all("a", href=True):
#     title = article.get_text(strip=True)
#     parent = article.find_parent("div")
#     date_tag = parent.find("time") if parent else None

#     if date_tag and date_tag.has_attr("datetime"):
#         date_str = date_tag["datetime"]
#         try:
#             pub_date = datetime.strptime(date_str[:10], "%Y-%m-%d")
#             articles.append((title, pub_date))
#         except:
#             continue

# # Group by month
# grouped_by_month = defaultdict(list)
# for title, date in articles:
#     month = date.strftime("%B")
#     grouped_by_month[month].append(title)

# # Print results
# print("\n BBC Innovation Articles Grouped by Month:\n")
# if grouped_by_month:
#     for month, titles in grouped_by_month.items():
#         print(f"{month}:")
#         for t in titles:
#             print(f" - {t}")
#         print()
# else:
#     print(" No articles with valid dates were found.")
