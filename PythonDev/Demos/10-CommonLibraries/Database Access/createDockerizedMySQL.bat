REM The following statement creates a Docker image for MySQL.
docker build -t mysqlimage .

REM The following statement starts a Docker container for MySQL.
docker run -d --name mysqlcontainer -p 3333:3306 mysqlimage

