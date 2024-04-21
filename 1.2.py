positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]

negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

def sentiment_tracker (pwords, words):
    x=0
    y=0
    i=0
    z=0
    for review in reviews:
        review = review.lower()
        z+=1
        for positive_word in pwords:
            if positive_word in review:
                x+=1
                #i+=1
                print(f"Positive word, {positive_word.upper()} found in review {z}.")
            else:
                i+=1
                continue
        for negative_word in words:
            if negative_word in review:
                #i+=1
                y+=1
                print(f"Negative word, {negative_word.upper()} found in review {z}.")
            else:
                continue
sentiment_tracker(positive_words, negative_words)
        