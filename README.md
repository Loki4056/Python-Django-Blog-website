# Python-Django-Blog-website

## Description
This is a blog website built with Python and Django. It includes user login functionality, an admin login that manages user logins, and the content that needs to be posted on the website.

## Features
- **User Login**: Users can create an account, log in, and log out. Users can also update their profile and password.
- **Admin Login**: Admins can manage user accounts, including creating, updating, and deleting users.
- **Blog Posts**: admin can create, update, and the users delete their own blog posts. All users can view all posts.

## Installation
1. Clone this repository: `git clone https://github.com/Loki4056/Python-Django-Blog-Website.git`
2. Navigate to the project directory: `cd Python-Django-Blog-Website`
3. create a new virtual environment in terminal using: python -m venv venv
4. Then activate the virtual Environment using: venv/scripts/activate 
5. Install the requirements: `pip install -r requirements.txt` 

##**Next step is importatnt todo for the project to run properly**

##**Next step is importatnt todo for the project to run properly**

6. Then we need to create localhost key and certificate to run the project in HTTPS://
    for that follow the below steps:

  1.Install OpenSSL:
    If you don't have OpenSSL installed, you can download it from the OpenSSL website (https://www.openssl.org/source/) or use a package manager for your operating     system to install it.

  2.Generate a Private Key:
       Open a command prompt or terminal and navigate to the directory where you want to generate the key and certificate.
        Run the following command to generate a private key file (e.g., localhost.key):
        `openssl genpkey -algorithm RSA -out localhost.key`
        You can specify the key size and algorithm as needed. The above command generates a 2048-bit RSA private key.

  3.Generate a Certificate Signing Request (CSR):
        Next, you need to create a Certificate Signing Request (CSR). The CSR contains information about the entity requesting the certificate (in this case, localhost).
        Run the following command:
        `openssl req -new -key localhost.key -out localhost.csr`
        This command will prompt you to enter information about your organization. You can enter "localhost" for the "Common Name" field. You can leave other fields empty or with placeholder values for development purposes.

  4.Generate a Self-Signed Certificate:
        Now, use the CSR to generate a self-signed certificate:
        `openssl x509 -req -in localhost.csr -signkey localhost.key -out localhost.crt`
        This command generates a self-signed certificate (localhost.crt) using the private key and CSR.
        
  5.After generating the key and certificate place it in the same folder where the manage.py file is saved and run the server 

7. Run the server: `python manage.py runserver_plus --cert localhost.crt --key localhost.key`

## Usage
1. Open your web browser and navigate to `http://127.0.0.1:8000/`.
2. Use the navigation links to access the different features of the website.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
