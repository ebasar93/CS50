CREATE TABLE got(
    "sentence_id",
    "character_no",
    "length"
);

INSERT INTO GOT ("sentence_id", "character_no", "length")
VALUES
(14,98,4),
(114,3,5),
(618,72,9),
(630,7,3),
(932,12,5),
(2230,50,7),
(2346,44,10),
(3041,14,5);

CREATE VIEW cipher AS
SELECT "sentence", "character_no", "length" FROM got
LEFT JOIN sentences ON "sentences"."id" = "got"."sentence_id"   ;

CREATE VIEW am AS
SELECT substr("sentence", "character_no", "length") AS "phrase" FROM "cipher";

CREATE VIEW message AS
SELECT group_concat("phrase",(" ")) AS "phrase" from am ;
