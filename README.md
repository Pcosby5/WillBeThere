# WillBeThere
# Django Authentication Server

## Stack Used
- **Language**: Python
- **Framework**: Django
- **Additional Libraries**: Django REST Framework


## Available Routes

- **/api/login**
  - **Method**: POST
  - **Description**: Endpoint for user login.
  - **Request Body**:
    ```
    {
	"username": "pcosby500",
    "password": "**********"
    }
    ```
  - **Response**:
    ```
    {
      "token": "example_token"
    }
    ```
  - **Authentication Required**: No

- **/api/register**
  - **Method**: POST
  - **Description**: Endpoint for user registration.
  - **Request Body**:
    ```
    {
	"username": "pcosby500",
    "password": "*********",
    "email": "example111@gmail.com",
    "first_name": "example111",
    "last_name": "example"
    }
    ```
  - **Response**:
    ```
    {
	"id": "12e26b03-472b-4dd9-874b-c2e0d1e714ee",
	"username": "pcosby500",
	"email": "example111@gmail.com",
	"first_name": "example111",
	"last_name": "example",
	"profile_image_url": null
    }
    ```
  - **Authentication Required**: No



- **/api/profile**
  - **Method**: GET
  - **Description**: Endpoint for getting user profile.
  - **Request Body**:
    ```
    {
	"Authorization": "Login Token",

    }
    ```
  - **Response**:
    ```
    {
	"id": "12e26b03-472b-4dd9-874b-c2e0d1e714ee",
	"username": "pcosby500",
	"email": "example111@gmail.com",
	"first_name": "example111",
	"last_name": "example",
	"profile_image_url": null
    }
    ```
  - **Authentication Required**: Yes









## Documentation for Available Routes

### /api/auth/login

- **Method**: POST
- **Description**: Endpoint for user login.
- **Request Body**:

