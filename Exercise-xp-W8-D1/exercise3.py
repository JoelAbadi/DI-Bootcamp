# from selenium import webdriver
# from bs4 import BeautifulSoup
# import chromedriver_autoinstaller
# import time

# # Automatically install the correct version of ChromeDriver
# chromedriver_autoinstaller.install()

# # Launch Chrome browser
# driver = webdriver.Chrome()

# # Navigate to Rotten Tomatoes - Movies In Theaters
# driver.get("https://www.rottentomatoes.com/browse/movies_in_theaters")

# # Wait for the JavaScript content to load
# time.sleep(5)

# # Get the fully rendered HTML
# soup = BeautifulSoup(driver.page_source, "html.parser")

# # Try to select movie titles
# print("\n Top Movie Titles:\n")
# titles = soup.select("span.p--small")

# if titles:
#     for i, title in enumerate(titles[:10], 1):
#         print(f"{i}. {title.text.strip()}")
# else:
#     print(" Could not find movie titles — the page structure may have changed.")

# # Close the browser
# driver.quit()
