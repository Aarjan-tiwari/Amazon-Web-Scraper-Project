#!/usr/bin/env python3
"""
Amazon Web Scraper - Standalone Python Script
A tool to monitor Amazon product prices and store data in CSV format.
"""

import csv
import datetime
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

class AmazonScraper:
    def __init__(self, url, csv_filename='AmazonWebScraperDataset.csv'):
        """
        Initialize the Amazon scraper.
        
        Args:
            url (str): Amazon product URL to monitor
            csv_filename (str): Name of the CSV file to store data
        """
        self.url = url
        self.csv_filename = csv_filename
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
            "Accept-Encoding": "gzip, deflate",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "DNT": "1",
            "Connection": "close",
            "Upgrade-Insecure-Requests": "1"
        }
        
        # Create CSV file if it doesn't exist
        if not os.path.exists(self.csv_filename):
            self.create_csv_file()
    
    def create_csv_file(self):
        """Create the initial CSV file with headers."""
        header = ['title', 'price', 'date']
        with open(self.csv_filename, 'w', newline='', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
        print(f"Created new CSV file: {self.csv_filename}")
    
    def scrape_product(self):
        """
        Scrape product information from Amazon.
        
        Returns:
            tuple: (title, price, date) or (None, None, None) if failed
        """
        try:
            # Make request to Amazon
            page = requests.get(self.url, headers=self.headers, timeout=10)
            page.raise_for_status()
            
            # Parse HTML
            soup = BeautifulSoup(page.content, "html.parser")
            
            # Extract title
            title_element = soup.find(id='productTitle')
            if not title_element:
                print("Warning: Could not find product title")
                return None, None, None
            
            title = title_element.get_text(strip=True)
            
            # Extract price
            price_element = soup.find('span', class_='a-price')
            if price_element:
                price_whole = price_element.find('span', class_='a-price-whole')
                price_fraction = price_element.find('span', class_='a-price-fraction')
                
                if price_whole and price_fraction:
                    price = f"${price_whole.get_text(strip=True)}.{price_fraction.get_text(strip=True)}"
                elif price_whole:
                    price = price_whole.get_text(strip=True)
                else:
                    price = "Price not available"
            else:
                price = "Price not available"
            
            # Clean up price text
            price = price.replace("..", ".")
            if price.startswith('$'):
                price = price[1:]  # Remove $ sign
            
            # Get current date
            today = datetime.date.today()
            
            return title, price, today
            
        except requests.RequestException as e:
            print(f"Request error: {e}")
            return None, None, None
        except Exception as e:
            print(f"Error during scraping: {e}")
            return None, None, None
    
    def save_to_csv(self, title, price, date):
        """
        Save scraped data to CSV file.
        
        Args:
            title (str): Product title
            price (str): Product price
            date (datetime.date): Scraping date
        """
        try:
            data = [title, price, date]
            with open(self.csv_filename, 'a', newline='', encoding='UTF8') as f:
                writer = csv.writer(f)
                writer.writerow(data)
            print(f"Data saved: {title} - ${price} - {date}")
        except Exception as e:
            print(f"Error saving to CSV: {e}")
    
    def check_price(self):
        """
        Main function to check price and save data.
        
        Returns:
            bool: True if successful, False otherwise
        """
        print(f"\nChecking price at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        title, price, date = self.scrape_product()
        
        if title and price and date:
            self.save_to_csv(title, price, date)
            return True
        else:
            print("Failed to scrape product information")
            return False
    
    def run_continuous_monitoring(self, interval_seconds=60):
        """
        Run continuous price monitoring.
        
        Args:
            interval_seconds (int): Time between price checks in seconds
        """
        print(f"Starting continuous monitoring every {interval_seconds} seconds...")
        print("Press Ctrl+C to stop")
        
        try:
            while True:
                self.check_price()
                time.sleep(interval_seconds)
        except KeyboardInterrupt:
            print("\nMonitoring stopped by user")
    
    def display_csv_data(self):
        """Display the current CSV data using pandas."""
        try:
            if os.path.exists(self.csv_filename):
                df = pd.read_csv(self.csv_filename)
                print(f"\nCurrent data in {self.csv_filename}:")
                print(df)
                print(f"\nTotal records: {len(df)}")
            else:
                print(f"CSV file {self.csv_filename} not found")
        except Exception as e:
            print(f"Error reading CSV: {e}")


def main():
    """Main function to run the scraper."""
    # Default Amazon product URL (Data Analyst T-Shirt)
    default_url = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XNL&th=1'
    
    print("Amazon Web Scraper")
    print("=" * 50)
    
    # Get user input for URL
    url = input(f"Enter Amazon product URL (press Enter for default): ").strip()
    if not url:
        url = default_url
        print(f"Using default URL: {url}")
    
    # Create scraper instance
    scraper = AmazonScraper(url)
    
    # Display current data
    scraper.display_csv_data()
    
    # Ask user what to do
    print("\nOptions:")
    print("1. Check price once")
    print("2. Run continuous monitoring")
    print("3. Display current data")
    print("4. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            scraper.check_price()
        elif choice == '2':
            interval = input("Enter monitoring interval in seconds (default: 60): ").strip()
            try:
                interval = int(interval) if interval else 60
                scraper.run_continuous_monitoring(interval)
            except ValueError:
                print("Invalid interval, using default 60 seconds")
                scraper.run_continuous_monitoring()
        elif choice == '3':
            scraper.display_csv_data()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")


if __name__ == "__main__":
    main()
