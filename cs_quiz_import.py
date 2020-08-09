import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://postgres:pk8742@localhost:5432/QuizHub')
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open('cs_quiz.csv')
    reader = csv.reader(f)
    for question,a,b,c,d,answer in reader:
        db.execute('INSERT INTO "QuizBox_cs_quiz"(question,a,b,c,d,answer) VALUES(:question,:a,:b,:c,:d,:answer)',{"question":question,"a":a,"b":b,"c":c,"d":d,"answer":answer})

        print(f"Added  question")

    db.commit()

if __name__ == '__main__':
    main()
