# Code-for-ICS-NAD-Dataset
## Paper
ICS-NAD: A Dataset Collected in Multiple Real-World Industrial Control Systems for Network Attack Detection (CAC 2025)    
A dataset collected in real-world industrial control systems for network attack detection (Scientific Data 2026)
## Cite
https://doi.org/10.1038/s41597-026-06738-x
## Abstract 
In the context of Industry 4.0, Industrial Control Systems (ICSs) are undergoing a significant transition from physical isolation to partial openness. While this shift enhances operational efficiency and integration, it also exposes ICSs to increasing network attacks. Effective intrusion detection methods rely on high-quality ICS datasets, yet existing options remain limited in scope, diversity, and realism. To address this gap, we introduce ICS-NAD, a dataset collected in real-world ICS scenarios with three well-known ICS brands. It contains two attack traffic sample patterns and covers 20 common ICS attack types. Through feature extraction and labeling, the ICS-NAD dataset provides 60 features with complete labels. We validate its utility using 10 machine learning and deep learning classification models. The dataset comprises 245.96 GB data files, including raw ICS network traffic (in PCAP format) and extracted features with labels (in CSV format). It is publicly available on the website to support ICS network attack detection research in academic and engineering contexts.
## Source Code Usage
There are three groups of code for processing the PCAP files of the ICS-NAD datset.
First, using the feature extraction codes provided by Chenyu Wang, you can extract 60 features from PCAP files of the dataset, and get corresponding CSV files.
Second, using the labeling codes provided by Shen Wang and Chengxi Tao, you can label all the records in the CSV files.   
Last, there are ten ML and DL models provided by Zihao Cheng for model training and dataset evaluation.
