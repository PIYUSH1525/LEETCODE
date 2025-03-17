SELECT 
firstName,lastName,city,state 
FROM 
Person p
LEFT JOIN Address ON  p.personID=Address.personId;