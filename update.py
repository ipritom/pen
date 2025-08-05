import os
import json
import re
import time
import requests
import os
import pathlib
from dotenv import load_dotenv
from datetime import datetime
from pprint import pprint

load_dotenv()
GITHUB_TOKEN = os.getenv('GIT_PAT')

AUTH_HEADER = {"Authorization": f"token {GITHUB_TOKEN}"}

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def extract_title_and_tags(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Extract title from the first line
    first_line = content.split('\n', 1)[0].strip()
    title = first_line.lstrip('#').strip()

    # Extract tags using a regular expression
    tags_match = re.search(r'<!--\s*\[([^\]]+)\]\s*-->', content)
    tags = tags_match.group(1).split(',') if tags_match else []

    return title, tags


def get_github_commit_info(file_name, markdown_path=None):
    if markdown_path is None:
        raise "Error"
    
    github_owner = 'ipritom'
    github_repo = 'pen'
    # makdown_path = 'blogs'

    url = f'https://api.github.com/repos/{github_owner}/{github_repo}/commits?path={markdown_path}/{file_name}'
    print(url)
    response = requests.get(url,headers=AUTH_HEADER)

    if response.status_code==200:
        return response.json()
    else:
        raise f"Error: for {file_name}"
    # pprint(response.json())

def process_markdown_folder(folder_path, output_json_path, newOnly:bool=False, except_this:list=[]):
    data = []

    # 1. read the existing metadata 
    # 3. fix 'created' field as datetime object
    # 2. create filename:position map
    temp_metadata = read_json(output_json_file)
    
    for elem in temp_metadata:
        elem['created'] = datetime.strptime(elem['created'], '%Y-%m-%dT%H:%M:%S%z')
    
    temp_metadata_map = {entry['filename']:i for i, entry in enumerate(temp_metadata)}

    # traversing files and update the metadata
    for filename in os.listdir(markdown_folder):
        if filename.endswith('.md'):
            # avoid api call for the existing/published articles
            if newOnly and filename not in except_this:
                if filename in temp_metadata_map:
                    data.append(temp_metadata[temp_metadata_map[filename]])
                    continue
            
            # fetch the github commit info
            content_info= get_github_commit_info(file_name=filename, markdown_path=folder_path)
            print(filename, markdown_folder)
            print(content_info)
            content_creation_date  = content_info[len(content_info)-1]["commit"]["author"]["date"]
            content_creation_date = datetime.strptime(content_creation_date, '%Y-%m-%dT%H:%M:%S%z')
            file_path = os.path.join(folder_path, filename)
            title, tags = extract_title_and_tags(file_path)
            data.append({'title': title, 'filename':filename, 'tags': tags, "created":content_creation_date})
  
  
    # Sort data based on the 'created_at' datetime
    data.sort(key=lambda x: x['created'] if x['created'] else datetime.min, reverse=True)

    # Custom JSON serializer for datetime objects
    def json_serializer(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError(f'Type not serializable: {type(obj)}')

    with open(output_json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2, ensure_ascii=False, default=json_serializer)

if __name__ == "__main__":
    
    # Replace 'path/to/markdown/folder' with the actual path to your folder containing markdown files
    # Replace 'output.json' with the desired name of the output JSON file

    # article type: blogs
    markdown_folder = "blogs"
    output_json_file = 'metadata/contents.json'
    
    # article type: silicon
    # markdown_folder = 'silicon'
    # output_json_file = "metadata/silicon_contents.json"

    s = time.time()
    process_markdown_folder(markdown_folder, output_json_file, newOnly=True)
    print("Process Finished | Time taken", (time.time()-s), "seconds")