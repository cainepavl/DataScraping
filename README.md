# Hacker News Stories Scraper  

This program fetches popular stories from Hacker News (HN) and displays them based on a minimum vote count. It highlights stories with more than 200 votes, making it easy to find trending content.  

## Table of Contents  

- [Features](#features)  
- [Requirements](#requirements)  
- [Installation](#installation)  
- [Usage](#usage)  
- [How It Works](#how-it-works)  
- [License](#license)
- [Contact](#contact) 

## Features  

- Scrapes stories from the Hacker News homepage.  
- Filters stories by vote count (only shows stories with more than 200 votes).  
- Combines stories from the first two pages of Hacker News.  
- Displays each story's title, vote count, and URL.  

## Requirements  

- Python 3.x  
- Requests library  
- BeautifulSoup4 library  

You can install the required libraries using pip:  

``` 
pip3 install requests beautifulsoup4
```
## Installation

1. Clone the repository:

```
git clone https://github.com/cainepavl/hacker-news-scraper.git
```

2. Navigate to the project directory:

```
cd WebScraper
```

## Usage

To run the program, use the following command:

```
python3 news.py
```

## How It Works

- Clear Screen: The program clears the console to provide a cleaner output.
  
- Fetching Stories: It uses the requests library to fetch HTML from Hacker News and BeautifulSoup to parse the HTML.
  
- Extracting Links and Votes: It extracts story titles, URLs, and vote counts from the HTML.

- Filtering Stories: Only stories with more than 200 votes are included in the final output.

- Displaying Results: Finally, it prints the filtered stories, including their title, vote count, and URL.

## License

This project is licensed under the MIT License - see the [LICENSE]() file for details.

## Contact

  