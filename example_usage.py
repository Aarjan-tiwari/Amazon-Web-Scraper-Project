#!/usr/bin/env python3
"""
Example usage of the Amazon Web Scraper
This script demonstrates basic functionality of the scraper.
"""

from amazon_scraper import AmazonScraper

def example_basic_usage():
    """Example of basic scraper usage."""
    print("=== Basic Usage Example ===")
    
    # Amazon product URL (Data Analyst T-Shirt)
    url = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XNL&th=1'
    
    # Create scraper instance
    scraper = AmazonScraper(url, 'example_output.csv')
    
    # Check price once
    print("\n1. Checking price once...")
    success = scraper.check_price()
    
    if success:
        print("✓ Price check successful!")
    else:
        print("✗ Price check failed!")
    
    # Display data
    print("\n2. Displaying current data...")
    scraper.display_csv_data()

def example_custom_monitoring():
    """Example of custom monitoring setup."""
    print("\n=== Custom Monitoring Example ===")
    
    # Custom Amazon product URL (you can change this)
    custom_url = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XNL&th=1'
    
    # Create scraper with custom CSV filename
    scraper = AmazonScraper(custom_url, 'custom_monitoring.csv')
    
    print("Custom monitoring setup complete!")
    print("You can now use scraper.run_continuous_monitoring(interval_seconds) to start monitoring")
    print("Example: scraper.run_continuous_monitoring(300)  # Check every 5 minutes")

def example_data_analysis():
    """Example of basic data analysis."""
    print("\n=== Data Analysis Example ===")
    
    try:
        import pandas as pd
        
        # Read the CSV data
        df = pd.read_csv('AmazonWebScraperDataset.csv')
        
        print("Data loaded successfully!")
        print(f"Total records: {len(df)}")
        print(f"Date range: {df['date'].min()} to {df['date'].max()}")
        
        # Convert price to numeric for analysis
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
        
        # Basic statistics
        print(f"\nPrice statistics:")
        print(f"Average price: ${df['price'].mean():.2f}")
        print(f"Lowest price: ${df['price'].min():.2f}")
        print(f"Highest price: ${df['price'].max():.2f}")
        
        # Price changes
        if len(df) > 1:
            price_changes = df['price'].diff().dropna()
            print(f"\nPrice changes detected: {len(price_changes[price_changes != 0])}")
            
            if len(price_changes[price_changes != 0]) > 0:
                print("Price change history:")
                for i, change in enumerate(price_changes):
                    if change != 0:
                        print(f"  Record {i+1}: ${change:+.2f} change")
        
    except FileNotFoundError:
        print("CSV file not found. Run the scraper first to generate data.")
    except Exception as e:
        print(f"Error during analysis: {e}")

if __name__ == "__main__":
    print("Amazon Web Scraper - Example Usage")
    print("=" * 50)
    
    # Run examples
    example_basic_usage()
    example_custom_monitoring()
    example_data_analysis()
    
    print("\n" + "=" * 50)
    print("Examples completed!")
    print("Check the generated CSV files for scraped data.")
    print("Use the main amazon_scraper.py script for interactive usage.")
