from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(title, topic, rating):
	new_article = knowledge(title=title, topic= topic, rating= rating)
   	session.add(new_article)
   	session.commit()





	

def query_all_articles():
	articles = session.query(
    	Knowledge).all()
   	return articles


print(query_all_articles())


def query_article_by_topic(topic):
	article = session.query(Knowledge).filter_by(
		topic=topic).first()
	return article
print(query_article_by_topic("An Enslish rock-band"))

def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(
		topic=topic).delete()
	session.commit()
delete_article_by_topic("Wow, Another English rock-band :|")

def delete_all_articles():
	pass

def edit_article_rating():
	pass
