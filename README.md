# wiki-offline

## Overview
This converts Wikipedia html into txt which makes it able to read offline.

Text file will be made and open at the same time right after calling `convertWikiToText(url: str)`.

## Tutorial (how to make the wiki-offline by myself)
* <a href="https://yjg30737.github.io/posts/python-how-to-get-wikipedia-text/">See the post</a>

## Setup
`python -m pip install git+https://github.com/yjg30737/wiki-offline.git --upgrade`

## Usage
```python
from wiki_offline import convertWikiToText

convertWikiToText('https://en.m.wikipedia.org/wiki/Banjo')
```

## Preview
Application below which is being used for preview is Windows Notepad.

![image](https://user-images.githubusercontent.com/55078043/176660545-d847c4d7-fa2d-4432-8d66-4fad2befb4bb.png)
