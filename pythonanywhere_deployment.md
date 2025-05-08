# Deploying Glossy to PythonAnywhere

This guide will walk you through deploying your Django Glossy e-commerce site to PythonAnywhere.

## Step 1: Create a PythonAnywhere Account

1. Go to [PythonAnywhere.com](https://www.pythonanywhere.com/) and sign up for an account
2. Choose the appropriate plan (you can start with a free account for testing)

## Step 2: Upload Your Code

### Option 1: Using Git (recommended)

1. From your PythonAnywhere dashboard, open a Bash console
2. Clone your repository:
   ```bash
   git clone https://github.com/yourusername/glossy.git
   ```
   If your code isn't on GitHub yet, you can upload it using option 2.

### Option 2: Upload a ZIP file

1. Create a ZIP file of your project:
   - On Windows, right-click the Glossy folder, select "Send to" > "Compressed (zipped) folder"
2. From your PythonAnywhere dashboard, upload the ZIP file
3. Open a Bash console and unzip the file:
   ```bash
   unzip glossy.zip -d glossy
   cd glossy
   ```

## Step 3: Set Up a Virtual Environment

In the Bash console:

```bash
cd glossy  # Make sure you're in your project directory
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Step 4: Create a Production .env File

Create a .env file in your project directory with production settings:

```bash
touch .env
nano .env
```

Add the following to the .env file:

```
DEBUG=False
SECRET_KEY=your_secure_secret_key_here
STRIPE_PUBLIC_KEY=your_stripe_public_key
STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_WH_SECRET=your_stripe_webhook_secret
PAYMENT_FEATURE_ENABLED=False
```

Press Ctrl+X, then Y to save and exit.

## Step 5: Collect Static Files

```bash
python manage.py collectstatic
```

## Step 6: Create and Configure the Web App

1. Go to the "Web" tab in your PythonAnywhere dashboard
2. Click "Add a new web app"
3. Select "Manual configuration" (not the Django option)
4. Select Python version (e.g., Python 3.10)

### Configure the Virtual Environment

In the "Virtualenv" section, enter the path to your virtual environment:
```
/home/yourusername/glossy/venv
```

### Configure WSGI File

Click on the WSGI configuration file link (e.g., `/var/www/yourusername_pythonanywhere_com_wsgi.py`)

Replace the content with:

```python
import os
import sys

# Add your project directory to the system path
path = '/home/yourusername/glossy'
if path not in sys.path:
    sys.path.append(path)

# Set environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'glossy.settings'

# Import Django's WSGI handler and get the application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

Click "Save" and return to the web app configuration.

### Configure Static Files

Add these mappings in the "Static files" section:

- URL: `/static/` - Directory: `/home/yourusername/glossy/staticfiles`
- URL: `/media/` - Directory: `/home/yourusername/glossy/media`

### Set Security Settings

Edit your .env file to include:
```
ALLOWED_HOSTS=yourusername.pythonanywhere.com
```

## Step 7: Initialize the Database

In the Bash console:

```bash
cd glossy
source venv/bin/activate
python manage.py migrate
python manage.py createsuperuser
```

Follow the prompts to create an admin user.

## Step 8: Reload and Test

1. Go back to the "Web" tab
2. Click the "Reload" button
3. Visit your site at `https://yourusername.pythonanywhere.com`

## Troubleshooting

If you encounter issues:
1. Check the error logs in the "Web" tab
2. Verify your ALLOWED_HOSTS setting includes your PythonAnywhere domain
3. Make sure DEBUG is set to False in production
4. Ensure your static files are properly collected and configured

## Updating Your Site

When you make changes to your code:

1. Upload or pull the new code to PythonAnywhere
2. In a Bash console:
   ```bash
   cd glossy
   source venv/bin/activate
   pip install -r requirements.txt  # If dependencies changed
   python manage.py migrate  # If models changed
   python manage.py collectstatic  # If static files changed
   ```
3. Reload your web app from the "Web" tab