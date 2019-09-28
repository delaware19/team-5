BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "User" (
	"USER_NAME"	TEXT UNIQUE,
	"PASSWORD"	INTEGER,
	"IS_ADMIN"	INTEGER,
	PRIMARY KEY("USER_NAME")
);
CREATE TABLE IF NOT EXISTS "Text" (
	"STORY_ID"	TEXT,
	"TEXT_CAPTIONS"	TEXT
);
CREATE TABLE IF NOT EXISTS "Image" (
	"IMAGE_ID"	TEXT,
	"IMAGE"	BLOB,
	PRIMARY KEY("IMAGE_ID")
);
CREATE TABLE IF NOT EXISTS "Story" (
	"NAME"	TEXT,
	"AGE"	INTEGER,
	"GENDER"	NUMERIC,
	"STORY_ID"	TEXT,
	"TYPE_OF_VISIT"	TEXT,
	"IMAGE_LIST"	TEXT,
	PRIMARY KEY("STORY_ID")
);
INSERT INTO "User" VALUES ('admin','password',1);
INSERT INTO "User" VALUES ('peasant','password',0);
INSERT INTO "Text" VALUES ('Ryan40','This is caption 1 ### this is caption 2 ###');
INSERT INTO "Text" VALUES ('Bonnie191','caption 3');
INSERT INTO "Text" VALUES ('Diane211','this is caption 4 ### this is caption 5 ###');
INSERT INTO "Text" VALUES ('Ian30','this is caption 6');
INSERT INTO "Text" VALUES ('John100','this is caption 7 ### this is caption 8 ###');
INSERT INTO "Image" VALUES ('test1
','this is image 1');
INSERT INTO "Image" VALUES ('test2','this is image 2');
INSERT INTO "Story" VALUES ('John',10,0,'John100','X-Ray','test1, test2');
INSERT INTO "Story" VALUES ('Ryan',4,0,'Ryan40','ER','test1, test2');
INSERT INTO "Story" VALUES ('Ian
',3,0,'Ian30','Check in','test1, test2');
INSERT INTO "Story" VALUES ('Diane',21,1,'Diane211','Other','test1, test2');
INSERT INTO "Story" VALUES ('Bonnie',19,1,'Bonnie191','Blood Work','test1, test2');
COMMIT;
