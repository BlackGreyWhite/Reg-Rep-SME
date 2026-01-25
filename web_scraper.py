"""
Web scraping utilities for extracting content from websites
Supports both static HTML and dynamic JavaScript sites
"""

import os
import time
import hashlib
from urllib.parse import urljoin, urlparse
from typing import List, Dict, Optional
import requests
from bs4 import BeautifulSoup
import html2text
from playwright.sync_api import sync_playwright
from config import get_logger

logger = get_logger(__name__)

class WebScraper:
    """Scrapes content from websites with smart static/dynamic detection"""
    
    def __init__(self, delay: int = 2, user_agent: str = None):
        self.delay = delay
        self.user_agent = user_agent or os.getenv("WEB_USER_AGENT", "RAG-Bot/1.0")
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": self.user_agent})
        self.html_converter = html2text.HTML2Text()
        self.html_converter.ignore_links = False
        self.html_converter.ignore_images = True
        
    def is_allowed_by_robots(self, url: str) -> bool:
        """Check if URL is allowed by robots.txt"""
        try:
            parsed = urlparse(url)
            robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
            
            response = self.session.get(robots_url, timeout=5)
            if response.status_code == 200:
                if "Disallow: /" in response.text:
                    logger.warning(f"Site may disallow scraping: {url}")
                    return False
            return True
        except:
            return True
    
    def scrape_static(self, url: str) -> Optional[Dict]:
        """Scrape static HTML content"""
        try:
            logger.info(f"Scraping (static): {url}")
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'lxml')
            
            # Remove unwanted elements
            for element in soup(['script', 'style', 'nav', 'footer', 'header']):
                element.decompose()
            
            # Extract title
            title = soup.find('title')
            title_text = title.get_text().strip() if title else url
            
            # Extract main content
            main_content = (
                soup.find('main') or 
                soup.find('article') or 
                soup.find('div', class_='content') or
                soup.find('body')
            )
            
            if not main_content:
                logger.warning(f"No main content found: {url}")
                return None
            
            # Convert to markdown
            html_content = str(main_content)
            text_content = self.html_converter.handle(html_content)
            
            # Clean up excessive whitespace
            text_content = '\n'.join(line.strip() for line in text_content.split('\n') if line.strip())
            
            if len(text_content) < 100:
                logger.warning(f"Content too short: {url}")
                return None
            
            return {
                'url': url,
                'title': title_text,
                'content': text_content,
                'method': 'static',
                'success': True
            }
            
        except Exception as e:
            logger.error(f"Static scraping failed for {url}: {e}")
            return None
    
    def scrape_dynamic(self, url: str) -> Optional[Dict]:
        """Scrape dynamic content using browser automation"""
        try:
            logger.info(f"Scraping (dynamic): {url}")
            
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page(user_agent=self.user_agent)
                
                # Navigate and wait for content
                page.goto(url, wait_until='networkidle')
                page.wait_for_timeout(2000)
                
                # Get title
                title = page.title()
                
                # Remove unwanted elements
                page.evaluate("""
                    () => {
                        document.querySelectorAll('script, style, nav, footer, header').forEach(el => el.remove());
                    }
                """)
                
                # Get main content
                content = page.evaluate("""
                    () => {
                        const main = document.querySelector('main') || 
                                   document.querySelector('article') ||
                                   document.querySelector('.content') ||
                                   document.body;
                        return main ? main.innerText : '';
                    }
                """)
                
                browser.close()
                
                if len(content) < 100:
                    logger.warning(f"Content too short: {url}")
                    return None
                
                return {
                    'url': url,
                    'title': title,
                    'content': content,
                    'method': 'dynamic',
                    'success': True
                }
                
        except Exception as e:
            logger.error(f"Dynamic scraping failed for {url}: {e}")
            return None
    
    def scrape_url(self, url: str, prefer_static: bool = True) -> Optional[Dict]:
        """Scrape a URL, trying static first then falling back to dynamic"""
        # Check robots.txt
        if not self.is_allowed_by_robots(url):
            logger.warning(f"Skipping (robots.txt): {url}")
            return None
        
        # Rate limiting
        time.sleep(self.delay)
        
        if prefer_static:
            result = self.scrape_static(url)
            if result and result['success']:
                return result
            
            logger.info(f"Falling back to dynamic scraping: {url}")
            return self.scrape_dynamic(url)
        else:
            return self.scrape_dynamic(url)
    
    def scrape_site(self, base_url: str, max_pages: int = 50, follow_links: bool = False) -> List[Dict]:
        """Scrape multiple pages from a site"""
        results = []
        visited = set()
        to_visit = [base_url]
        
        while to_visit and len(results) < max_pages:
            url = to_visit.pop(0)
            
            if url in visited:
                continue
            
            visited.add(url)
            result = self.scrape_url(url)
            
            if result and result['success']:
                results.append(result)
                logger.info(f"✓ Scraped {len(results)}/{max_pages}: {url}")
                
                if follow_links and len(results) < max_pages:
                    try:
                        response = self.session.get(url, timeout=10)
                        soup = BeautifulSoup(response.content, 'lxml')
                        
                        for link in soup.find_all('a', href=True):
                            next_url = urljoin(url, link['href'])
                            if urlparse(next_url).netloc == urlparse(base_url).netloc:
                                if next_url not in visited and next_url not in to_visit:
                                    to_visit.append(next_url)
                    except:
                        pass
        
        logger.info(f"Scraped {len(results)} pages from {base_url}")
        return results


def load_website_sources(filepath: str = "website_sources.txt") -> List[str]:
    """Load website URLs from file"""
    if not os.path.exists(filepath):
        logger.warning(f"Website sources file not found: {filepath}")
        return []
    
    urls = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                urls.append(line)
    
    logger.info(f"Loaded {len(urls)} website sources")
    return urls


def scrape_all_sources(sources_file: str = "website_sources.txt", max_pages_per_site: int = 50) -> List[Dict]:
    """Scrape all websites from sources file"""
    urls = load_website_sources(sources_file)
    
    if not urls:
        logger.warning("No website sources to scrape")
        return []
    
    scraper = WebScraper(
        delay=int(os.getenv("WEB_SCRAPE_DELAY", 2)),
        user_agent=os.getenv("WEB_USER_AGENT")
    )
    
    all_results = []
    
    for url in urls:
        logger.info(f"\n{'='*80}")
        logger.info(f"Processing website: {url}")
        logger.info(f"{'='*80}")
        
        # Check if it's a single page or site to crawl
        if url.endswith('/') or 'docs' in url or 'documentation' in url:
            results = scraper.scrape_site(url, max_pages=max_pages_per_site, follow_links=True)
        else:
            result = scraper.scrape_url(url)
            results = [result] if result else []
        
        all_results.extend(results)
        logger.info(f"Collected {len(results)} pages from this source")
    
    logger.info(f"\n{'='*80}")
    logger.info(f"Total pages scraped: {len(all_results)}")
    logger.info(f"{'='*80}\n")
    
    return all_results


if __name__ == "__main__":
    results = scrape_all_sources()
    print(f"\nScraped {len(results)} pages")
    for i, result in enumerate(results[:5], 1):
        print(f"{i}. {result['title'][:60]}... ({result['method']})")