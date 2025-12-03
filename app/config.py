import os
from fastapi.templating import Jinja2Templates

# Get the directory of the current file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Set the directory for templates
template_dir = os.path.join(BASE_DIR, 'templates')
templates = Jinja2Templates(directory=template_dir)