# Predicting Cherry Blossom Full Bloom Timing in Japan: Geographic Location and Initial Flowering Date Enable Two-Day Accurate
Forecasts

## Overview

This repository contains an analysis of cherry blossom blooming patterns across Japan using historical flowering data. It investigates how geographical and climatic factors influence the duration between initial flowering and full bloom of cherry blossoms. The analysis employs a mixed effects linear regression model to predict bloom progression using data from 100 monitoring stations between 1953-2019. The repository includes scripts for data download and cleaning, model development, statistical analysis, and visualization. The analysis is fully reproducible, with all necessary data and code provided. The findings aim to help improve the accuracy of cherry blossom viewing period predictions, which has implications for tourism planning and cultural celebrations in Japan.


## File Structure

The repo is structured as:

-   `data/01-raw_data` contains the raw data as obtained from X.
-   `data/02-analysis_data` contains the cleaned dataset that was constructed.
-   `models` contains the fitted model. 
-   `other` contains details about LLM chat interactions.
-   `paper` contains the files used to generate the paper, including the Quarto document and reference bibliography file, as well as the PDF of the paper. 
-   `scripts` contains the Python scripts used to download data, clean and process the data, perform exploratory data analysis, create and train the model, and evaluate the model's performance.


## Statement on LLM usage

Aspects of the code were written with the help of the auto-complete tool, JetBrains AI. Claude was used to assist with Python code development, including package management, data import processes, and troubleshooting table formatting in Quarto documents. The entire chat history is available in `other/llm_usage.txt`.

