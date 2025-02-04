SELECT "city", COUNT("type") FROM schools WHERE "type" = 'Public School' GROUP BY "city" ORDER BY COUNT("type") DESC, "name" LIMIT 10 ;

-- SELECT "name", COUNT("type") FROM schools GROUP BY "city" HAVING "type" = 'Public School' ORDER BY COUNT("type") DESC, "name" LIMIT 10
-- Charter olan sehirler publicden saymadi, ayrimi ilk anda yapmak lazimmis
