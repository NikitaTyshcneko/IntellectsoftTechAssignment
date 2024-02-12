**Copy code**
```
git clone https://github.com/NikitaTyshcneko/IntellectsoftTechAssignment.git
```
**Install dependencies:**
```
pip install -r requirements.txt
```
**Apply migrations:**
```
python manage.py makemigrations
python manage.py migrate
```
**Run the Django development server:**
```
python manage.py runserver
```
**API Endpoints**

api/v1/auth/login - login 

api/v1/logout - logout

GET /api/v1/clients/: Retrieve clients.

POST /api/v1/clients/: Add a new client.

PUT /api/v1/clients/: Update client.

DELETE /api/v1/clients/: Delete client.

GET /api/v1/requests/: Retrieve requests.

POST /api/v1/requests/: Add a new request.

PUT /api/v1/requests/: Update request.

DELETE /api/v1/requests/: Delete request.

GET /api/v1/docs/: Swagger documentation.

**Testing**
```
pytest
```
**Dockerization** 
The application is containerized using Docker for easy deployment and scalability. Use the provided Dockerfile to build the Docker image.
```
docker-compose up --build
``` 
