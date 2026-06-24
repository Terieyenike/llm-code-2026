#!/usr/bin/env python
# coding: utf-8

# In[9]:


import frontmatter

with open('fm.md', 'r', encoding='utf-8') as f:
    post = frontmatter.load(f)

print(post.metadata['title'])
print(post.metadata['tags']) 


# In[10]:


print(post.content)


# In[11]:


post.to_dict()


# In[5]:


import io
import zipfile
import requests
import frontmatter

from IPython.display import Markdown, display


# In[74]:


url = 'https://codeload.github.com/DataTalksClub/faq/zip/refs/heads/main'
resp = requests.get(url)


# In[65]:


repository_data = []

# Create a ZipFile object from the downloaded content
zf = zipfile.ZipFile(io.BytesIO(resp.content))


# In[34]:


for file_info in zf.infolist():
    filename = file_info.filename.lower()

    # Only process markdown files
    if not filename.endswith('.md'):
        continue

    # Read and parse each file
    with zf.open(file_info) as f_in:
        content = f_in.read()
        post = frontmatter.loads(content)
        data = post.to_dict()
        data['filename'] = filename
        repository_data.append(data)

zf.close()


# In[23]:


repository_data


# In[24]:


display(Markdown(repository_data[0]['content']))


# In[17]:


print(repository_data[1])


# In[1]:


import io
import zipfile
import requests
import frontmatter

def read_repo_data(repo_owner, repo_name):
    """
    Download and parse all markdown files from a GitHub repository.

    Args:
        repo_owner: GitHub username or organization
        repo_name: Repository name

    Returns:
        List of dictionaries containing file content and metadata
    """
    prefix = 'https://codeload.github.com'
    url = f'{prefix}/{repo_owner}/{repo_name}/zip/refs/heads/main'
    resp = requests.get(url)

    if resp.status_code != 200:
        raise Exception(f"Failed to download repository: {resp.status_code}")

    repository_data = []
    zf = zipfile.ZipFile(io.BytesIO(resp.content))

    for file_info in zf.infolist():
        filename = file_info.filename
        filename_lower = filename.lower()

        if not (filename_lower.endswith('.md')
            or filename_lower.endswith('.mdx')):
            continue

        try:
            with zf.open(file_info) as f_in:
                content = f_in.read().decode('utf-8', errors='ignore')
                post = frontmatter.loads(content)
                data = post.to_dict()
                data['filename'] = filename
                repository_data.append(data)
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            continue

    zf.close()
    return repository_data


# In[2]:


dtc_faq = read_repo_data('DataTalksClub', 'faq')
evidently_docs = read_repo_data('evidentlyai', 'docs')

print(f"FAQ documents: {len(dtc_faq)}")
print(f"Evidently documents: {len(evidently_docs)}")


# In[7]:


dtc_faq


# In[11]:


display(Markdown(dtc_faq[0]['content']))

