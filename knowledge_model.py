from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

		__tablename__ = 'English Rock Bands'
		article_id = Column(Integer, primary_key=True)
		title = Column(String)
		topic = Column(String)
		rating = Column(Integer)

		def __repr__(self):
			 return ("If you want to learn about {},"
			 		 "you should look at the Wikipedia article called {}. "
					"We gave this article a rating of {} out of 10!").format(self.topic, self.title, self.rating)
		    return ("Title: {}\n"
	               "Topic: {} \n"
	               "Rating: {}").format(
	                    self.title,
	                    self.topic,
	                    self.rating)

article1 = Knowledge(title = "King Crimson",  topic= "An Enslish rock-band" , rating= 10) 
print(article1)

article2 = Knowledge(title="Led Zeppelin", topic= "Another English rock-band", rating= 9)
print(article2)

article3 = Knowledge(title=  "Black Sbbath", topic= "Wow, Another English rock-band :|", rating= 8)
print(article3)
