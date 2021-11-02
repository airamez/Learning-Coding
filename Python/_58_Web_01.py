# Extrating all URL from a Web Page and saving to a file

from urllib.request import urlopen  # Module to access URL
import re  # Module for RegEx

regex = r'(https?://[^\s]+)'  # RegEx to match an URL

urls = list()
with urlopen('https://www.cnn.com/') as response:
    for line in response:
        line = line.decode('utf-8')
        urlsFound = re.findall(regex, line)
        for url in urlsFound:
            urls.append(url)

file = open('urls_from_cnn.txt', 'w+')
for url in urls:
    file.write(f'{url}\n')
file.close()

'''
Practices: 
Create a new program do recusivelly keep requesting all recovered URL
ATTENTION: Pay attention for potential risks
'''