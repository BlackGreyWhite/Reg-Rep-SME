# Azure AI Foundry RAG POC: Complete Guide (2026)
## 🚀 Files + Websites Knowledge Base with GPT-5-mini

### **✅ YOUR ACTUAL SETUP:**
- **Region**: Sweden Central (best latency from India ~150ms)
- **Resource Group**: rg-rag-poc
- **Project**: regrep-sme-poc
- **Storage**: adlsragpoc
- **AI Search**: aisearch-rag-regrep
- **Azure OpenAI**: openai-rag-regrep
- **Deployment**: Global Standard
- **Interface**: NEW Foundry Portal (2026)
- **Model**: GPT-5-mini (latest, no registration needed)

---

## 🎯 What You'll Build

A Retrieval-Augmented Generation (RAG) system that acts as an AI expert by combining:
- 📄 **Your internal documents** (stored in Azure Data Lake Storage)
- 🌐 **Specific websites** (automatically scraped and indexed)

**The AI will answer questions using both sources and cite where information came from!**

---

## 📋 Prerequisites

### Azure Requirements
- [ ] **Azure Free Trial** ($200 credit) - Sign up: https://azure.microsoft.com/free/
- [ ] **Estimated POC cost**: $1-5 (if you delete resources same day)
- [ ] **Time needed**: 3-4 hours total

### Local Setup
- [ ] Python 3.10 or higher
- [ ] Visual Studio Code (or any IDE)
- [ ] Azure CLI
- [ ] Terminal/Command Prompt

### Knowledge Sources
- [ ] 3-5 documents to upload (PDFs, Word docs, text files)
- [ ] List of 2-3 websites to scrape (check robots.txt)

---

## 🌍 Why Sweden Central?

**You're using Sweden Central region because:**
- ✅ **Great latency from India** (~150ms - better than East US)
- ✅ **GPT-5-mini fully supported** (Global Standard available)
- ✅ **GDPR compliant** (European data protection)
- ✅ **Excellent infrastructure** (mature region)
- ✅ **All resources in one region** (faster, cheaper)
- ✅ **Better model availability than India regions**

**Important:** All your resources are in Sweden Central for optimal performance.

---

## 💰 Cost Expectations

### If You Complete POC in One Day:
- **Total cost**: $1-3 ✅
- **Breakdown**: 
  - AI Search: $2.50/day × 0.3 days = $0.75
  - GPT-5-mini: ~$0.50 for all queries
  - ADLS: ~$0.10
  - Other: Negligible

### If You Leave Resources Running:
- **Daily cost**: ~$3.10/day
- **1 week**: $21.70 ⚠️
- **1 month**: $93 ❌

