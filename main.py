import scraper
import pandas as pd
import constant

data = []
df = pd.DataFrame(data)

try:
  # Scraping
  for location in constant.LOCATIONS:
    for sub_district in constant.LOCATIONS[location]:
      for i in range(1, 51):
        print(f'Scraping location {location} sub-district {sub_district} page {i} ...')
        scraped_data = pd.DataFrame(scraper.scrape_data(location, sub_district, i))
        df = pd.concat([df, scraped_data])
        if len(scraped_data) == 0:
          break

  # Export to CSV
  print("Exporting to CSV")
  df.to_csv('rumah123_jabodetabek.csv', index=False)
except Exception as e:
  print(e)