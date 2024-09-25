# Remove Follow Requests Script

A Python script to remove pending follow requests on a social media platform.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)


## Introduction

The `remove_follow_requests.py` script is designed to automate the process of removing pending follow requests on a social media platform. It can be useful for managing your followers and keeping your account clean.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/remove-follow-requests.git


2. Download chromwebdriver 

    Latest Version will be available in https://getwebdriver.com/chromedriver#stable


## USAGE

1. Download Meta Data Of your Account 

Login Into Ur Account and Navigate into : https://accountscenter.instagram.com/info_and_permissions/

Request a download of  all available information about your account 
In a few hours you'll receive an email prompting you to download the data 
Download it and Proceed to unzip it into a folder in which the script will be 

2. Replace the chromwebdriver path with your path 

chromedriver_path = "path_to_webdriver.exe"

3. Next launch the usernames_into_json file while updating  

Line : with open('pending_follow_requests.json', 'r') as file:
    data = json.load(file)

pending_follow_requests.json must be changed with the path into the file that's in 
Downloads\instagram-"username"-2024-09-24-p333JIDx\connections\followers_and_following

4. Launch the Script and log into ur account to proceed to the automatic deletion of the pending follow request 


