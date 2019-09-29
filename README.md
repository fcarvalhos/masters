# Masters

##This repository contains the codes in Python 3.6.5 and R languages related to development of my masters' project.


The project consists in an data-driven evaluation of the problem solving strategy, tinkering, employed by undergraduate students in an introductory university course. 
Using Educational Data Mining this project aims to identify different students' tinkering levels and to assess how these strategies impact in the students' final marks.

The folders in this repository have the following content:

1. [Python Crawlers](https://github.com/fcarvalhos/masters/tree/master/Python%20Crawlers) contains the codes used to collect data from the moodle database and to collect data from local files.

1. [Code Processing](https://github.com/fcarvalhos/masters/tree/master/Codes%20processing) contains the codes used to create each data objects to e future analyzed, as well the necessary file to create an dataset based on the students' AST features

1. [Clustering](https://github.com/fcarvalhos/masters/tree/master/Clustering) folder contains the scripts in R language to apply Wards AHC and K-means clustering methodson the dataset and to assess the validity and quality of the clusters generated. This folder contais also the scripts used to generate Association Rules based on the Apriori algorithm
  1. [Preprocess](https://github.com/fcarvalhos/masters/tree/master/Clustering/preprocess) contains the scripts used to preprocess the data before the clustering steps









_PS:The codes were written as separated functions in order to meet the projects' needs. However, the integration between these functions should be trivial_
