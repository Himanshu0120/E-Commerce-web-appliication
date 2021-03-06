# E-Commerce-web-appliication

This repository contains an E-Commerce website made using django backend and HTML/Bootstrap 
for frontend. This app has all the features that are required for any similar kind of application to work and these are-:

## Features
### Admin Control

* The admin has the control to add,remove or modify the products that are available.
* The admin can create or remove super users to control the app.
* The admin and superusers also have the responsibility to update the status for the products that have been ordered, as delivered or pending.

### Authentication and Authorization

* Any customer thst is not a superuser or admin is not authorized to change any product or any category or any such kind of activity.
* Login and Signup functionality is used to authenticate the customers.
* User cannot proceed to checkout or cannot view his order history without logging in and new users need to signup.

### Filtering 

* Products can be filterd on the basis of category of the product. 

### Cart and Order History

* Users can add products to cart and also can go to cart page to check the total price and quantity of items in their cart.
* After placing the order cart gets refreashed and all previous are removed.
* Logged in users can also view the order history where all the previous orders of that customer are shown.

### Snapshots 

![homePage image](https://github.com/Himanshu0120/E-Commerce-web-appliication/blob/master/ss/home.PNG)
![homePage image](https://github.com/Himanshu0120/E-Commerce-web-appliication/blob/master/ss/lgoin.PNG)
![Test Image](https://github.com/Himanshu0120/E-Commerce-web-appliication/blob/master/ss/cart.PNG)
![homePage image](https://github.com/Himanshu0120/E-Commerce-web-appliication/blob/master/ss/order.PNG)

### How to run

* Download or clone the repo.
* Download all the libraries listed in requirements.txt
* Goto the directory where the repo is saved and open CMD in that directory
* Run 'python manage.y runserver' .
* Open the lnik http://127.0.0.1:8000/ on your browser.
