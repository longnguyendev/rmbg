import os
import time
import schedule
from datetime import datetime, timedelta

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')

def cleanup_files():
    now = datetime.now()
    for filename in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.isfile(file_path):
            file_modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            if now - file_modified_time > timedelta(minutes=30):
                os.remove(file_path)
                print(f'Removed {file_path}')

schedule.every(30).minutes.do(cleanup_files)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)