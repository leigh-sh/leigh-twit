DROP TABLE IF EXISTS Users;
CREATE TABLE Users (
  user_id INTEGER PRIMARY KEY autoincrement,
  user_name text NOT NULL
);

DROP TABLE IF EXISTS follow;
CREATE TABLE Follow (
  followed_id INTEGER,
  follower_id INTEGER
);

DROP TABLE IF EXISTS Tweets;
CREATE TABLE Tweets (
  tweet_id INTEGER PRIMARY KEY autoincrement,
  tweed text NOT NULL,
  author INTEGER NOT NULL
);