**🛡️ Protection: Set up cost alerts immediately! (We'll show you how)**

---

## 🔧 Phase 1: Azure Portal Setup (30-45 minutes)

### Step 1.1: Create Azure Data Lake Storage Gen2

**Why:** Store your source documents (PDFs, Word docs, etc.)

1. **Open Azure Portal** → https://portal.azure.com
2. **Search** "Storage accounts" (top search bar)
3. **Click** "+ Create"

4. **Basics tab:**
   - **Subscription**: Your subscription
   - **Resource Group**: Click "Create new" → Name: `rg-rag-sweden`
   - **Storage account name**: `adlsrag[yourname]` (must be globally unique, lowercase)
   - **Region**: **Sweden Central** ⭐
   - **Performance**: Standard
   - **Redundancy**: **LRS (Locally Redundant Storage)** ← Cheapest

5. **Click** "Next: Advanced"

6. **Advanced tab:**
   - ✅ **IMPORTANT**: Enable **"Hierarchical namespace"** (this makes it ADLS Gen2)
   - Keep other defaults

7. **Click** "Review + Create" → "Create"

8. **Wait** 1-2 minutes for deployment

**After Deployment:**

9. **Click** "Go to resource"
10. **Left menu** → "Containers"
11. **Click** "+ Container"
    - **Name**: `knowledge-base`
    - **Access level**: Private
12. **Click** "Create"

**Upload Your Documents:**

13. **Click** on `knowledge-base` container
14. **Click** "Upload" button
15. **Select** 3-5 files (PDFs, Word docs, text files)
    - Keep under 10MB each for POC
    - Examples: product docs, policies, research papers
16. **Click** "Upload"
17. **Verify** files appear in the list

✅ **Done! Storage ready.**

---

### Step 1.2: Create Azure AI Search Service

**Why:** Creates searchable index for documents + web content

1. **Azure Portal** (stay logged in)
2. **Search** "Azure AI Search"
3. **Click** "+ Create"

4. **Configure:**
   - **Subscription**: Your subscription
   - **Resource Group**: Select `rg-rag-sweden`
   - **Service name**: `aisearch-rag-sweden` (or unique name)
   - **Location**: **Sweden Central** ⭐
   - **Pricing tier**: **Basic** ← $75/month, but we'll delete it

5. **Click** "Review + Create" → "Create"

6. **Wait** 2-3 minutes

**💰 Cost Alert:** This is your biggest cost (~$2.50/day). Delete when done!

✅ **Done! Search service ready.**

---

### Step 1.3: Create Azure OpenAI Service

**Why:** Provides GPT-5-mini and embedding models

1. **Azure Portal**
2. **Search** "Azure OpenAI"
3. **Click** "+ Create"

4. **⚠️ IMPORTANT**: Select **"Azure OpenAI"** (second option)
   - NOT "Foundry (Recommended)"

5. **Configure:**
   - **Subscription**: Your subscription
   - **Resource Group**: Select `rg-rag-sweden`
   - **Region**: **Sweden Central** ⭐
   - **Name**: `openai-rag-sweden`
   - **Pricing tier**: S0 (Standard)

6. **Click** "Next" through tabs → "Create"

7. **Wait** 3-5 minutes

✅ **Done! OpenAI service ready.**

---

### Step 1.4: Set Up Cost Alerts (CRITICAL!)

**Do this now to avoid surprises!**

1. **Azure Portal** → Search "Cost Management"
2. **Click** "Cost Management + Billing"
3. **Left menu** → "Budgets"
4. **Click** "+ Add"

5. **Configure Budget:**
   - **Scope**: Your subscription
   - **Name**: "RAG POC Budget"
   - **Reset period**: Monthly
   - **Amount**: $20
   
6. **Alert conditions** (create multiple):
   - Alert at 50% ($10)
   - Alert at 80% ($16)
   - Alert at 100% ($20)

7. **Alert recipients**:
   - Enter your email

8. **Click** "Create"

✅ **Done! You'll get email alerts if costs rise.**

---

## 🎨 Phase 2: Azure AI Foundry Setup (25-35 minutes)

### Step 2.1: Create Foundry Project

1. **Navigate to** → https://ai.azure.com

2. You'll see the **NEW Foundry** interface
   - Welcome message
   - "Create smarter agents with Microsoft Foundry"

3. **Find project creation** (one of these options):
   - Click **"Start building"** dropdown → "Create a project"
   - OR: Your profile icon (top-right) → "All projects" → "+ New project"
   - OR: Look for "Create" button in top navigation

4. **Dialog appears:** "Create a project"

5. **Fill in basic info:**
   - **Project name**: `rag-sweden-poc`

6. **Click** "Advanced options" to expand

7. **Configure advanced settings:**
   - **Subscription**: Your subscription
   - **Resource group**: Select `rg-rag-sweden`
   - **Region**: **Sweden Central** ⭐
   - **Microsoft Foundry resource**: Auto-generated name is fine (e.g., `rag-sweden-poc-resource`)
   - **Public network access**: Enabled (keep default)

8. **Review your settings:**
   - ✅ Region: Sweden Central
   - ✅ Resource group: rg-rag-sweden
   - ✅ Everything matches!

9. **Click** blue "Create" button

10. **Wait** 5-10 minutes for deployment
    - Progress screen will show
    - Creating project workspace
    - Creating Foundry resource (backend infrastructure)

11. **When complete**, you'll see your project welcome page:
    - Project name in top-left
    - Project endpoint (visible)
    - Project API key (hidden with dots)
    - Project region: swedencentral ✅

✅ **Done! Project created.**

**💡 Note:** The NEW Foundry automatically created the "hub" (now called "Foundry resource"). No separate step needed like in old classic mode!

---

### Step 2.2: Understanding the NEW Foundry Navigation

**Your welcome screen shows:**
- **Top bar**: Home | Discover | Build | Operate | Docs
- **Project info**: Endpoint, API key, region
- **"New arrivals"**: Latest model announcements

**Navigation Pattern:**
- **Home** → Welcome page (where you are)
- **Discover** → Browse AI capabilities
- **Build** ⭐ → Deploy models, create agents (we'll use this!)
- **Operate** ⭐ → Manage connections, monitor (we'll use this!)
- **Docs** → Help and documentation

**No left sidebar on home page** - use top tabs instead!

---

### Step 2.3: Deploy GPT-5-mini (Chat Model)

1. **Click "Build"** tab (top navigation)

2. **Look for "Models"** section
   - You might see: "Models", "Model catalog", or "Browse models"
   - Click on it

3. **Search for GPT-5-mini:**
   - Use search bar at top
   - Type: "gpt-5-mini"
   - Find: **"gpt-5-mini (2025-08-07)"** or similar
   - Provider should show: "Azure OpenAI"

4. **Click on the model card**
   - Details page opens
   - Shows capabilities, pricing, regions

5. **Click "Deploy"** button (usually blue, top-right)

6. **Deployment configuration panel appears:**

   **Settings to configure:**
   
   - **Deployment name**: `gpt-5-mini`
     - ⚠️ **CRITICAL**: Use this exact name! Your code expects it.
   
   - **Deployment type**: Click dropdown
     - You'll see: Global Standard, Data Zone Standard, etc.
     - **Select**: ✅ **"Global Standard"** ⭐
     - This is Microsoft's recommended option for Sweden Central
     - Same price as Data Zone Standard, better performance
   
   - **Model version**: Keep "Latest" or "2025-08-07"
     - This is the latest stable version
   
   - **Model version upgrade policy**: "Upgrade once new default version becomes available"
     - Keep this default (auto-updates to newer versions)
   
   - **Tokens per Minute Rate Limit**: 
     - **IMPORTANT**: Change from 100,000 to **50,000**
     - Drag the slider LEFT to the middle (50K)
     - Or type **50000** in the box
     - Shows: "50000 / 200000"
     - ✅ Saves costs, plenty for POC (processes ~20-30 pages/min)
   
   - **Guardrails**: "DefaultV2"
     - Keep this default (content filtering)
   
   - **Other settings**: Keep defaults

7. **Click "Deploy"** or "Create deployment"

8. **Wait 2-3 minutes**
   - Progress indicator shows
   - Status changes: Creating → Succeeded

9. **Verify deployment:**
   - Stay in Build → Models area
   - Look for "Deployments" tab or section
   - Should show: `gpt-5-mini` with green ✓ "Succeeded"

✅ **Done! Chat model deployed.**

**💡 Why Global Standard?**
- Microsoft's recommended deployment type
- Better performance and routing optimization
- Higher quota availability in Sweden Central
- Same price as Data Zone Standard (both charge per token)
- Production-grade reliability
- Full feature access

**💡 Why 50K TPM not 100K?**
- ✅ **Lower quota requirement** - Easier approval, less likely to hit limits
- ✅ **Costs less** - Saves ~$1.50/month in base fees
- ✅ **Still 50x more than needed** - Your POC will use ~500-1000 TPM total
- ✅ **Can increase later** - If you need more, you can adjust anytime
- 📊 **Reference**: 50K TPM processes ~20-30 pages of text per minute

**Note:** We initially considered Data Zone Standard as a safer option to avoid quota issues, but Sweden Central has excellent quota for Global Standard, making it the superior choice!

---

### Step 2.4: Deploy text-embedding-3-small (Embedding Model)

**Still in Build tab:**

1. **Go back to "Models"** (main section)
   - Use breadcrumb navigation or back button
   - Or click "Models" again

2. **Search**: "text-embedding-3-small"
   - Clear previous search
   - Type the full name
   - Find: **"text-embedding-3-small"**

3. **Click on model card**

4. **Click "Deploy"**

5. **Configure deployment:**
   - **Deployment name**: `text-embedding-3-small`
     - ⚠️ **CRITICAL**: Use exact name!
   - **Deployment type**: **Global Standard** ⭐
   - **Model version**: Latest
   - **Tokens per Minute**: **50,000** 
     - Type 50000 in the box or drag slider to middle
     - Same reasoning as GPT-5-mini (cost savings, plenty for POC)
   - **Guardrails**: DefaultV2 (keep default)
   - Keep other defaults

6. **Click "Deploy"**

7. **Wait 2-3 minutes**

8. **Verify both deployments:**
   - Build → Models → Deployments
   - Should see TWO models:
     - ✅ `gpt-5-mini` - Status: Succeeded
     - ✅ `text-embedding-3-small` - Status: Succeeded
   - Both with green checkmarks

✅ **Done! Both models deployed.**

**⚠️ Model Names Are Critical!**
The Python code references these exact deployment names. If you used different names, you'll need to update your `.env` file later.

**💡 Why text-embedding-3-small?**
- ✅ **5x cheaper** than ada-002 ($0.02 vs $0.10 per 1M tokens)
- ✅ **Better quality** (62% better on benchmarks)
- ✅ **Available in Sweden Central**
- ✅ Same 1,536 dimensions as ada-002
- ✅ Recommended for 2026!

---

### Step 2.5: Connect Azure AI Search

**Why:** Allows your code to search the knowledge base

1. **Click "Operate"** tab (top navigation)

2. **Look for "Connected resources"** or "Connections"
   - Might be under: Resources, Connections, Connected services
   - Navigate to connections section

3. **Check if Azure AI Search already connected:**
   - Look through list
   - See if type "Azure AI Search" exists
   - If YES with "Connected" status → skip to Step 2.6!

4. **If NOT connected:**
   - Click **"+ New connection"** or **"Add connection"**
   - Panel or dialog appears

5. **Configure connection:**
   - **Service type**: Select **"Azure AI Search"**
   - **Subscription**: Your subscription
   - **Resource**: Select `aisearch-rag-sweden`
   - **Connection name**: Auto-generated is fine
   - **Authentication**: **"API key"** ← Simpler for POC
     - ⚠️ Use Managed Identity for production!

6. **Click "Add"** or "Create"

7. **Verify:**
   - Back in connections list
   - Should see: aisearch-rag-sweden
   - Type: Azure AI Search
   - Status: Connected ✓ (green indicator)

✅ **Done! Search connected.**

---

### Step 2.6: Get Your Project Connection String

**This connects your Python code to the project.**

**You need this format:**
```
<region>.api.azureml.ms;<subscription-id>;<resource-group>;<project-name>
```

#### **Method 1: Build It Yourself (Easiest)**

**Step A: Get your Subscription ID**

1. **Azure Portal** → https://portal.azure.com
2. **Search** "Subscriptions"
3. **Click** on your subscription
4. **Copy** the "Subscription ID"
   - Format: `12345678-abcd-1234-5678-123456789012`
   - Save this!

**Step B: Build the connection string**

Using your info:
```
swedencentral.api.azureml.ms;<your-subscription-id>;rg-rag-sweden;rag-sweden-poc
```

**Example:**
```
swedencentral.api.azureml.ms;12345678-abcd-1234-5678-123456789012;rg-rag-sweden;rag-sweden-poc
```

#### **Method 2: Find in Foundry (Alternative)**

1. **Operate** tab
2. Look for **"Settings"** or **"Properties"**
3. Find **"Connection string"** or **"Project details"**
4. Copy it

#### **Method 3: Azure CLI (Backup)**

```bash
# Get subscription ID
az account show --query id -o tsv

# Then build connection string manually
```

**Save this connection string!** You'll need it for `.env` file.

✅ **Done! Phase 2 complete.**

---

## 💻 Phase 3: Local Development Setup (15-20 minutes)

### Step 3.1: Create Project Folder

**Windows (PowerShell/CMD):**
```bash
# Create and navigate to project folder
mkdir rag-poc
cd rag-poc

# Create Python virtual environment
py -3 -m venv .venv

# Activate it
.venv\Scripts\activate

# Verify Python version (should be 3.10+)
python --version
```

**Mac/Linux (Terminal):**
```bash
# Create and navigate to project folder
mkdir rag-poc
cd rag-poc

# Create Python virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate

# Verify Python version
python --version
```

**✅ You should see:** `Python 3.10.x` or higher

---

### Step 3.2: Install Python Packages

1. **Create `requirements.txt`** in your `rag-poc` folder:

```txt
# Azure AI packages
azure-ai-projects==1.0.0b10
azure-ai-inference[prompts]
azure-identity
azure-search-documents
azure-storage-blob

# Data processing
python-dotenv
pypdf

# Web scraping packages
beautifulsoup4
requests
playwright
lxml
html2text
aiohttp

# Web UI (optional)
streamlit
```

2. **Install packages:**
```bash
pip install -r requirements.txt
```

**Wait 3-5 minutes** for installation.

3. **Install Playwright browsers** (for dynamic website scraping):
```bash
playwright install chromium
```

**Wait 1-2 minutes**.

✅ **Done! Packages installed.**

---

### Step 3.3: Install Azure CLI

**Windows:**
```bash
winget install -e --id Microsoft.AzureCLI
```

**Mac:**
```bash
brew update && brew install azure-cli
```

**Linux:**
```bash
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

**Sign in:**
```bash
az login
```
- Browser window opens
- Sign in with your Azure account
- Return to terminal
- Should see "Login successful"

**Verify:**
```bash
az account show
```
- Should show your subscription details

✅ **Done! Azure CLI ready.**

---

### Step 3.4: Create Configuration Files

#### **File 1: `.env` (Environment Variables)**

Create `.env` in `rag-poc` folder:

```env
# Azure AI Foundry Project Connection
AIPROJECT_CONNECTION_STRING=swedencentral.api.azureml.ms;58a263f1-4410-4cb7-83b7-c3dd6e1a0e41;rg-rag-poc;regrep-sme-poc

# Azure AI Search (direct connection)
AISEARCH_ENDPOINT=https://aisearch-rag-regrep.search.windows.net
AISEARCH_KEY=<get-from-portal-keys-section>
AISEARCH_INDEX_NAME=unified-knowledge-index

# Azure AI Foundry Models (use /models endpoint for SDK)
FOUNDRY_ENDPOINT=https://regrep-sme-poc-resource.services.ai.azure.com/models
FOUNDRY_KEY=<get-from-foundry-portal>

# ADLS Storage (direct connection)
ADLS_ACCOUNT_NAME=adlsragpoc
ADLS_ACCOUNT_KEY=<get-from-portal-access-keys>
ADLS_CONTAINER_NAME=knowledge-base

# Model Deployments (must match deployment names in Foundry)
EMBEDDINGS_MODEL=text-embedding-3-small
CHAT_MODEL=gpt-5-mini

# Web Scraping Settings
WEB_SCRAPE_DELAY=2
WEB_MAX_PAGES_PER_SITE=50
WEB_USER_AGENT=Mozilla/5.0 (compatible; RAG-Bot/1.0)
```

**⚠️ Get your API keys:**
1. **AI Search Key**: Portal → aisearch-rag-regrep → Keys → Copy "Primary admin key"
2. **Foundry Key**: ai.azure.com → Your project (regrep-sme-poc) → Home page → Copy API key (shown with dots)
3. **Storage Key**: Portal → adlsragpoc → Access keys → key1 → Copy "Key"

**⚠️ CRITICAL:** FOUNDRY_ENDPOINT must end with `/models` (not the full project path) for SDK to work!

#### **File 2: `.gitignore` (Protect Secrets)**

Create `.gitignore`:

```txt
.env
.venv/
__pycache__/
*.pyc
.playwright/
scraped_content/
*.log
```

#### **File 3: `website_sources.txt` (Websites to Scrape)**

Create `website_sources.txt`:

```txt
# Add your specific websites here (one per line)
# Check robots.txt before adding!

# Example: MAS Singapore (financial regulations)
https://www.mas.gov.sg/regulation

# Add your websites below:
# https://yourcompany.com/docs
# https://industry-site.com/resources
```

**💡 Important:**
- One URL per line
- Check `https://website.com/robots.txt` first
- Respect "Crawl-delay" settings
- Only scrape publicly available content

✅ **Done! Configuration ready.**

---

## 🔨 Phase 4: Create the RAG Application

**Now we create 5 Python files. Copy each exactly as shown.**

### File 1: `config.py` (Helper Functions)

```python
import os
import sys
import pathlib
import logging
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.inference.tracing import AIInferenceInstrumentor
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up logging
logger = logging.getLogger("app")
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(stream=sys.stdout))

def get_logger(module_name):
    """Returns a module-specific logger"""
    return logging.getLogger(f"app.{module_name}")

def enable_telemetry(log_to_project: bool = False):
    """Enable instrumentation and telemetry logging"""
    AIInferenceInstrumentor().instrument()
    
    # Enable logging message contents
    os.environ["AZURE_TRACING_GEN_AI_CONTENT_RECORDING_ENABLED"] = "true"
    
    if log_to_project:
        from azure.monitor.opentelemetry import configure_azure_monitor
        
        project = AIProjectClient.from_connection_string(
            conn_str=os.environ["AIPROJECT_CONNECTION_STRING"],
            credential=DefaultAzureCredential()
        )
        
        application_insights_connection_string = project.telemetry.get_connection_string()
        if application_insights_connection_string:
            configure_azure_monitor(connection_string=application_insights_connection_string)
            logger.info("Telemetry enabled - view traces in Azure AI Foundry")

def get_project_client():
    """Get authenticated project client"""
    return AIProjectClient.from_connection_string(
        conn_str=os.environ["AIPROJECT_CONNECTION_STRING"],
        credential=DefaultAzureCredential()
    )
```

### File 2: `web_scraper.py` (Website Scraping)

```python
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
```

### File 3: `create_search_index.py` (Create Index)

```python
import os
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SearchField,
    SearchFieldDataType,
    VectorSearch,
    HnswAlgorithmConfiguration,
    VectorSearchProfile,
    SemanticConfiguration,
    SemanticField,
    SemanticPrioritizedFields,
    SemanticSearch
)
from dotenv import load_dotenv

load_dotenv()

def create_unified_search_index():
    """Create Azure AI Search index for BOTH ADLS documents AND web content"""
    
    # Connection using API key (works with NEW Foundry)
    search_endpoint = os.environ["AISEARCH_ENDPOINT"]
    search_key = os.environ["AISEARCH_KEY"]
    
    index_client = SearchIndexClient(
        endpoint=search_endpoint,
        credential=AzureKeyCredential(search_key)
    )
    
    index_name = os.environ["AISEARCH_INDEX_NAME"]
    
    # Define index schema with source type
    fields = [
        SearchField(name="id", type=SearchFieldDataType.String, key=True, sortable=True, filterable=True),
        SearchField(name="content", type=SearchFieldDataType.String, searchable=True),
        SearchField(name="title", type=SearchFieldDataType.String, searchable=True, filterable=True, sortable=True),
        SearchField(name="source_type", type=SearchFieldDataType.String, filterable=True, facetable=True),
        SearchField(name="source_path", type=SearchFieldDataType.String, filterable=True),
        SearchField(name="url", type=SearchFieldDataType.String, filterable=True),
        SearchField(
            name="content_vector",
            type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
            searchable=True,
            vector_search_dimensions=1536,
            vector_search_profile_name="myHnswProfile"
        )
    ]
    
    # Configure vector search
    vector_search = VectorSearch(
        algorithms=[HnswAlgorithmConfiguration(name="myHnsw")],
        profiles=[VectorSearchProfile(name="myHnswProfile", algorithm_configuration_name="myHnsw")]
    )
    
    # Configure semantic search
    semantic_config = SemanticConfiguration(
        name="my-semantic-config",
        prioritized_fields=SemanticPrioritizedFields(
            title_field=SemanticField(field_name="title"),
            content_fields=[SemanticField(field_name="content")]
        )
    )
    
    semantic_search = SemanticSearch(configurations=[semantic_config])
    
    # Create index
    index = SearchIndex(
        name=index_name,
        fields=fields,
        vector_search=vector_search,
        semantic_search=semantic_search
    )
    
    print(f"Creating unified search index: {index_name}")
    result = index_client.create_or_update_index(index)
    print(f"✓ Index created: {result.name}")
    
    return result

if __name__ == "__main__":
    create_unified_search_index()
    print("\n✓ Unified search index created successfully!")
    print("  - Ready for ADLS files")
    print("  - Ready for web content")
```

### File 4: `index_all_sources.py` (Index Everything)

```python
"""
Unified indexing script that indexes BOTH:
1. Documents from Azure Data Lake Storage
2. Content from websites
"""

import os
import hashlib
from typing import List, Dict
from azure.core.credentials import AzureKeyCredential
from azure.storage.blob import BlobServiceClient
from azure.search.documents import SearchClient
from azure.ai.inference import EmbeddingsClient
from web_scraper import scrape_all_sources
from dotenv import load_dotenv

load_dotenv()

def extract_text_from_blob(blob_client):
    """Extract text from blob (supports PDF, text, and other formats)"""
    try:
        blob_data = blob_client.download_blob()
        content = blob_data.readall()
        
        # Check if it's a PDF
        if blob_client.blob_name.lower().endswith('.pdf'):
            from pypdf import PdfReader
            import io
            
            pdf_file = io.BytesIO(content)
            reader = PdfReader(pdf_file)
            
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            
            return text
        
        # Try to decode as text
        try:
            text = content.decode('utf-8')
        except:
            text = str(content)
        
        return text
    except Exception as e:
        print(f"Error extracting text: {e}")
        return ""

def chunk_text(text, chunk_size=1000, overlap=200):
    """Split text into overlapping chunks"""
    chunks = []
    start = 0
    
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        
        if chunk:
            chunks.append(chunk)
        
        start = end - overlap
    
    return chunks

def get_embeddings(text, embeddings_client):
    """Generate embeddings for text"""
    response = embeddings_client.embed(
        input=[text],
        model=os.environ["EMBEDDINGS_MODEL"]
    )
    return response.data[0].embedding

def index_adls_documents(embeddings_client, search_client) -> List[Dict]:
    """Index documents from ADLS"""
    print("\n" + "="*80)
    print("INDEXING ADLS DOCUMENTS")
    print("="*80)
    
    # Connection using storage account key
    adls_account = os.environ["ADLS_ACCOUNT_NAME"]
    adls_key = os.environ["ADLS_ACCOUNT_KEY"]
    container_name = os.environ["ADLS_CONTAINER_NAME"]
    
    blob_service_client = BlobServiceClient(
        account_url=f"https://{adls_account}.blob.core.windows.net",
        credential=adls_key
    )
    
    container_client = blob_service_client.get_container_client(container_name)
    blobs = container_client.list_blobs()
    
    documents = []
    
    for blob in blobs:
        print(f"Processing file: {blob.name}")
        
        blob_client = container_client.get_blob_client(blob.name)
        text = extract_text_from_blob(blob_client)
        
        if not text:
            print(f"Warning: No text extracted from {blob.name}")
            continue
        
        chunks = chunk_text(text)
        
        for i, chunk in enumerate(chunks):
            doc_id = hashlib.md5(f"adls_{blob.name}_{i}".encode()).hexdigest()
            embedding = get_embeddings(chunk, embeddings_client)
            
            doc = {
                "id": doc_id,
                "content": chunk,
                "title": blob.name,
                "source_type": "adls_file",
                "source_path": blob.name,
                "url": blob_client.url,
                "content_vector": embedding
            }
            
            documents.append(doc)
            print(f"  Created chunk {i+1}/{len(chunks)}")
    
    print(f"✓ Prepared {len(documents)} documents from ADLS")
    return documents

def index_web_content(embeddings_client, search_client) -> List[Dict]:
    """Index content from websites"""
    print("\n" + "="*80)
    print("INDEXING WEB CONTENT")
    print("="*80)
    
    max_pages = int(os.getenv("WEB_MAX_PAGES_PER_SITE", 50))
    web_results = scrape_all_sources(max_pages_per_site=max_pages)
    
    if not web_results:
        print("Warning: No web content scraped")
        return []
    
    documents = []
    
    for result in web_results:
        print(f"Processing: {result['title'][:60]}...")
        
        chunks = chunk_text(result['content'])
        
        for i, chunk in enumerate(chunks):
            doc_id = hashlib.md5(f"web_{result['url']}_{i}".encode()).hexdigest()
            embedding = get_embeddings(chunk, embeddings_client)
            
            doc = {
                "id": doc_id,
                "content": chunk,
                "title": result['title'],
                "source_type": "website",
                "source_path": result['url'],
                "url": result['url'],
                "content_vector": embedding
            }
            
            documents.append(doc)
        
        print(f"  Created {len(chunks)} chunks")
    
    print(f"✓ Prepared {len(documents)} documents from web")
    return documents

def index_all_sources():
    """Index ALL sources: ADLS files + Websites"""
    
    # Connection to Foundry models using API key
    foundry_endpoint = os.environ["FOUNDRY_ENDPOINT"]
    foundry_key = os.environ["FOUNDRY_KEY"]
    
    embeddings_client = EmbeddingsClient(
        endpoint=foundry_endpoint,
        credential=AzureKeyCredential(foundry_key)
    )
    
    # Connection to Azure AI Search using API key
    search_endpoint = os.environ["AISEARCH_ENDPOINT"]
    search_key = os.environ["AISEARCH_KEY"]
    search_client = SearchClient(
        endpoint=search_endpoint,
        index_name=os.environ["AISEARCH_INDEX_NAME"],
        credential=AzureKeyCredential(search_key)
    )
    
    all_documents = []
    
    try:
        adls_docs = index_adls_documents(embeddings_client, search_client)
        all_documents.extend(adls_docs)
    except Exception as e:
        print(f"Error indexing ADLS: {e}")
    
    try:
        web_docs = index_web_content(embeddings_client, search_client)
        all_documents.extend(web_docs)
    except Exception as e:
        print(f"Error indexing web content: {e}")
    
    if all_documents:
        print("\n" + "="*80)
        print(f"UPLOADING {len(all_documents)} TOTAL DOCUMENTS TO INDEX")
        print("="*80)
        
        batch_size = 100
        for i in range(0, len(all_documents), batch_size):
            batch = all_documents[i:i+batch_size]
            result = search_client.upload_documents(documents=batch)
            print(f"Uploaded batch {i//batch_size + 1}: {len(batch)} documents")
        
        print("\n" + "="*80)
        print("✓ INDEXING COMPLETE!")
        print("="*80)
        print(f"Total documents indexed: {len(all_documents)}")
        
        adls_count = sum(1 for d in all_documents if d['source_type'] == 'adls_file')
        web_count = sum(1 for d in all_documents if d['source_type'] == 'website')
        print(f"  - ADLS files: {adls_count}")
        print(f"  - Web pages: {web_count}")
    else:
        print("Warning: No documents to index!")

if __name__ == "__main__":
    index_all_sources()
```

### File 5: `chat_with_knowledge.py` (RAG Chat App)

```python
import os
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from dotenv import load_dotenv

load_dotenv()

def search_documents(query, search_client, top=5):
    """Search for relevant documents from ALL sources"""
    results = search_client.search(
        search_text=query,
        top=top,
        select=["content", "title", "source_type", "source_path", "url"]
    )
    
    documents = []
    for result in results:
        documents.append({
            "content": result["content"],
            "title": result["title"],
            "source_type": result["source_type"],
            "source_path": result["source_path"],
            "url": result.get("url", "")
        })
    
    return documents

def create_context_from_documents(documents):
    """Create context string from retrieved documents"""
    context_parts = []
    
    for i, doc in enumerate(documents, 1):
        source_label = "FILE" if doc['source_type'] == 'adls_file' else "WEB"
        # Limit content length per source to avoid overwhelming the model
        content = doc['content'][:1000]  # First 1000 chars only
        context_parts.append(
            f"[Source {i} - {source_label}: {doc['title']}]\n{content}\n"
        )
    
    return "\n---\n".join(context_parts)  # Clear separator between sources

def chat_with_rag(query, show_sources=True):
    """Main RAG chat function with mixed sources"""
    
    # Connection to Azure AI Search using API key
    search_endpoint = os.environ["AISEARCH_ENDPOINT"]
    search_key = os.environ["AISEARCH_KEY"]
    search_client = SearchClient(
        endpoint=search_endpoint,
        index_name=os.environ["AISEARCH_INDEX_NAME"],
        credential=AzureKeyCredential(search_key)
    )
    
    # Connection to Foundry models using API key
    foundry_endpoint = os.environ["FOUNDRY_ENDPOINT"]
    foundry_key = os.environ["FOUNDRY_KEY"]
    chat_client = ChatCompletionsClient(
        endpoint=foundry_endpoint,
        credential=AzureKeyCredential(foundry_key)
    )
    
    print(f"Searching knowledge base for: {query}")
    documents = search_documents(query, search_client)
    
    if not documents:
        print("Warning: No relevant documents found")
        return "I couldn't find any relevant information to answer your question."
    
    context = create_context_from_documents(documents)
    
    adls_sources = sum(1 for d in documents if d['source_type'] == 'adls_file')
    web_sources = sum(1 for d in documents if d['source_type'] == 'website')
    
    print(f"Found {len(documents)} relevant sources ({adls_sources} files, {web_sources} web pages)")
    
    system_prompt = """Answer questions using the information provided in the sources below.

Example:
Question: What regulations does MAS enforce?
Sources: "MAS enforces financial regulations and monetary policy..."
Answer: According to Source 1, MAS enforces financial regulations and oversees monetary policy in Singapore.

Now answer the user's question using the same approach.

Sources:
{context}

Question: {question}

Provide a clear, helpful answer and cite the source number(s).
"""
    
    messages = [
        SystemMessage(content=system_prompt.format(context=context, question=query)),
        UserMessage(content=query)
    ]
    
    print("Generating response with GPT-5-mini...")
    response = chat_client.complete(
        model=os.environ["CHAT_MODEL"],
        messages=messages
    )
    
    answer = response.choices[0].message.content
    
    print("\n" + "="*80)
    print("ANSWER:")
    print("="*80)
    print(answer)
    
    # Only show sources if we have a real answer (not "I don't know" response)
    if show_sources and not any(phrase in answer.lower() for phrase in [
        "don't have", "couldn't find", "no information", "don't know", "unable to", 
        "can't find", "cannot find", "no relevant"
    ]):
        print("\n" + "="*80)
        print("SOURCES:")
        print("="*80)
        for i, doc in enumerate(documents, 1):
            icon = "📄" if doc['source_type'] == 'adls_file' else "🌐"
            print(f"{i}. {icon} {doc['title']}")
            print(f"   {doc['url'] or doc['source_path']}")
        print("="*80 + "\n")
    
    return answer

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, required=True, help="Question to ask")
    parser.add_argument("--no-sources", action="store_true", help="Don't show sources")
    
    args = parser.parse_args()
    
    chat_with_rag(args.query, not args.no_sources)
```

✅ **Done! All 5 files created.**

---

## 🚀 Phase 5: Run and Test (20-30 minutes)

### Step 5.1: Prepare Website Sources

**Edit `website_sources.txt`:**

```txt
# Example: Add your websites here
https://www.mas.gov.sg/regulation
https://www.mas.gov.sg/publications

# Add more below:
```

**Optional - Test scraping first:**
```bash
python web_scraper.py
```

---

### Step 5.2: Create Search Index

```bash
# Make sure venv is activated!
# Windows: .venv\Scripts\activate
# Mac/Linux: source .venv/bin/activate

python create_search_index.py
```

**Expected output:**
```
Creating unified search index: unified-knowledge-index
✓ Index created: unified-knowledge-index
  - Ready for ADLS files
  - Ready for web content
```

---

### Step 5.3: Index All Sources

```bash
python index_all_sources.py
```

**Expected output:**
```
================================================================================
INDEXING ADLS DOCUMENTS
================================================================================
Processing file: document1.pdf
  Created chunk 1/5
  ...
✓ Prepared 15 documents from ADLS

================================================================================
INDEXING WEB CONTENT
================================================================================
Processing website: https://www.mas.gov.sg/regulation
Scraping (static): https://www.mas.gov.sg/regulation
✓ Scraped 1/50
...
✓ Prepared 45 documents from web

================================================================================
UPLOADING 60 TOTAL DOCUMENTS TO INDEX
================================================================================
Uploaded batch 1: 60 documents

================================================================================
✓ INDEXING COMPLETE!
================================================================================
Total documents indexed: 60
  - ADLS files: 15
  - Web pages: 45
```

**⏱️ This takes 5-15 minutes depending on website count!**

---

### Step 5.4: Test Your RAG System!

```bash
# Basic query
python chat_with_knowledge.py --query "What are the main topics covered?"

# Query about web sources
python chat_with_knowledge.py --query "What are the latest regulations?"

# Query about files
python chat_with_knowledge.py --query "Summarize the key points from our documents"

# With telemetry (view traces in Foundry)
python chat_with_knowledge.py --query "Compare internal and external information" --enable-telemetry
```

**Expected output:**
```
================================================================================
ANSWER:
================================================================================
Based on the sources provided:

From our internal documentation (Source 1 - File):
- Topic A is covered extensively
- Key point B is emphasized

From industry regulations (Source 3 - Web):
- Requirement X must be followed
- Standard Y is recommended

This response was powered by GPT-5-mini in Sweden Central!

================================================================================
SOURCES:
================================================================================
1. 📄 internal-policy.pdf
   https://adlsrag[yourname].blob.core.windows.net/knowledge-base/internal-policy.pdf
2. 📄 product-manual.docx
   https://adlsrag[yourname].blob.core.windows.net/knowledge-base/product-manual.docx
3. 🌐 MAS Regulations - Overview
   https://www.mas.gov.sg/regulation
4. 🌐 MAS Publications
   https://www.mas.gov.sg/publications
================================================================================
```

🎉 **It works! You've built a complete RAG system!**

---

## ✅ Success Checklist

- [ ] All resources created in Sweden Central
- [ ] GPT-5-mini deployed (Global Standard)
- [ ] text-embedding-3-small deployed
- [ ] Azure AI Search connected
- [ ] Search index created
- [ ] ADLS documents indexed
- [ ] Website content scraped and indexed
- [ ] RAG chat returns answers from both sources
- [ ] Sources clearly labeled (📄 vs 🌐)
- [ ] Sources only shown for valid answers (not "don't know" responses)

---

## 📊 Phase 6: Evaluate Your RAG System (Optional but Recommended)

### Why Evaluate?

**You need to know:**
- ✅ Does it answer correctly?
- ✅ Does it cite the right sources?
- ✅ Does it refuse to answer when it doesn't know?
- ✅ Does it hallucinate (make up facts)?

---

### Quick Manual Testing (5 minutes)

**Test 1: Known Fact**
```bash
python chat_with_knowledge.py --query "What regulations are mentioned in the documents?"
```
✅ **Check:** Does the answer match what's actually in your documents?

**Test 2: Not in Documents**
```bash
python chat_with_knowledge.py --query "What is the best pizza topping?"
```
✅ **Check:** Should say "I don't have information" and NOT show sources

**Test 3: Verify Sources**
```bash
python chat_with_knowledge.py --query "What are the key compliance requirements?"
```
✅ **Check:** Open the cited sources - is that info actually there?

**Test 4: Ambiguous Question**
```bash
python chat_with_knowledge.py --query "Tell me about regulations"
```
✅ **Check:** Should cite multiple relevant sources

---

### File 6: `evaluate_rag.py` (Automated Evaluation)

Create this file for systematic testing:

```python
"""
Simple RAG evaluation script
Tests accuracy, relevance, and hallucination detection
"""

import os
from chat_with_knowledge import chat_with_rag

# Test cases: questions you know the answers to
TEST_CASES = [
    {
        "question": "What topics are covered in the Securities and Futures regulations?",
        "expected_keywords": ["securities", "futures", "derivatives", "reporting", "regulation"],
        "should_answer": True
    },
    {
        "question": "What is the best pizza topping recipe?",
        "expected_keywords": ["don't have", "no information", "not in", "no relevant", "don't know"],
        "should_answer": False
    },
    {
        "question": "What regulations does MAS enforce?",
        "expected_keywords": ["mas", "regulation", "financial", "monetary"],
        "should_answer": True
    },
    {
        "question": "How do I bake a chocolate cake?",
        "expected_keywords": ["don't have", "no information", "not in", "no relevant"],
        "should_answer": False
    }
]

def evaluate():
    """Run evaluation tests"""
    print("="*80)
    print("RAG SYSTEM EVALUATION")
    print("="*80)
    
    passed = 0
    failed = 0
    
    for i, test in enumerate(TEST_CASES, 1):
        print(f"\n[Test {i}/{len(TEST_CASES)}] {test['question']}")
        print("-" * 80)
        
        try:
            # Get answer (suppress source printing)
            answer = chat_with_rag(test['question'], show_sources=False)
            
            # Check if answer contains expected keywords
            answer_lower = answer.lower()
            keyword_found = any(kw.lower() in answer_lower for kw in test['expected_keywords'])
            
            # Determine if test passed
            if test['should_answer']:
                # Should give a real answer with expected keywords
                if keyword_found and len(answer) > 50:
                    print("✅ PASS: Found expected content")
                    passed += 1
                else:
                    print("❌ FAIL: Missing expected keywords or answer too short")
                    print(f"   Answer: {answer[:100]}...")
                    failed += 1
            else:
                # Should refuse to answer
                if keyword_found:
                    print("✅ PASS: Correctly refused to answer")
                    passed += 1
                else:
                    print("❌ FAIL: Should have refused but gave an answer")
                    print(f"   Answer: {answer[:100]}...")
                    failed += 1
                    
        except Exception as e:
            print(f"❌ ERROR: {e}")
            failed += 1
    
    # Summary
    print("\n" + "="*80)
    print("EVALUATION SUMMARY")
    print("="*80)
    print(f"Total Tests: {len(TEST_CASES)}")
    print(f"Passed: {passed} ({passed/len(TEST_CASES)*100:.0f}%)")
    print(f"Failed: {failed} ({failed/len(TEST_CASES)*100:.0f}%)")
    
    if passed == len(TEST_CASES):
        print("\n🎉 All tests passed! Your RAG system is working well.")
    elif passed >= len(TEST_CASES) * 0.7:
        print("\n⚠️  Most tests passed, but some issues found. Review failed tests.")
    else:
        print("\n❌ Many tests failed. Review your system configuration.")
    
    return passed, failed

if __name__ == "__main__":
    evaluate()
```

**Run evaluation:**
```bash
python evaluate_rag.py
```

**Expected output:**
```
================================================================================
RAG SYSTEM EVALUATION
================================================================================

[Test 1/3] What does MAS regulate?
--------------------------------------------------------------------------------
✅ PASS: Found expected content

[Test 2/3] What is the best pizza recipe?
--------------------------------------------------------------------------------
✅ PASS: Correctly refused to answer

[Test 3/3] What are the reporting requirements?
--------------------------------------------------------------------------------
✅ PASS: Found expected content

================================================================================
EVALUATION SUMMARY
================================================================================
Total Tests: 3
Passed: 3 (100%)
Failed: 0 (0%)

🎉 All tests passed! Your RAG system is working well.
```

---

### Customize Test Cases

**Edit `TEST_CASES` in `evaluate_rag.py` to match YOUR documents:**

```python
TEST_CASES = [
    {
        # Question about content you KNOW is in your documents
        "question": "What are the key points in [your specific document]?",
        "expected_keywords": ["keyword1", "keyword2", "keyword3"],  # Words that MUST be in answer
        "should_answer": True
    },
    {
        # Question about topic NOT in your documents - should refuse to answer
        "question": "What is [completely unrelated topic]?",
        "expected_keywords": ["don't have", "no information", "not in"],  # Refusal phrases
        "should_answer": False
    }
]
```

**Tips:**
- Add 10-20 test cases for thorough evaluation
- Mix "should answer" and "should refuse" questions (50/50 split)
- Use questions where you know the exact answer
- Test edge cases (vague questions, multi-part questions)

**Example for MAS regulation documents:**
```python
TEST_CASES = [
    {
        "question": "What are the derivatives reporting requirements?",
        "expected_keywords": ["derivatives", "reporting", "requirements"],
        "should_answer": True
    },
    {
        "question": "What is the recipe for chocolate chip cookies?",
        "expected_keywords": ["don't have", "no information"],
        "should_answer": False
    }
]
```

---

### Advanced: Azure AI Evaluation (Built-in Tools)

**For production systems, use Azure's built-in evaluators:**

```bash
pip install azure-ai-evaluation
```

**File 7: `advanced_evaluation.py`**

```python
"""
Advanced evaluation using Azure AI Evaluation SDK
"""

from azure.ai.evaluation import evaluate, GroundednessEvaluator, RelevanceEvaluator, CoherenceEvaluator
from azure.identity import DefaultAzureCredential
from azure.core.credentials import AzureKeyCredential
import os
from dotenv import load_dotenv

load_dotenv()

# Create test dataset (ground truth Q&A pairs)
test_data = [
    {
        "query": "What does MAS regulate?",
        "response": "MAS regulates financial institutions and monetary policy.",  # Expected answer
        "context": "Source documents about MAS regulations"
    },
    {
        "query": "What are the penalties for non-compliance?",
        "response": "Penalties include fines and license revocation.",
        "context": "Source documents about penalties"
    }
]

def run_advanced_evaluation():
    """Run Azure AI Evaluation"""
    
    foundry_endpoint = os.environ["FOUNDRY_ENDPOINT"]
    foundry_key = os.environ["FOUNDRY_KEY"]
    
    # Initialize evaluators
    evaluators = {
        "groundedness": GroundednessEvaluator(
            credential=AzureKeyCredential(foundry_key),
            azure_endpoint=foundry_endpoint
        ),
        "relevance": RelevanceEvaluator(
            credential=AzureKeyCredential(foundry_key),
            azure_endpoint=foundry_endpoint
        ),
        "coherence": CoherenceEvaluator(
            credential=AzureKeyCredential(foundry_key),
            azure_endpoint=foundry_endpoint
        )
    }
    
    # Run evaluation
    results = evaluate(
        data=test_data,
        evaluators=evaluators
    )
    
    print("Evaluation Results:")
    print(f"Groundedness Score: {results['groundedness']}")
    print(f"Relevance Score: {results['relevance']}")
    print(f"Coherence Score: {results['coherence']}")

if __name__ == "__main__":
    run_advanced_evaluation()
```

**Note:** Advanced evaluation requires additional Azure AI services setup.

---

### Evaluation Metrics Explained

**1. Groundedness (0-5 score)**
- Does the answer use ONLY information from sources?
- Score 5 = Fully grounded, no hallucinations
- Score 1 = Makes up facts

**2. Relevance (0-5 score)**
- Is the answer relevant to the question?
- Score 5 = Directly answers question
- Score 1 = Off-topic

**3. Coherence (0-5 score)**
- Is the answer well-structured and readable?
- Score 5 = Clear and coherent
- Score 1 = Confusing or broken

**4. Citation Accuracy**
- Are sources correctly cited?
- Can you find the info in cited documents?

---

### Trust Checklist

**Before trusting your RAG system in production:**

- [ ] Tested with 20+ known Q&A pairs (>90% accuracy)
- [ ] Verified it refuses to answer when it doesn't know
- [ ] Checked citations - info is actually in cited sources
- [ ] No hallucinations detected in sample tests
- [ ] Answers are coherent and well-structured
- [ ] Response time is acceptable (<5 seconds)
- [ ] Cost per query is within budget

**For POC:** Run `evaluate_rag.py` and verify 3/3 tests pass!

---

---

## 🎨 Phase 7: Build a Web UI with Streamlit (Optional)

Want a ChatGPT-like interface instead of command line? Add Streamlit!

### Step 7.1: Install Streamlit

```bash
pip install streamlit
```

---

### Step 7.2: Create Streamlit App

**File 8: `app.py`**

```python
"""
Streamlit Web UI for RAG Chat
Simple ChatGPT-like interface
"""

import streamlit as st
from chat_with_knowledge import chat_with_rag
import sys
from io import StringIO

# Page config
st.set_page_config(
    page_title="RAG Knowledge Assistant",
    page_icon="📚",
    layout="centered"
)

st.title("📚 RAG Knowledge Assistant")
st.caption("Ask questions about your documents and websites")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask a question about your knowledge base..."):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get assistant response
    with st.chat_message("assistant"):
        with st.spinner("Searching knowledge base..."):
            try:
                # Capture print output from chat_with_rag
                old_stdout = sys.stdout
                sys.stdout = StringIO()
                
                # Get response (sources hidden in UI, we'll show them separately)
                response = chat_with_rag(prompt, show_sources=False)
                
                # Restore stdout
                sys.stdout = old_stdout
                
                # Display response
                st.markdown(response)
                
                # Store in history
                st.session_state.messages.append({"role": "assistant", "content": response})
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
                sys.stdout = old_stdout

# Sidebar with info
with st.sidebar:
    st.header("About")
    st.write("This RAG system searches through:")
    st.write("📄 Your ADLS documents")
    st.write("🌐 Indexed websites")
    
    st.header("Stats")
    st.metric("Chat History", len(st.session_state.messages) // 2)
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
    
    st.header("Tips")
    st.info("Ask specific questions for best results!")
```

---

### Step 7.3: Run the Web UI

```bash
streamlit run app.py
```

**Opens in browser automatically!**

URL: http://localhost:8501

---

### Step 7.4: Using the UI

**Interface includes:**
- 💬 Chat input box at bottom
- 📜 Scrollable chat history
- 🔄 Clear history button in sidebar
- 📊 Message counter

**Try it:**
1. Type: "What regulations are mentioned?"
2. Press Enter
3. Get instant answer with sources!

**To stop:**
- Press `Ctrl + C` in terminal

---

### Advanced: Deploy to Cloud (Optional)

**Want to share with team?**

**Option A: Streamlit Cloud (Free)**
1. Push code to GitHub
2. Go to share.streamlit.io
3. Connect repo
4. Deploy!

**Option B: Azure Container Instances**
```bash
# Create Dockerfile
# Deploy to Azure
# Get public URL
```

---

### Streamlit Features You Can Add

**1. File Upload:**
```python
uploaded_file = st.file_uploader("Upload a document to add to knowledge base")
if uploaded_file:
    # Process and index the file
    st.success("Document added!")
```

**2. Source Display:**
```python
with st.expander("View Sources"):
    st.write("📄 Document 1: filename.pdf")
    st.write("🌐 Website 1: example.com")
```

**3. Settings:**
```python
with st.sidebar:
    st.header("Settings")
    num_sources = st.slider("Number of sources", 1, 10, 5)
```

**4. Export Chat:**
```python
if st.button("Export Chat"):
    chat_text = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages])
    st.download_button("Download", chat_text, "chat.txt")
```

---

## ☁️ Phase 8: Deploy to Cloud (Share with Team)

Want your team to access the app? Deploy it to the cloud!

### 📊 Deployment Options Comparison

| Feature | Streamlit Cloud | Azure Container Instances | Azure App Service |
|---------|----------------|--------------------------|-------------------|
| **Cost** | FREE | ~$15/month | ~$55/month |
| **Setup Time** | 10 minutes | 30 minutes | 45 minutes |
| **Difficulty** | Easy | Medium | Medium |
| **Custom Domain** | ❌ | ⚠️ Manual | ✅ Built-in |
| **SSL/HTTPS** | ✅ Free | ⚠️ Manual | ✅ Free |
| **Authentication** | ❌ | ⚠️ Manual | ✅ Azure AD |
| **Auto-scaling** | ⚠️ Limited | ❌ | ✅ |
| **CI/CD** | ✅ GitHub | ⚠️ Manual | ✅ GitHub |
| **Best For** | Quick demos | Team testing | Production |

---

### Option 1: Streamlit Cloud (Easiest - FREE!)

**Perfect for:** Quick team sharing, demos, POCs
**Time:** 10 minutes
**Cost:** FREE

#### Step 1.1: Prepare Code for GitHub

**Create `.gitignore`:**
```bash
# .gitignore
.env
.venv/
__pycache__/
*.pyc
.DS_Store
scraped_content/
.playwright/
```

**Important: Choose the right requirements file**

You need TWO different requirements files:

**`requirements.txt` - For local development and one-time setup:**
```txt
# Full dependencies for setup and development
# Use this when setting up locally

# Azure AI packages
azure-ai-projects==1.0.0b10
azure-ai-inference[prompts]
azure-identity
azure-search-documents
azure-storage-blob

# Data processing
python-dotenv
pypdf

# Web scraping packages
beautifulsoup4
requests
playwright
lxml
html2text
aiohttp

# Web UI
streamlit
```

**What each package does:**
- `azure-ai-projects`: Creates search index schema (one-time: `create_search_index.py`)
- `azure-identity`: Azure CLI authentication during setup
- `azure-ai-inference`: Embeddings and chat completions
- `azure-search-documents`: Upload/search documents in index
- `azure-storage-blob`: Read files from ADLS
- `python-dotenv`: Load environment variables from .env
- `pypdf`: Extract text from PDF files
- `beautifulsoup4, requests, playwright, lxml, html2text, aiohttp`: Web scraping
- `streamlit`: Web UI

**`requirements-deploy.txt` - For cloud deployment (minimal):**
```txt
# Minimal dependencies for deployed Streamlit app
# Use this for Streamlit Cloud, Docker, Azure deployments

# Core app dependencies
streamlit==1.31.0
azure-ai-inference[prompts]==1.0.0b5
azure-search-documents==11.4.0
azure-storage-blob==12.19.0
python-dotenv==1.0.0
pypdf==3.17.0

# Web scraping (only if indexing websites)
beautifulsoup4==4.12.3
requests==2.31.0
playwright==1.41.0
lxml==5.1.0
html2text==2020.1.16
aiohttp==3.9.1
```

**Why minimal for deployment?**
- ✅ Faster deployment (smaller image)
- ✅ Lower memory usage
- ✅ Fewer security vulnerabilities
- ✅ Only what the app actually needs

**Even more minimal (if NOT using web scraping):**
```txt
# Bare minimum - files only, no websites
streamlit
azure-ai-inference[prompts]
azure-search-documents
azure-storage-blob
python-dotenv
pypdf
```

**Which to use when:**
```bash
# Local setup and indexing
pip install -r requirements.txt
python create_search_index.py
python index_all_sources.py

# Deployment
# Use requirements-deploy.txt in:
# - Dockerfile
# - Streamlit Cloud
# - Azure deployments
```

#### Step 1.2: Push to GitHub

```bash
# Initialize git
cd rag-poc
git init
git add .
git commit -m "Initial RAG POC with Streamlit"

# Create repo on GitHub
# Go to github.com/new and create "rag-poc" repo

# Push code
git remote add origin https://github.com/YOUR_USERNAME/rag-poc.git
git branch -M main
git push -u origin main
```

#### Step 1.3: Deploy to Streamlit Cloud

1. Go to https://share.streamlit.io
2. Click "Sign in" → Use GitHub account
3. Click "New app"
4. Fill in:
   - **Repository:** `YOUR_USERNAME/rag-poc`
   - **Branch:** `main`
   - **Main file path:** `app.py`

5. Click "Advanced settings"
6. Add secrets (paste these exactly):
   ```toml
   FOUNDRY_ENDPOINT = "https://regrep-sme-poc-resource.services.ai.azure.com/models"
   FOUNDRY_KEY = "your-foundry-key-here"
   AISEARCH_ENDPOINT = "https://aisearch-rag-regrep.search.windows.net"
   AISEARCH_KEY = "your-search-key-here"
   ADLS_ACCOUNT_NAME = "adlsragpoc"
   ADLS_ACCOUNT_KEY = "your-storage-key-here"
   ADLS_CONTAINER_NAME = "knowledge-base"
   AISEARCH_INDEX_NAME = "unified-knowledge-index"
   EMBEDDINGS_MODEL = "text-embedding-3-small"
   CHAT_MODEL = "gpt-5-mini"
   ```

7. Click "Deploy!"

#### Step 1.4: Share with Team

**Your app is live at:**
```
https://your-app-name.streamlit.app
```

**Share this URL with your team!**

**Features:**
- ✅ Automatically updates when you push to GitHub
- ✅ Free SSL certificate (HTTPS)
- ✅ No maintenance required
- ⚠️ Public URL (anyone with link can access)

---

### Option 2: Azure Container Instances (Recommended for Teams)

**Perfect for:** Private deployment, team access, Azure integration
**Time:** 30 minutes
**Cost:** ~$15/month

#### Step 2.1: Create Dockerfile

**File: `Dockerfile`**

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
# Using minimal requirements for deployment
COPY requirements-deploy.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers (only if using web scraping)
RUN pip install playwright && \
    playwright install chromium --with-deps

# Copy application files
COPY app.py .
COPY chat_with_knowledge.py .
COPY web_scraper.py .

# Expose Streamlit port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

**Note:** If you're NOT using web scraping, remove these lines:
```dockerfile
# Remove these 2 lines if no web scraping:
RUN pip install playwright && \
    playwright install chromium --with-deps
```

#### Step 2.2: Create `.dockerignore`

```
.venv/
__pycache__/
.env
*.pyc
.git/
.DS_Store
scraped_content/
.playwright/
```

#### Step 2.3: Deploy with Script

**File: `deploy_to_azure.sh`**

```bash
#!/bin/bash
set -e

echo "🚀 Deploying RAG POC to Azure Container Instances..."

# Load environment variables from .env
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
fi

# Configuration
RG="rg-rag-poc"
LOCATION="swedencentral"
REGISTRY="ragpocregistry"
APP_NAME="rag-poc-app"
DNS_LABEL="rag-poc-demo"

# Create container registry
echo "Creating Azure Container Registry..."
az acr create \
    --name $REGISTRY \
    --resource-group $RG \
    --location $LOCATION \
    --sku Basic

# Build and push image
echo "Building and pushing Docker image..."
az acr build \
    --registry $REGISTRY \
    --image rag-streamlit:latest \
    .

# Get ACR credentials
echo "Retrieving ACR credentials..."
ACR_USER=$(az acr credential show --name $REGISTRY --query username -o tsv)
ACR_PASS=$(az acr credential show --name $REGISTRY --query passwords[0].value -o tsv)

# Deploy to Azure Container Instances
echo "Deploying container..."
az container create \
    --name $APP_NAME \
    --resource-group $RG \
    --image $REGISTRY.azurecr.io/rag-streamlit:latest \
    --cpu 1 \
    --memory 2 \
    --registry-username $ACR_USER \
    --registry-password $ACR_PASS \
    --dns-name-label $DNS_LABEL \
    --ports 8501 \
    --location $LOCATION \
    --environment-variables \
        ADLS_ACCOUNT_NAME="$ADLS_ACCOUNT_NAME" \
        ADLS_CONTAINER_NAME="$ADLS_CONTAINER_NAME" \
        AISEARCH_INDEX_NAME="$AISEARCH_INDEX_NAME" \
        EMBEDDINGS_MODEL="$EMBEDDINGS_MODEL" \
        CHAT_MODEL="$CHAT_MODEL" \
    --secure-environment-variables \
        FOUNDRY_ENDPOINT="$FOUNDRY_ENDPOINT" \
        FOUNDRY_KEY="$FOUNDRY_KEY" \
        AISEARCH_ENDPOINT="$AISEARCH_ENDPOINT" \
        AISEARCH_KEY="$AISEARCH_KEY" \
        ADLS_ACCOUNT_KEY="$ADLS_ACCOUNT_KEY"

# Get public URL
echo ""
echo "Retrieving public URL..."
FQDN=$(az container show \
    --name $APP_NAME \
    --resource-group $RG \
    --query ipAddress.fqdn \
    --output tsv)

echo ""
echo "✅ Deployment complete!"
echo "🌐 Your app is available at: http://${FQDN}:8501"
echo ""
echo "📋 Share this URL with your team!"
echo ""
echo "💡 To update the app:"
echo "   1. Make changes to your code"
echo "   2. Run: ./deploy_to_azure.sh"
echo "   3. Container will be recreated automatically"
```

**Make it executable and run:**
```bash
chmod +x deploy_to_azure.sh
./deploy_to_azure.sh
```

**Your app URL:**
```
http://rag-poc-demo.swedencentral.azurecontainer.io:8501
```

**Pros:**
- ✅ Runs in your Azure subscription (private)
- ✅ Secrets managed securely
- ✅ Can restrict to Azure VNet
- ✅ Easy updates (just re-run script)

**To update:**
```bash
# Make code changes
./deploy_to_azure.sh  # Rebuilds and redeploys
```

---

### Option 3: Azure App Service (Production-Ready)

**Perfect for:** Production apps, custom domains, high availability
**Time:** 45 minutes
**Cost:** ~$55/month (B1 tier)

#### Step 3.1: Use Same Dockerfile from Option 2

#### Step 3.2: Deploy to App Service

```bash
#!/bin/bash
set -e

echo "🚀 Deploying to Azure App Service..."

# Configuration
RG="rg-rag-poc"
LOCATION="swedencentral"
REGISTRY="ragpocregistry"
PLAN="rag-poc-plan"
APP_NAME="rag-poc-app"

# Create ACR if not exists
az acr create \
    --name $REGISTRY \
    --resource-group $RG \
    --sku Basic \
    --location $LOCATION \
    2>/dev/null || true

# Build and push
az acr build \
    --registry $REGISTRY \
    --image rag-streamlit:latest \
    .

# Create App Service Plan
az appservice plan create \
    --name $PLAN \
    --resource-group $RG \
    --location $LOCATION \
    --is-linux \
    --sku B1

# Create Web App
az webapp create \
    --name $APP_NAME \
    --resource-group $RG \
    --plan $PLAN \
    --deployment-container-image-name $REGISTRY.azurecr.io/rag-streamlit:latest

# Configure container registry
ACR_USER=$(az acr credential show --name $REGISTRY --query username -o tsv)
ACR_PASS=$(az acr credential show --name $REGISTRY --query passwords[0].value -o tsv)

az webapp config container set \
    --name $APP_NAME \
    --resource-group $RG \
    --docker-custom-image-name $REGISTRY.azurecr.io/rag-streamlit:latest \
    --docker-registry-server-url https://$REGISTRY.azurecr.io \
    --docker-registry-server-user $ACR_USER \
    --docker-registry-server-password $ACR_PASS

# Configure environment variables
az webapp config appsettings set \
    --name $APP_NAME \
    --resource-group $RG \
    --settings \
        FOUNDRY_ENDPOINT="$FOUNDRY_ENDPOINT" \
        FOUNDRY_KEY="$FOUNDRY_KEY" \
        AISEARCH_ENDPOINT="$AISEARCH_ENDPOINT" \
        AISEARCH_KEY="$AISEARCH_KEY" \
        ADLS_ACCOUNT_NAME="$ADLS_ACCOUNT_NAME" \
        ADLS_ACCOUNT_KEY="$ADLS_ACCOUNT_KEY" \
        ADLS_CONTAINER_NAME="$ADLS_CONTAINER_NAME" \
        AISEARCH_INDEX_NAME="$AISEARCH_INDEX_NAME" \
        EMBEDDINGS_MODEL="$EMBEDDINGS_MODEL" \
        CHAT_MODEL="$CHAT_MODEL" \
        WEBSITES_PORT=8501

echo ""
echo "✅ Deployment complete!"
echo "🌐 Your app: https://${APP_NAME}.azurewebsites.net"
```

#### Step 3.3: (Optional) Add Custom Domain

```bash
# Add custom domain
az webapp config hostname add \
    --webapp-name rag-poc-app \
    --resource-group rg-rag-poc \
    --hostname rag.yourdomain.com

# Enable free SSL
az webapp config ssl bind \
    --name rag-poc-app \
    --resource-group rg-rag-poc \
    --certificate-thumbprint auto \
    --ssl-type SNI
```

#### Step 3.4: (Optional) Enable Azure AD Authentication

**Restrict access to your organization:**

1. Portal → App Services → rag-poc-app
2. Settings → Authentication
3. Add identity provider → Microsoft
4. Configure:
   - Tenant: Your organization
   - Restrict access: Require authentication
5. Save

Now only users in your Azure AD can access!

**Pros:**
- ✅ Production SLA (99.95%)
- ✅ Auto-scaling
- ✅ Custom domain + free SSL
- ✅ Azure AD authentication
- ✅ Application Insights monitoring
- ✅ Deployment slots (staging/production)

---

## 🔒 Security Best Practices

### For All Deployments:

**1. Never commit secrets to Git:**
```bash
# Check before committing
git status
# Make sure .env is NOT listed
```

**2. Use environment variables:**
- Streamlit Cloud: Use secrets UI
- Azure: Use App Settings (encrypted at rest)

**3. Rotate keys regularly:**
```bash
# Regenerate keys every 90 days
az search admin-key renew --resource-group rg-rag-poc --service-name aisearch-rag-regrep --key-kind primary
```

**4. Monitor access:**
- Azure: Enable Application Insights
- Streamlit: Check usage in dashboard

---

## 📊 Cost Summary

**Monthly costs by deployment option:**

| Option | Infrastructure | Total/Month |
|--------|---------------|-------------|
| **Streamlit Cloud** | FREE | $0 |
| **Container Instances** | $15 (container) | $15 |
| **App Service B1** | $55 (app service) | $55 |

**Plus shared costs (same for all):**
- AI Search Basic: $75/month
- Storage: ~$1/month
- Azure OpenAI: Pay per use (~$10-50/month)

**Total POC cost:**
- With Streamlit Cloud: ~$85/month
- With Container Instances: ~$100/month
- With App Service: ~$140/month

---

## 🚀 Recommended Deployment Path

**Phase 1: POC (Week 1)**
→ Use **Streamlit Cloud** (FREE, 10 minutes)
→ Share with immediate team for feedback

**Phase 2: Team Testing (Week 2-4)**
→ Deploy to **Azure Container Instances** ($15/month)
→ Restrict to company network
→ Gather feedback from broader team

**Phase 3: Production (Month 2+)**
→ Migrate to **Azure App Service** ($55/month)
→ Add custom domain, SSL, Azure AD
→ Enable monitoring and scaling

---

## 🔄 Update Workflow

**After deployment, to update your app:**

### Streamlit Cloud:
```bash
git add .
git commit -m "Updated chat UI"
git push
# App updates automatically in 2-3 minutes!
```

### Azure Container Instances:
```bash
./deploy_to_azure.sh
# Rebuilds and redeploys in ~5 minutes
```

### Azure App Service:
```bash
# Set up CI/CD with GitHub Actions (one-time)
az webapp deployment source config \
    --name rag-poc-app \
    --resource-group rg-rag-poc \
    --repo-url https://github.com/YOUR_USERNAME/rag-poc \
    --branch main

# Then just:
git push
# Auto-deploys in 3-5 minutes!
```

---

## 🤖 Phase 9: Automated Recreation Script (Bonus)

Want to quickly recreate everything after deleting it? This script automates 90% of the setup.

### File 9: `setup.sh`

```bash
#!/bin/bash
set -e

echo "🚀 Setting up RAG POC in Azure..."

# Configuration variables
RG="rg-rag-poc"
LOCATION="swedencentral"
STORAGE="adlsragpoc"
SEARCH="aisearch-rag-regrep"
OPENAI="openai-rag-regrep"
SUBSCRIPTION="58a263f1-4410-4cb7-83b7-c3dd6e1a0e41"

# Set subscription
echo "Setting subscription..."
az account set --subscription $SUBSCRIPTION

# Create resource group
echo "Creating resource group..."
az group create --name $RG --location $LOCATION

# Create storage account
echo "Creating storage account..."
az storage account create \
  --name $STORAGE \
  --resource-group $RG \
  --location $LOCATION \
  --sku Standard_LRS \
  --kind StorageV2

# Create container
echo "Creating storage container..."
STORAGE_KEY=$(az storage account keys list --resource-group $RG --account-name $STORAGE --query '[0].value' -o tsv)
az storage container create \
  --name knowledge-base \
  --account-name $STORAGE \
  --account-key $STORAGE_KEY

# Create AI Search
echo "Creating AI Search service..."
az search service create \
  --name $SEARCH \
  --resource-group $RG \
  --location $LOCATION \
  --sku basic

# Create Azure OpenAI
echo "Creating Azure OpenAI..."
az cognitiveservices account create \
  --name $OPENAI \
  --resource-group $RG \
  --location $LOCATION \
  --kind OpenAI \
  --sku S0 \
  --custom-domain $OPENAI

# Get all keys
echo "Retrieving API keys..."
STORAGE_KEY=$(az storage account keys list --resource-group $RG --account-name $STORAGE --query '[0].value' -o tsv)
SEARCH_KEY=$(az search admin-key show --resource-group $RG --service-name $SEARCH --query 'primaryKey' -o tsv)
OPENAI_KEY=$(az cognitiveservices account keys list --resource-group $RG --name $OPENAI --query 'key1' -o tsv)

# Auto-generate .env file
echo "Generating .env file..."
cat > .env << EOF
# Auto-generated by setup.sh on $(date)

# Azure AI Foundry Project Connection
AIPROJECT_CONNECTION_STRING=swedencentral.api.azureml.ms;$SUBSCRIPTION;$RG;regrep-sme-poc

# Azure AI Search
AISEARCH_ENDPOINT=https://$SEARCH.search.windows.net
AISEARCH_KEY=$SEARCH_KEY
AISEARCH_INDEX_NAME=unified-knowledge-index

# Azure AI Foundry Models
FOUNDRY_ENDPOINT=https://regrep-sme-poc-resource.services.ai.azure.com/models
FOUNDRY_KEY=<NEED-TO-GET-FROM-FOUNDRY-UI>

# ADLS Storage
ADLS_ACCOUNT_NAME=$STORAGE
ADLS_ACCOUNT_KEY=$STORAGE_KEY
ADLS_CONTAINER_NAME=knowledge-base

# Model Deployments
EMBEDDINGS_MODEL=text-embedding-3-small
CHAT_MODEL=gpt-5-mini

# Web Scraping Settings
WEB_SCRAPE_DELAY=2
WEB_MAX_PAGES_PER_SITE=50
WEB_USER_AGENT=Mozilla/5.0 (compatible; RAG-Bot/1.0)
EOF

echo ""
echo "✅ Infrastructure created and .env file generated!"
echo ""
echo "⚠️  Manual steps still required (5 minutes):"
echo ""
echo "1. Create Foundry Project:"
echo "   - Go to https://ai.azure.com"
echo "   - Click 'New project'"
echo "   - Name: regrep-sme-poc"
echo "   - Resource group: $RG"
echo "   - Region: Sweden Central"
echo ""
echo "2. Deploy Models in Foundry:"
echo "   - Build → Models → Deploy:"
echo "     • gpt-5-mini (50K TPM, Global Standard)"
echo "     • text-embedding-3-small (50K TPM, Global Standard)"
echo ""
echo "3. Get Foundry Key:"
echo "   - ai.azure.com → Project home → Copy API key"
echo "   - Update .env: FOUNDRY_KEY=<your-key>"
echo ""
echo "4. Upload Documents:"
echo "   - Portal → adlsragpoc → Containers → knowledge-base"
echo "   - Upload your PDFs/documents"
echo ""
echo "5. Run Indexing:"
echo "   python create_search_index.py"
echo "   python index_all_sources.py"
echo ""
echo "6. Test:"
echo "   python chat_with_knowledge.py --query \"What is MAS?\""
echo "   streamlit run app.py"
echo ""
echo "Total time: ~5-10 minutes for manual steps"
```

**Make it executable:**
```bash
chmod +x setup.sh
```

**Run it:**
```bash
./setup.sh
```

---

### What Gets Automated:

✅ Resource group creation
✅ Storage account + container
✅ AI Search service
✅ Azure OpenAI service
✅ All API keys retrieved automatically
✅ .env file auto-generated with keys

### What You Still Do Manually (5 minutes):

❌ Create Foundry project (UI only - no CLI yet)
❌ Deploy models in Foundry (UI only)  
❌ Get Foundry API key (UI only)
❌ Upload your documents to ADLS
❌ Run indexing scripts

**This is as automated as possible!** Foundry doesn't have CLI support yet, so those steps must be manual.

---

### Recreation Workflow:

**Tonight (cleanup):**
```bash
az group delete --name rg-rag-poc --yes
```
Deletes everything, stops all costs.

**Tomorrow (recreate in ~7 minutes):**
```bash
./setup.sh  # 2 minutes - fully automated
```
Then follow the 5 manual steps printed at the end (~5 minutes).

**Total time: ~7 minutes to get everything back!**

---

## 🧹 Cleanup (IMPORTANT!)

**When done testing, delete everything to stop costs:**

### Method 1: Delete Resource Group (Easiest)

**Azure Portal:**
1. Go to "Resource Groups"
2. Select `rg-rag-sweden`
3. Click "Delete resource group"
4. Type the name to confirm: `rg-rag-sweden`
5. Click "Delete"
6. Wait 5-10 minutes

**Or via CLI:**
```bash
az group delete --name rg-rag-sweden --yes --no-wait
```

**This deletes:**
- ✅ ADLS Storage
- ✅ AI Search (biggest cost!)
- ✅ Azure OpenAI
- ✅ Foundry Project
- ✅ Everything!

### Method 2: Delete Individually

If you want to keep some resources:

1. **Delete AI Search first** (biggest cost - $2.50/day)
2. Delete Azure OpenAI
3. Keep ADLS if needed (very cheap)

---

## 🎓 What You Learned

✅ **Azure AI Foundry** - Modern AI development platform
✅ **RAG Pattern** - Retrieval-Augmented Generation
✅ **GPT-5-mini** - Latest efficient language model
✅ **Vector Search** - Semantic search with embeddings
✅ **Web Scraping** - Ethical data collection
✅ **Multi-source Knowledge** - Files + Websites
✅ **Regional Deployment** - Data Zone Standard
✅ **Cost Management** - Azure budget alerts
✅ **Production Patterns** - Connection strings, authentication

---

## 📈 Next Steps

### Immediate Improvements:
1. **Better document parsing** - Use `pypdf2`, `python-docx`
2. **Semantic chunking** - Smart text splitting
3. **Conversation memory** - Multi-turn chats
4. **UI** - Build with Streamlit/Gradio
5. **Evaluation** - Azure AI evaluation tools

### Production Considerations:
1. **Security** - Managed Identity (not API keys)
2. **Monitoring** - Application Insights
3. **Cost optimization** - Right-sized resources
4. **CI/CD** - Automated deployment
5. **Data governance** - Access controls

### Advanced Features:
1. **Multi-modal** - Images in documents
2. **Real-time updates** - Change tracking
3. **Hybrid search** - Keyword + vector
4. **Citation extraction** - Exact quotes
5. **Agents** - Complex workflows

---

## 🐛 Troubleshooting

### "Insufficient quota" error
- ✅ Use Data Zone Standard (not Global Standard)
- ✅ Try different region (East US 2 as backup)
- ✅ Request quota increase (1-2 days)

### "No module named 'azure'"
```bash
# Reactivate venv and reinstall
pip install -r requirements.txt
```

### "Authentication failed"
```bash
az login
az account show
```

### "No documents indexed"
- Check files in ADLS container
- Verify `.env` has correct storage account name
- Check file permissions

### "No web content scraped"
- Test: `python web_scraper.py`
- Check robots.txt
- Verify URLs in `website_sources.txt`

---

## 📚 Resources

- **Azure AI Foundry**: https://learn.microsoft.com/azure/ai-foundry/
- **GPT-5 Models**: https://learn.microsoft.com/azure/ai-services/openai/concepts/models#gpt-5
- **Azure AI Search RAG**: https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview
- **Web Scraping Ethics**: https://www.robotstxt.org/
- **Azure Pricing Calculator**: https://azure.microsoft.com/pricing/calculator/

---

## ✅ Conclusion

**You've built a production-ready RAG system!**

- ✅ Uses latest GPT-5-mini in Sweden Central
- ✅ Combines internal docs + external websites
- ✅ Provides cited, grounded answers
- ✅ Optimized for latency from India (~150ms)
- ✅ Cost-effective for POC ($1-5 total)
- ✅ Follows Azure best practices

**Total time**: 3-4 hours
**Total cost**: $1-5 (with prompt deletion)
**Latency**: ~150ms from Bangalore

**🎉 Congratulations on building your first RAG system!**

---

**Questions? Issues?**
- Review troubleshooting section
- Check Azure AI Foundry docs
- Test components individually
- Remember to delete resources when done!

**Happy building! 🚀**
