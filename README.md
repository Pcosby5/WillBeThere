# WillBeThere
# Django Authentication Server

## Stack Used
- **Language**: Python
- **Framework**: Django
- **Additional Libraries**: Django REST Framework


## Available Routes

- **/api/auth/login**
  - **Method**: POST
  - **Description**: Endpoint for user login.
  - **Request Body**:
    ```
    {
      "username": "pcosby50",
      "password": "example111"
    }
    ```
  - **Response**:
    ```
    {
      "token": "example_token"
    }
    ```
  - **Authentication Required**: No

- **/api/auth/register**
  - **Method**: POST
  - **Description**: Endpoint for user registration.
  - **Request Body**:
    ```
    {
      "username": "pcosby50",
      "password": "example111"
      "email": "example111@gmail.com"
      "first_name": "example111"
      "last_name": "example"
    }
    ```
  - **Response**:
    ```
    {
      "username": "pcosby50",
      "password": "example111"
      "email": "example111@gmail.com"
      "first_name": "example111"
      "last_name": "example"
    }
    ```
  - **Authentication Required**: No



- **/api/auth/password/reset**
  - **Method**: POST
  - **Description**: Endpoint for resetting user password.
  - ...








## Documentation for Available Routes

### /api/auth/login

- **Method**: POST
- **Description**: Endpoint for user login.
- **Request Body**:

