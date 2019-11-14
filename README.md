# Fake User Handling Demo
``` Details
This repository includes a functional UI testing for an application consists of tasks like generating fake users 
based on facebook.com register template. fake.db includes 1000 fake users to be used for registering to facebook.com
``` 

# User information structure
``` python
  "first_name": self.generator.first_name(),
  "last_name": self.generator.last_name(),
  "sex": sex,
  "mail": self.generator.free_email(),
  "password": self.generator.password(),
  "birth_date": self.generator.date_of_birth(),
  "tel": self.generator.phone_number(),
  "image": self.generator.image_url()
```

## Python Project
``` Python projects 
- userhandling
``` 

## Technology Stack
- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [Faker](https://github.com/joke2k/faker)
- [sqlite3](https://www.sqlite.org/download.html)
- [GIT](https://git-scm.com/downloads)


## Test Steps
``` Test Steps 
3. A/T Populate FB register with 1000 users,
4. Test FB login validation for all CRUD.
``` 


## Deployment
``` Deployment 
1. Clone the repository to deploy on your system.
``` 

## Author

* **Ali Pala** - *See the all repositories* - [Github Repo](https://github.com/alipala)

