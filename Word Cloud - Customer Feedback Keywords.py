# -*- coding: utf-8 -*-
"""
Created on Sun Aug 10 16:21:51 2025
@author: Abdullah
"""
import matplotlib.pyplot as plt
from wordcloud import WordCloud
reviews = [
    "Great service and fast delivery!",
    "The product quality is excellent.",
    "I had a wonderful shopping experience.",
    "Customer support was very helpful.",
    "Fast shipping and great prices.",
    "I love the variety of products available.",
    "The website is easy to navigate.",
    "I will definitely shop here again!",
    "The delivery was delayed, but the product is good.",
    "Excellent customer service!",
]
text = ' '.join(reviews)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
