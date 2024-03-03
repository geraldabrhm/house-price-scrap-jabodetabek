import requests
import bs4

headers = {
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
  'Accept-Language':'en-US,en;q=0.5',
  'cookie':'locale=en_US;'
}

def scrape_data(location, sub_district, page):
  scraped_data = []

  _url = f'https://www.rumah123.com/jual/{location}/{sub_district}/rumah/?page={page}'

  url = _url
  r = requests.get(url,headers=headers)
  soup = bs4.BeautifulSoup(r.text,'html.parser')

  for item in soup.find('div',{'class':'ui-search-page__content'}).find_all('div',{'class':'card-featured__middle-section'}):
    title = None
    price = None
    lt = None
    lb = None

    if item.find('h2'):
      title = item.find('h2').text

    if item.find('strong'):
      price = item.find('strong').text

    tipe = item.find('div',{'class':'card-featured__middle-section__header-badge'}).find('div').text.lower()
    if tipe == 'rumah':
      if item.find('div',{'class':'card-featured__middle-section__attribute'}):
        item_attribute = item.find('div',{'class':'card-featured__middle-section__attribute'}).find_all('div',{'class':'attribute-info'})
        if len(item_attribute) > 0:
          lt = item_attribute[0].text.replace(':','')
          if len(item_attribute) > 1:
            lb = item_attribute[1].text.replace(':','')
    
    scraped_data.append({
      'location': location,
      'sub_district': sub_district,
      'title': title,
      'price': price,
      'lt' : lt,
      'lb' : lb
    })

  return scraped_data