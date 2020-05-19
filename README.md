
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

## Result Examples
```
C:\Users\sumaiyya\school\20spring\ling165\proj>python main.py lilnasx 3
CRITICAL:root:twint.output:checkData:copyrightedTweet
[+] Finished: Successfully collected 400 Tweets from @lilnasx.
Working with 399 tweets as input
False    ma... i missed the... school bus again 🥺 👉🏾👈🏾 👟🧦
False    never think that i want lady gaga to hop on
True     this kinda flow
False    i have to be disrespected like this
False    1 year ago today.. ahhh what a time
True     nope most of them aren’t going on either lol
True     thank you ny ❤️
False    i can do to help with the phrase he said in this song
True     dm
False    did i will create a multiverse through my music videos. which is why i’m a new person in each one of u some money to go get some food then stay inside.
True     sent $190 🧥👢
True     what changed
False    one a few of these still love the ones that didn’t tho
True     omg i llove him
True     i have headphones on i’m sorry
8/15 tweets generated are real tweets (0.5333333333333333)
```

```
C:\Users\sumaiyya\school\20spring\ling165\proj>python main.py aoc 4
[+] Finished: Successfully collected 400 Tweets from @aoc.
Working with 400 tweets as input
False    My mom works an hourly job. This is personal to me.
False    Yep! I rent, borrow, and thrift my clothes. (It’s also environmentally sustainable!) 🌎 The Post is just mad that you can do right now if you’ve been financially impacted is call ALL your bill providers & ask to defer your April payment. Phone bill, mortgage, credit cards, student loans - many are doing so, but you *must* contact them.
True     My heart breaks for your family. I am so very sorry for your loss, and our prayers are with your family.
True     Ann Arbor, let’s do this! 🇺🇸🗳
False    Look who’s talking about showing up for work! The woman didn’t hold a press conference for months while holding a job as press sec. If you’re so supportive of this admin’s plan, why don’t you go out and try delivering groceries for a living w/o health insurance or mass testing?
False    I deal w/ a lot of people to work. Climate transition, edu expansion w/ apprenticeships & colleges, M4A. These are jobs bills.
False    Over 20 million people have lost their jobs since COVID-19 hit the US. Not one deserves to be frightened about eviction or foreclosure during a pandemic. Join us in 10 mins to rally for an Essential Workers Bill of Rights! 💪🏽
False    It is admittedly hard to see those who care about civility + toxicity (which I understand) sit in silence about the disturbing antisemitism emerging around Sen. Sanders. A pundit also compared him to a disease on national TV. It’s disturbing. If you care, please care everywhere.
False    The best way to thank our essential workers is to support PPE production, fully funding our healthcare system, produce mass testing and contact tracing, and forgive student loan debt in the US. This is an unprecedented crisis. The Federal gov has the power to guarantee healthcare, housing, & basic income. Yet conservative officials are resisting doing the bare minimum to save lives. He didn’t.
False    Coronavirus tips! In addition to washing your hands, make sure you are also wiping down: - Doorknobs 🚪 - Light switches 💡 - Your cell phone 🤳🏼 - Arm rests 💺 - Car/bike handles 🚲🚗 - & anything your hands touch regularly! 🤝 A spray or cleaner works fine. 🧽 Be well!
False    To clarify, $1200 checks are ONLY going to some w/social sec numbers, NOT immigrants w/ tax IDs (ITINs). Thanks to GOP, these checks will be cut off the backs of *taxpaying immigrants,* who get nothing. Many are essential workers who pay more taxes than Amazon. Wall St gets $4T
False    I find it amusing that GOPers stalk my livestreams to obsess over any & every word, bc I’m *actually available* to constituent Qs at 10pm after a long day. Meanwhile, many GOP electeds hide from constituents & avoid town halls. Maybe that’s why they’re so preoccupied w/ mine 💁🏽‍♀️
False    I have always believed that real change happens not with a panel or task force, but in everyday people organizing mass movements to demand change. Yet we should also commit to showing up everywhere- every space where there are decisions made, the people must have a voice.
True     Grassroots supporter @lexibenavides made it
True     First up: as many of you saw yesterday, Katie Porter did a masterful job in Oversight to get the (hesitant) CDC to commit to FREE testing on Coronavirus ⬇️
False    Starting in 5 MINS: Who’s getting a $1200 check? What do UI benefits look like if you were just pressured into it last year. This is basic. The truth matters.
False    As governor, Pence’s science denial contributed to one of the worst HIV outbreaks in Indiana’s history. He is not a moderate. She just plays one on TV.
False    Did you know you can organize your building, block or neighborhood for #COVID to help others & keep people safe? It’s called Mutual Aid. Join me + legendary organizer Mariame Kaba TOMORROW as we walk through the steps of supporting others safely. RSVP: http://act.ocasiocortez.com/signup/mutual-aid …
False    Govs: Extended stay-at-home orders cannot be successful without issuing mortgage, rent, + debt moratoriums to go with them. Many people are going out bc they are panicked about paying bills due next wk on the 1st. Payment suspensions keep ppl indoors. Bills bring them outside.
False    Govs: Extended stay-at-home orders cannot be successful without issuing mortgage, rent, + debt moratoriums to go with them. Many people are going out bc they are panicked about paying bills due next wk on the 1st. Payment suspensions keep ppl indoors. Bills bring them outside.
4/20 tweets generated are real tweets (0.2)
```

## Conclusion
One of the biggest obstacles in this project was having a sufficient amount of data, and even the length of the tweets ended up playing a difference. Users who tweet more formally such as @AOC might have a more easy to replicate style, unlike users who tweet more erratically or have shorters tweets such as @LilNasX or @Cher. 
I still feel there are some issues with the sythesizer recognizing sentences that already exist in the corpus since some of @AOC's results look a bit too good to be true, but the results for a 4-gram did tend to skew on the more natural-sounding side. 
