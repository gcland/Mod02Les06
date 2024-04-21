python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]
def keyword_search (i):
    for string in python_reviews:
        string = string.lower()
        for word in keyword_list:
            if word in string:
                print(f"Reviews mention, {word.upper()}.")


keyword_list = ['good', 'excellent', 'bad', 'poor', 'average']
keyword_search(keyword_list)
#Could add ability to input keyword items and append those items to the keyword_list (starting from 0 items in list).