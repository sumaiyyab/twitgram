import searchtweets as st
import json
import sys

def loadTweets (user):
	print('Loading tweets from ' + user + '...')
	search_args = st.load_credentials("twitter_keys.yaml",
									yaml_key="search_tweets_api",
									env_overwrite=False)

	rule = st.gen_rule_payload("from:"+user, 
							results_per_call=100,
							from_date="2020-04-18",
							to_date="2020-05-18"
							)

	rs = st.ResultStream(rule_payload=rule,
						max_results=100,
						**search_args)

	results = list(rs.stream())
	with open(user+'Twts.jsonl', 'w', encoding='utf-8') as f:
		for tweet in results:
			json.dump(tweet, f)
			f.write('\n')
	print('done - ' + str(len(results)) + " tweets saved")