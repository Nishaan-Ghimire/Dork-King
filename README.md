# Dork-King 🕵️‍♂️

Dork-King is an automated dorking tool designed to help security researchers and bug bounty hunters find potentially sensitive files, misconfigurations, and vulnerable endpoints on web domains. By leveraging Google dorking techniques, the tool automates crafting and executing search queries, then presents the findings in a clean, Bootstrap-powered HTML report.

## Features 🚀
- **Automated Google Dorking:** Quickly generate dork queries for a target domain.  
- **Pre-configured Payloads:** Dork payloads include common file leaks, exposed credentials, database dumps, error logs, and more.  
- **HTML Report Generation:** All findings are presented in an easy-to-navigate Bootstrap-based HTML page with clickable search links.  
- **Targeted Vulnerability Categories:** Includes queries for subdomains, login pages, SQL errors, backup files, open redirects, and more.  

---

## Example Dork Payloads 🔍
Some of the automated search payloads include:
- **Exposed Configuration Files:**  
  ```
  site:targetdomain.com ext:xml | ext:conf | inurl:.env
  ```
- **Database Files:**  
  ```
  site:targetdomain.com ext:sql | ext:mdb
  ```
- **Directory Listing:**  
  ```
  site:targetdomain.com intitle:index.of
  ```
- **Open Redirect Vulnerabilities:**  
  ```
  site:targetdomain.com inurl:redirect | inurl:url
  ```

---

## Installation & Usage ⚙️  
### Prerequisites  
- **Python 3**  
- Required Libraries: Install dependencies using:  
  ```bash
  pip install requests beautifulsoup4
  ```

### How to Run:
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/dork-king.git  
   cd dork-king  
   ```
2. Run the script with a target domain:  
   ```bash
   python3 dorkking.py example.com  
   ```
3. After completion, an HTML file will be generated in the same directory with the name `<target_domain>.html`.  

### Sample Command  
```bash
python3 dorkking.py testsite.com  
```
This will generate queries like `site:testsite.com ext:sql` and export the results in an interactive HTML report.

---

## Output 🎯
The tool generates an HTML file with the following:
- Search category (e.g., "Database Files Exposed").  
- Number of results returned from Google.  
- A clickable Google search link to manually explore the results.  

---

## HTML Report Preview 📝  
The report includes:
- **Bootstrap-based design**  
- **Cards for each vulnerability category** with clickable links and payload information  
- **Responsive layout** for easy viewing  

---

## Disclaimer ⚠️  
This tool is for **educational purposes only**. Unauthorized scanning or dorking of websites without permission is illegal. Use responsibly!

---

## License 💄  
[MIT License](LICENSE)

