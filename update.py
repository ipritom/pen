import os
import json
import re
import time
import requests
from datetime import datetime
from pprint import pprint
from dataclasses import dataclass

# @dataclass
# class ContentInfo:
    

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


def get_github_commit_info(file_name):
    github_owner = 'ipritom'
    github_repo = 'pen'
    makdown_path = 'blogs'


    url = f'https://api.github.com/repos/{github_owner}/{github_repo}/commits?path={makdown_path}/{file_name}'
    response = requests.get(url)
    if response.status_code==200:
        return response.json()
    else:
        raise f"Error: for {file_name}"
    # pprint(response.json())

def process_markdown_folder(folder_path, output_json_path):
    data = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):
            content_info= get_github_commit_info(file_name=filename)
            content_creation_date  = content_info[len(content_info)-1]["commit"]["author"]["date"]
            file_path = os.path.join(folder_path, filename)
            title, tags = extract_title_and_tags(file_path)
            data.append({'title': title, 'tags': tags, "created":content_creation_date})

    with open(output_json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    
    # Replace 'path/to/markdown/folder' with the actual path to your folder containing markdown files
        
    markdown_folder = 'blogs'

    # Replace 'output.json' with the desired name of the output JSON file
    output_json_file = 'metadata/contents.json'

    s = time.time()
    process_markdown_folder(markdown_folder, output_json_file)
    print("Process Finished | Time taken", (time.time()-s), "seconds")