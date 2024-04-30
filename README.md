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




- **/api/users**
  - **Method**: GET
  - **Description**: Endpoint for getting all users.
  - **Request Body**:
    ```
    {
	"Authorization": "null",

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
    },
    {
		"id": "2d80e331-9ca3-4148-9451-d4cd29c58252",
		"username": "maydan",
		"email": "",
		"first_name": "Maydan",
		"last_name": "Technology",
		"profile_image_url": null
	},
	{
		"id": "26c1e4c1-2f32-4d72-b204-686d308ca4d8",
		"username": "Emmanuel",
		"email": "hemazyn65@gmail.com",
		"first_name": "",
		"last_name": "",
		"profile_image_url": null
	},
	{
		"id": "bc97592a-4a7b-4515-9644-0ed997fd5539",
		"username": "qwert",
		"email": "djoshuaadeyemi1@gmail.com",
		"first_name": "",
		"last_name": "",
		"profile_image_url": null
	},
	{
		"id": "7d43b4df-f7f2-48b5-b5e4-6ed2638672d7",
		"username": "Tofunmi",
		"email": "iamemmanuel234@gmail.com",
		"first_name": "",
		"last_name": "",
		"profile_image_url": null
	},
    ```
  - **Authentication Required**: No




- **/api/users/user_id/**
  - **Method**: GET
  - **Description**: Endpoint for getting a particular user.
  - **Request Body**:
    ```
    {
	"Authorization": "null",

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








## Documentation for Available Routes

### /api/auth/login

- **Method**: POST
- **Description**: Endpoint for user login.
- **Request Body**:

