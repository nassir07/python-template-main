# jira_cc_ingestion



## Description

The aim of this project is to collect data from Jira codecraft throught jira api, jira api- it is still applicable to any jira data collection.
A per-project configuration is used to set the fields to collect and how to parse them. Each jira project data is stored in a separate table.
Historical data is kept for the updated jira issues i.e. when a jira issue is updated between to runs a new row is inserted. The calls for jira API to get jira issues data are made in a way that only issues updated after the last run are loaded.

Sprint data collection for specific projects can be set in the configuration.   

A specific users list is collected, it is used to collect the list of users who are reporters in some specific jira projects.  

## Scope and sources  

Jira server : https://jira.cc.bmwgroup.net/   
Jira projects collected : IPBM, IPBD, Light Stack SP25, SWP, IPNDEV, IPNATH, CDC, ADBK25, PADV, CVDRVN, ORIONINIT  
Sprint data collected : IPNATH  

## Input & Output  

- In the config file, are set for each project to collect:
    - the name
    - output table name
    - fields to collect and the method to use for parsing


- Credentials are passed as arguments in each main module to run :
    - jira token 
    - sql server user 
    - sql server password

## How to run?
Main modules to run are located in the pipelines package
They can be run separetely and they expect 3 arguments :
    - jira token 
    - sql server user 
    - sql server password


## Steps and logic  

For issues data for a jira project :
- Connect to db
- Get the maximum update date stored in the table
- get issue from jira that were updated after the maximum update date stored using jql
- parse the data of these issues
- insert this new data

For sprint data for a jira project : 
- retrieve all boards id related to the project
- retrieve all sprints related to the retrieved boards
- parse sprint data
- drop create new table & insert new data






## Installation  
Having pipenv available and python 3.10, you van use : 'python -m pipenv install --ignore-pipfile --python'


## Project status 
Initial devolopment is completed. The Job is in use. Improvements or new projects to collect can be introduced. 
