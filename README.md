
# twitgram
A tweet generator that uses n-gram modeling to replicate a user's tweets. Final project for LING 165 @ SJSU

## Setup
For this project, I debated between a few different options : use Twitter's Developer API or manually parse the HTML of a profile and isolate the tweets' text using xpath.

First, I tried manually parsing the HTML of a profile and isolating the tweets' text using xpath. However, with this approach, it was difficult to filter out retweets since they were in the same kind of div class as a user's original tweets. Since retweets were not written by the target user, their inclusion would throw off the modeling of the user's language, so it was crucial that they be filtered out. Furthermore, because Twitter profiles utilize infinite scroll instead of pagination, I was limited to the results found on the first page, which was a very small amount of data to work with. Any tweets generated with this dataset would simply be already existing tweets. 

Next, I tried using Twitter's Developer API and their [searchtweets Python wrapper](https://github.com/twitterdev/search-tweets-python) to read tweets from a public Twitter account and save the output to a JSONL file. However, this approach had its own limitations. While I was able to filter out retweets with this image, because I was using the free tier, I was limited to a max of 50 API calls and a max 100 tweets per call (including retweets). This already isn't a large amount of data to work with, but once retweets were filtered out, this number dropped even more. For example, when testing on my personal Twitter account, the number dropped to only 72 tweets to work with.

I finally ended up using [Twint](https://github.com/twintproject/twint), a lightweight open-source Twitter scraping tool available as both CLI application and a Python module. Twint had all the features I was looking for: searching by user, filtering out retweets, and returning a large amount of data without worrying about hitting a limit. 

## Implementation
main.py is based off Dr. Koo's n-gram sonnet generation lab.
First, an overall corpus is created to hold all the tweets we are working with, as well as a dictionary to keep track of the n-grams and their respective frequencies. 
Next, each tweet is split into n-grams based off a user-specified value for n. A higher n produces more natural sounding tweets, but they are also more likely to already exist in the corpus. On the other hand, a lower n leads to more variance, but can often sound obviously synthesized.
These n-grams are then chained together so that the ending of a preceding n-gram overlaps with a following n-gram. 
Lastly, the chain of n-grams is converted to a string. 

## Results

## Conclusion
