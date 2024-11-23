import requests
from bs4 import BeautifulSoup
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_hn_stories(url):
  res = requests.get(url)
  soup = BeautifulSoup(res.text, 'html.parser')
  links = soup.select('.titleline > a')
  subtext = soup.select('.subtext')
  return links, subtext

def create_custom_hn(links, subtext):
  hn = []
  for idx, item in enumerate(links):
    title = item.getText()
    href = item.get('href', None)
    vote = subtext[idx].select('.score')
    if len(vote):
      points = int(vote[0].getText().replace(' points', ''))
      if points > 200:
        hn.append(f"{title}  ({points})  {href}")
  return sorted(hn, reverse=True)

# Fetch stories from both pages
links1, subtext1 = get_hn_stories('https://news.ycombinator.com/news')
links2, subtext2 = get_hn_stories('https://news.ycombinator.com/news?p=2')

# Combine stories and filter by votes
all_stories = create_custom_hn(links1 + links2, subtext1 + subtext2)

# Clear the screen before printing the first entry
clear_screen()

# Print each story on a separate line with a blank line in between
for story in all_stories:
  print(story)
  print()