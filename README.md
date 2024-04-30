# WillBeThere
# Django Authentication Server

## Stack Used
- **Language**: Python
- **Framework**: Django
- **Additional Libraries**: Django REST Framework

## Base-Url
https://will-be-there-auth-server.onrender.com/


## Documentation for Available Routes

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






- **/api/change-password**
  - **Method**: POST
  - **Description**: Endpoint for changing a user password if they remember the password.
  - **Request Body**:
    ```
    {

	"current_password": "Do******",
	"new_password": "Gif******",
	"confirm_new_password": "Gif******"

    }
    ```
  - **Response**:
    ```
    {
	"detail": "Password has been changed successfully."
    }
    ```
  - **Authentication Required**: Yes





- **/google/login/**
  - **Method**: POST
  - **Description**: Endpoint for signing up as a google account user.
  - **Request Body**:
    ```
    {

	"Authorization": "null"

    }
    ```
  - **Response**:
    ```
    {
	"continue to google"
    }
    ```
  - **Authentication Required**: No






- **/api/forgot-password**
  - **Method**: POST
  - **Description**: Endpoint for changing a user password if they do not remember the password.
  - **Request Body**:
    ```
    {
	"email":
		"domprehtabitha@gmail.com"

    }
    ```
  - **Response**:
    ```
    {
	"detail": "Password reset email has been sent.",
    "new_password": "set new password.",
    "confirm_password": "set new password.",
    }
    ```
  - **Authentication Required**: Yes





- **/api/logout**
  - **Method**: POST
  - **Description**: Endpoint for logging out user.
  - **Request Body**:
    ```
    {
	"Authorization":
		"token"

    }
    ```
  - **Response**:
    ```
    {
	"detail": "Logout succesfull or success 200 ok message.",

    }
    ```
  - **Authentication Required**: Yes




- **/api/users/delete**
  - **Method**: POST
  - **Description**: Endpoint for deleting out user.
  - **Request Body**:
    ```
    {
	"Authorization":
		"token"

    }
    ```
  - **Response**:
    ```
    {
	"detail": "delete success or success 200 ok message.",

    }
    ```
  - **Authentication Required**: Yes




- **/api/users/update**
  - **Method**: POST
  - **Description**: Endpoint for updating user.
  - **Request Body**:
    ```
    {
	"Authorization":
		"token"

    }
    ```
  - **Response**:
    ```
    {
	"id": "12e26b03-472b-4dd9-874b-c2e0d1e714ee",
	"username": "pcosby500",
	"email": "domprehtabitha@gmail.com",
	"first_name": "example111",
	"last_name": "example",
	"profile_image_url": null
    }
    ```
  - **Authentication Required**: Yes



## User- Auth
Login User - https://will-be-there-auth-server.onrender.com/api/login/ <br>
Register user - https://will-be-there-auth-server.onrender.com/api/register/ <br>
Logout user - https://will-be-there-auth-server.onrender.com/api/logout/ <br>
Google login - https://will-be-there-auth-server.onrender.com/accounts/google/login/ <br>
Change-password - https://will-be-there-auth-server.onrender.com/api/change-password/ <br>
Forgot-password - https://will-be-there-auth-server.onrender.com/api/forgot-password/ <br>

## User management and Details
User-update - https://will-be-there-auth-server.onrender.com/api/users/update/ <br>
User-delete - https://will-be-there-auth-server.onrender.com/api/users/delete/ <br>
Get all users - https://will-be-there-auth-server.onrender.com/api/users/ <br>
Get Users by User id - https://will-be-there-auth-server.onrender.com/api/users/user_id/ <br>


