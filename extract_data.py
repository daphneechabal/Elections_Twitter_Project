import json

with open('daphnee.json', 'w') as file:
    for i in range(len(tweets_data)): #for i, tweet in enumerate(tweets_data):
        twt = {}
        userId = tweets_data[i]['user']['id'] #twt['id'] = tweet['id']
        userLocation = tweets_data[i]['user']['location']
        userFriendsCount = tweets_data[i]['user']['friends_count']
        hashtags = tweets_data[i]['entities']['hashtags']
        placeType = None if tweets_data[i]['place'] == None else tweets_data[i]['place']['place_type']
        quotedStatusText = tweet['quoted_status']['text'] if 'quoted_status' in tweet else None
        twt['quoted_status'] = {'text':quotedStatusText}
        twt['in_reply_to_status_id'] = tweet['in_reply_to_status_id']
        twt['text'] =  tweets_data[i]['text']
        twt['lang'] =  tweets_data[i]['lang']
        twt['user'] = {'id':userId, 'location':userLocation, 'friends_count':userFriendsCount}
        twt['entities'] = {'hashtags':hashtags}
        twt['place'] = {'place_type':placeType}
        file.write(json.dumps(twt) + '\n')
