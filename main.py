import json

with open('icons.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

icons = data['icons']

def dict2str(data:dict) -> str:
    return json.dumps(data)

def dict2url(data:dict) -> str:
    url_format = 'https://img.shields.io/badge/-{}-{}?style=flat-square&logo={}&logoColor=FFFFFF'
    name = data['title'].replace(' ', '%20')
    color = data['hex']
    logo = data['slug']
    return url_format.format(name, color, logo)

def query_icon(query:str) -> list:
    result = []
    for icon in icons:
        if query.lower() in dict2str(icon).lower():
            result.append(icon)
    return result

def generate_markdown(result:list) -> str:
    markdown = '# Simple Icons\n\n'
    markdown += '| Name | Icon | URL |\n'
    markdown += '| ---- | ---- | --- |\n'
    for icon in result:
        name = icon['title']
        url = dict2url(icon)
        markdown += '| {} | ![{}]({}) | `{}` |\n'.format(name, name, url, url)
    return markdown

def main():
    query = input('Enter the name of the icon you want to search: ')
    result = query_icon(query)
    markdown = generate_markdown(result)
    
    with open('result.md', 'w', encoding='utf-8') as f:
        f.write(markdown)
    print('The result has been saved to result.md')

if __name__ == '__main__':
    main()
