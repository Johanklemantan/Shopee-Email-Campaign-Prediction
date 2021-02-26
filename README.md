# Final-Project-JCDS-0506-BDG-Widagdo-Johan-Klemantan
This is the final project for JCDS 0506 BDG Program about Email Classification

## Background
Sending email is one of the alternatives used by Shopee to tell and promote certain event sale to users. With the ability to be able to predict whether user is reading or not reading the email, enable Shopee to evaluate their crew works during campaign period until event launch. This is because, when user is open the email, the possibility of that user know there is an event or promo will be highly increased and also increasing the possibility of that user do transaction during event period. Therefore, with the making of this model, hopefully Shopee able to build a strategy for future marketing.

__Source__ : <a href='https://www.kaggle.com/davydev/shopee-code-league-20/tasks?taskId=1574'>Kaggle</a>


## Goals
The goals of this project is to build model that able to predict whether user is going to read the email sent by Shopee. In this case, Shopee's priority is user.



## Data Used
- 18 columns and 73539 rows for train data
- 6 columns and 127886 rows for user data

## Train Data Information
1. country_code = Code Number of Country in Shopee's user
1. grass_date = Date when the email was sent
1. user_id = Unique number each user
1. subject_line_length = Character Length for subject of email sent
1. last_open_day = How many days this user last open his email
1. last_login_day = How many days this user last open his Shopee account
1. last_checkout_day = How many days this user last checkout at his Shopee account
1. open_count_last_[10/30/60]_ days = Total email that open during N days
1. login_count_last_[10/30/60]_ days = Total times this user open his Shopee account during N days
1. checkout_count_last_[10/30/60]_ days = Total times this checkout from his Shopee account during N days
1. open_flag = __Target Variable__ Whether this user open his email or not
1. row_id = Row number 

## User Data Information
1. user_id = Unique number each user
1. attr_[1/2] = General attribute each user. Boolean type
1. attr_3 = General attribute each user. Int type
1. age = age of the user
1. domain = domain email of each user

# Result

## After searching the least Total Loss, found the most fitted model is :
1. Logistic Regression with Benchamrk and Threshold 0.49
1. Saved money = 290 million Rupiah/month (only for Shopee user in Indonesia)
1. Unnecessary Email 14.11 %
1. Loss Potential Customer 4.01 %
1. Total Loss 34.18 %

# Dashboard

## Home
<img src='../static/dashboardhome.png'>

## Business Problem Visualization
<img src='../static/dashboardvisualization.png'>

## Prediction
<img src='../static/dashboardprediction.png'>

## Results
<img src='../static/dashboardresult.png'>

<center>
  Thank You for Your Attention :)
  </center>
