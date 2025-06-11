-- Common SQL Queries for Flight Management System

-- 1. Select all flights
SELECT * FROM FlightInfo;

-- 2. Search flight by ID
SELECT * FROM FlightInfo WHERE FlightID = 101;

-- 3. Find flights by origin
SELECT * FROM FlightInfo WHERE FlightOrigin = 'New York';

-- 4. Find flights by destination
SELECT * FROM FlightInfo WHERE FlightDestination = 'London';

-- 5. Find flights by status
SELECT * FROM FlightInfo WHERE Status = 'On Time';

-- 6. Count flights by status
SELECT Status, COUNT(*) as FlightCount 
FROM FlightInfo 
GROUP BY Status;

-- 7. Find all delayed flights
SELECT * FROM FlightInfo WHERE Status = 'Delayed';

-- 8. Find flights between specific origins and destinations
SELECT * FROM FlightInfo 
WHERE FlightOrigin = 'New York' AND FlightDestination = 'London';

-- 9. Update flight status
UPDATE FlightInfo 
SET Status = 'Departed' 
WHERE FlightID = 101;

-- 10. Delete a specific flight
DELETE FROM FlightInfo WHERE FlightID = 101;

-- 11. Find flights with origins starting with specific letter
SELECT * FROM FlightInfo WHERE FlightOrigin LIKE 'N%';

-- 12. Count total number of flights
SELECT COUNT(*) as TotalFlights FROM FlightInfo;
