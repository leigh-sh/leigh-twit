DROP TABLE IF EXISTS USER;
CREATE TABLE USER (
  user_id INTEGER PRIMARY KEY autoincrement,
  user_name text NOT NULL
);

DROP TABLE IF EXISTS follower;
CREATE TABLE follower (
  following_id INTEGER,
  follower_id INTEGER
);

DROP TABLE IF EXISTS post;
CREATE TABLE message (
  post_id INTEGER PRIMARY KEY autoincrement,
  puslisher_id INTEGER NOT NULL,
  text text NOT NULL,
  date_published INTEGER
);
