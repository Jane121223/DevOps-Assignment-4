docker build -t service-a service-a
docker stop sa || true
docker rm sa || true
docker run -d --name sa -p 5001:5001 service-a
