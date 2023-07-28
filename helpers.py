""" Collection of helper functions """

def clean_leadership(soup):
    """clean soup object of leadership news article page"""
    main = soup.find_all("div", class_="content-inner")
    cleaned = main[0].get_text()
    return cleaned

def clean_punch_or_sun(soup):
    """clean soup object of punch news article page"""
    main = soup.find_all("div", class_="post-content")
    cleaned = main[0].get_text()
    return cleaned

def clean_pmnews(soup):
    """clean soup object of pmnews news article page"""
    main = soup.find_all("div", class_="article-content")
    cleaned = main[0].get_text()
    return cleaned

def clean_dailytrust(soup):
    """clean soup object of pmnews news article page"""
    main = soup.find_all("article", class_="article__body")
    cleaned = main[0].get_text()
    return cleaned

def clean_thisday(soup):
    """clean soup object of pmnews news article page"""
    main = soup.find_all("div", class_="article-content")
    cleaned = main[0].get_text()
    return cleaned