from bs4 import BeautifulSoup
import requests
import re

track_list=[]
music_list={}
i=100

for j in range (1, 11):	

	url = 'http://pitchfork.com/features/staff-lists/9555-the-100-best-tracks-of-2014/%r' %j
	r= requests.get(url)
	

	soup = BeautifulSoup(r.text)

	#print (soup.prettify().encode("utf-8"))

	tracks = soup.find_all(class_="text year-end-review")

	track_list = []

	for l in range(0,len(tracks)):

		str_track = str(tracks[l])
		track_info = str_track.split('data-section-title=')
		track_info =track_info[1].split('id')
		track_list.append(track_info[0])

	

	for entry in track_list:
		artist_name = entry.split('. ')[1].split('-')[0]
		
		if '&quot;' in entry:
			song_name = entry.split('- &quot;')[1].split('&quot;')[0]
		else:
			song_name = entry.split('- "')[1].split('"')[0]
		 
		music_list[i] = {}
		music_list[i]['artist'] = artist_name
		music_list[i]['track'] = song_name

		i-=1

#print music_list
for i in range (1,101):
	print i, '.' , music_list[i]['artist'] , '--' , music_list[i]['track']