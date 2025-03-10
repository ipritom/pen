# pen
This repo contains my writings 

## How to add tags
In the end of an article write tag as following. 
```
<!-- [test, philosophy, language] -->
```

## Update content list 

After writing a new article run `update.py`

## Automatic Publish
Just run the `publish.bat` file. 

## Configure metadata generation
Manipulate the following line in the `update.py`
```python
process_markdown_folder(markdown_folder, output_json_file, newOnly=False, except_this=['kukur.md'])

```

`newOnly=True` : will save time and reduce api hit
`except_this=[]`: includes list of existing contents `.md` to update metadata
