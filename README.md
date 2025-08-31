# Amazon Web Scraper Project

A Python-based web scraping tool that monitors Amazon product prices and stores the data in a CSV file for analysis and tracking purposes.

## 🎯 Project Overview

This project is an automated Amazon price monitoring system that:
- Scrapes product information (title, price, date) from Amazon product pages
- Stores data in a CSV file for historical tracking
- Runs continuously to monitor price changes over time
- Uses web scraping techniques with proper headers to avoid detection

## ✨ Features

- **Real-time Price Monitoring**: Continuously tracks product prices at configurable intervals
- **Data Extraction**: Extracts product title, price, and current date
- **CSV Data Storage**: Automatically saves scraped data to a CSV file
- **Anti-Detection**: Uses realistic browser headers to avoid being blocked
- **Automated Operation**: Runs in a loop with configurable sleep intervals
- **Data Analysis Ready**: CSV output can be easily imported into pandas for analysis

## 🛠️ Technologies Used

- **Python 3.11+**
- **BeautifulSoup4** - HTML parsing and data extraction
- **Requests** - HTTP requests to Amazon
- **Pandas** - Data manipulation and analysis
- **CSV** - Data storage and export
- **Datetime** - Date tracking and timestamps

## 📋 Prerequisites

Before running this project, make sure you have:

- Python 3.11 or higher installed
- pip (Python package installer)
- Internet connection to access Amazon
- Basic understanding of Python programming

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Amazon-Web-Scraper-Project.git
cd Amazon-Web-Scraper-Project
```

### 2. Install Required Dependencies

```bash
pip install -r requirements.txt
```

Or install packages individually:

```bash
pip install beautifulsoup4
pip install requests
pip install pandas
pip install lxml
```

### 3. Verify Installation

```bash
python -c "import bs4, requests, pandas; print('All packages installed successfully!')"
```

## 📖 Usage

### Basic Usage

1. **Open the Jupyter Notebook**:
   ```bash
   jupyter notebook "Amazon Web Scraper Dataset final.ipynb"
   ```

2. **Run Individual Cells**:
   - Cell 1: Imports libraries and sets up basic scraping
   - Cell 2: Extracts and cleans product data
   - Cell 3: Gets current date
   - Cell 4: Creates initial CSV file
   - Cell 5: Reads and displays CSV data
   - Cell 6: Appends new data to CSV
   - Cell 7: Defines the main scraping function
   - Cell 8: Runs continuous monitoring loop

### Continuous Monitoring

To run the scraper continuously:

```python
while(True):
    check_price()
    time.sleep(5)  # Wait 5 seconds between checks
```

**Note**: Press `Ctrl+C` to stop the continuous monitoring.

### Customization

#### Change Target Product

Update the `URL` variable in the code:

```python
URL = 'https://www.amazon.com/your-product-url-here'
```

#### Modify Monitoring Interval

Change the sleep duration in the monitoring loop:

```python
time.sleep(60)  # Check every minute instead of 5 seconds
```

#### Add More Data Fields

Extend the CSV structure by modifying the header and data arrays:

```python
header = ['title', 'price', 'date', 'rating', 'availability']
data = [title, price, today, rating, availability]
```

## 📊 Data Output

The scraper generates a CSV file (`AmazonWebScraperDataset.csv`) with the following structure:

| Column | Description | Example |
|--------|-------------|---------|
| `title` | Product title | "Funny Got Data MIS Data Systems Business Analyst T-Shirt" |
| `price` | Product price | "16.99" |
| `date` | Scraping date | "2024-08-03" |

## 🔧 Configuration

### Headers Configuration

The scraper uses realistic browser headers to avoid detection:

```python
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "DNT": "1",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1"
}
```

### File Paths

- **Input**: Amazon product URL (configurable)
- **Output**: `AmazonWebScraperDataset.csv` (in project directory)

## ⚠️ Important Notes

### Legal Considerations

- **Respect robots.txt**: Check Amazon's robots.txt file before scraping
- **Rate Limiting**: Use reasonable delays between requests (5+ seconds recommended)
- **Terms of Service**: Ensure compliance with Amazon's terms of service
- **Personal Use Only**: This tool is for educational and personal use

### Technical Limitations

- **HTML Structure Changes**: Amazon may change their HTML structure, breaking the scraper
- **IP Blocking**: Excessive requests may result in temporary IP blocking
- **CAPTCHA**: May encounter CAPTCHA challenges with high-frequency requests

## 🐛 Troubleshooting

### Common Issues

1. **"Price not available" error**:
   - Product may be out of stock
   - HTML structure may have changed
   - Check if the product page is accessible

2. **CSV file not created**:
   - Ensure write permissions in the directory
   - Check if the file path is correct

3. **Connection errors**:
   - Verify internet connection
   - Check if Amazon is accessible
   - Consider using a VPN if IP is blocked

### Debug Mode

Add print statements to debug issues:

```python
def check_price():
    try:
        # ... existing code ...
        print(f"Successfully scraped: {title} - {price}")
    except Exception as e:
        print(f"Error occurred: {e}")
```

## 📈 Data Analysis

### Using Pandas for Analysis

```python
import pandas as pd

# Load the data
df = pd.read_csv('AmazonWebScraperDataset.csv')

# Basic statistics
print(df.describe())

# Price trend analysis
df['date'] = pd.to_datetime(df['date'])
df['price'] = pd.to_numeric(df['price'])

# Plot price over time
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['price'])
plt.title('Product Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚖️ Disclaimer

This project is for educational purposes only. Users are responsible for ensuring compliance with:
- Amazon's Terms of Service
- Applicable laws and regulations
- Website robots.txt files
- Rate limiting policies

The developers are not responsible for any misuse of this tool.

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Search existing GitHub issues
3. Create a new issue with detailed information
4. Include error messages and system information

## 🔮 Future Enhancements

Potential improvements for future versions:

- [ ] Email notifications for price drops
- [ ] Multiple product monitoring
- [ ] Price history visualization
- [ ] Database storage instead of CSV
- [ ] Web interface for configuration
- [ ] Price drop alerts
- [ ] Historical price analysis
- [ ] Export to different formats (JSON, Excel)

## 📚 Learning Resources

- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/)
- [Requests Documentation](https://requests.readthedocs.io/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Web Scraping Best Practices](https://www.scraperapi.com/blog/web-scraping-best-practices/)

---

**Happy Scraping! 🕷️📊**
