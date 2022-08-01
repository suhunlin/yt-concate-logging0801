import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
LOGS = 'logs'
OUTPUTS = 'outputs'
DOWNLOADS = 'downloads'
VIDEOS = os.path.join(DOWNLOADS, 'videos')
CAPTIONS = os.path.join(DOWNLOADS, 'captions')
