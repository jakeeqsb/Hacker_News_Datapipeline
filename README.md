# Hacker_News_Datapipeline
Summary:
A ,simple and DAG based, data pipeline filtering, cleaning, aggregating, summarizing json data from Hacker News.
This project is a guided project from Dataquest.io 


![screen shot 2018-01-22 at 4 54 20 pm](https://user-images.githubusercontent.com/10664813/35252373-02d5cdea-ff95-11e7-9822-fb4f933896fb.png)

#### file_to_json: loads 'hn_stories_2014.json' file into a dictionary and return it
#### filter_stories: return a generator of filtering popular stories that have more than 50 points, more than 1 comment, and do not begin with 'Ask HN'
#### json_to_csv: build a virtual csv file and put the transformed json data onto the file
#### extract_titles: returns of every Hacer News story title
#### clean_titles : get rid of punctuation and transform each title into lower case and then return it
#### build_keyword_dictionary: return a dictionary of the word frequency in a title
#### top_keywords : sort the result from build_keyword_dictionary decreasing order then return first 100 results.

