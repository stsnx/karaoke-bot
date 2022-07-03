from pythainlp import romanize
from pythainlp.tokenize import word_tokenize
text = "เขาข้าวเค้าเข่า"
a=word_tokenize(text)
for i in a:
    print(romanize(i),end=' ')