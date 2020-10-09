from docx import Document
import re

N = str(input())
n = str(input())
try:
    document = Document(N)
    lst = []
    for para in document.paragraphs:
        lst += re.split(r'[ ),]+', str(para.text))
    count = 0
    for i in lst:
        if i.lower() == n.lower():
            count += 1
    print(n+":", count)
except:
    print(n+":", 0)
