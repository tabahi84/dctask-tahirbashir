# Democrance - Task
This repo is created to demonstrate task execution and completion as part of hiring process.


## Task Details
This task comprised of 4 Steps.
- Customer creation and verification.
- Quote/Policy generation and listing.
- Search implementation based on name, year and policy
- Authentication mechanism suggestion for customers & agents

> [!NOTE]  
> All aforementioned tasks have been completed and ready for review.

## Setup
### 1. Clone Repository
```
git clone https://github.com/tabahi84/dctask-tahirbashir
cd dctask-tahirbashir
```

### 2-a. Run via Virtual-Environment (Conda)
```
conda create -n envDCTask python=3.10
conda activate envDCTask
pip install -r requirements.txt
cd insurance_system
python manage.py migrate
python manage.py runserver
```

OR

### 2-b. Run via Docker [Preferable]
```
docker compose build
docker compose -d up
```

### 3. Modes of Access
Once code is running, DJango application will be available on [localhost:8000](http://localhost:8000)

#### 3-a. AdminPanel
URL: http://localhost:8000/admin
```
username: admin
password: admin123
```
![Admin-Login-Page](__README-MEDIA__/Admin-Login.png)

#### 3-b. SwaggerUI [Preferable]
URL: http://localhost:8000/docs
![SwaggerUI](__README-MEDIA__/SwaggerUI.png)

#### 3-c. DJango Views
URL: http://localhost:8000/api/v1/create_customer
![DJango-View-CreateCustomer](__README-MEDIA__/DJango-Create-Customer.png)

URL: http://localhost:8000/api/v1/quote
![DJango-View-Quote](__README-MEDIA__/DJango-Quote.png)



