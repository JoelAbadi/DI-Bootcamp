# from selenium import webdriver
# from bs4 import BeautifulSoup
# from collections import Counter
# from statistics import mean
# import chromedriver_autoinstaller
# import time

# # Auto-install ChromeDriver
# chromedriver_autoinstaller.install()

# # Start Chrome
# driver = webdriver.Chrome()

# # Open the AccuWeather forecast page
# driver.get("https://www.accuweather.com/en/us/attica/30607/weather-forecast/2139413")

# # Wait for content to load
# time.sleep(5)

# # Parse page source with BeautifulSoup
# soup = BeautifulSoup(driver.page_source, "html.parser")

# # Close browser
# driver.quit()

# # Extract temperatures and conditions
# temps = []
# conditions = []

# for card in soup.select("div.daily-forecast-card"):
#     temp_tag = card.select_one("div.high")
#     cond_tag = card.select_one("div.phrase")

#     if temp_tag and cond_tag:
#         try:
#             temp = int(temp_tag.text.replace("°", "").strip())
#             condition = cond_tag.text.strip()
#             temps.append(temp)
#             conditions.append(condition)
#         except:
#             continue

# # Analyze results
# print("\n🌦 Weather Forecast Analysis:\n")

# if temps:
#     avg_temp = mean(temps)
#     print(f" Average High Temperature: {avg_temp:.1f}°C")
# else:
#     print(" No temperature data found.")

# if conditions:
#     most_common = Counter(conditions).most_common(1)[0][0]
#     print(f"🌤 Most Common Condition: {most_common}")
# else:
#     print(" No condition data found.")
