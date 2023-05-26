# ResultsPostProcessor User Guide

## Table of Contents
- [Introduction](#introduction)
    - [About the Application](#about-the-application)
    - [System Requirements](#system-requirements)
    - [Installation Guide](#installation-guide)
    - [Overview of User Interface](#overview-of-user-interface)
- [Features & Functionality](#features--functionality)
    - [Average Minimum Principal Strain for Each Node](#average-minimum-principal-strain-for-each-node)
    - [Average Minimum Principal Strain & Minimum Femur Strength When Considering Each Node as Center Node](#average-minimum-principal-strain--minimum-femur-strength-when-considering-each-node-as-center-node)
- [Troubleshooting](#troubleshooting)
- [Updates & Version History](#updates--version-history)

## Introduction

### About the Application
The results processor is designed to streamline and mass-analyze the nodal results (of finite element analysis of a femur but could be used for many other purposes). The application is capable of processing and averaging nodal results (as each node contains results from several elements). This information (result of each node) could be fed back into the application to produce the average minimum principal strain and, subsequently, the Minimum Femur Strength when considering each node as the center node of a 3mm radius circle.

### System Requirements
The latest version of the application operates on Windows platforms, but it could be run on Linux using the Wine compatibility layer. Better Linux and MacOS compatibility are in development.

### Installation Guide
Download and run the ResultsPotProcessor.exe file from the [GitHub page](https://github.com/mafazsyed/ResultsPostProcessor). No installation is required.

### Overview of User Interface
Figure 1 shows the user interface of the application.

<img src="https://github.com/mafazsyed/ResultsPostProcessor/assets/120568449/a4994cec-8686-49de-9ec4-872b7a3aea17" width="500">

## Features & Functionality
The following results post processing features are available:
1. Determine the average Minimum Principal Strain (or any other value) for each node (from multiple values for each node).
2. Determine the average Minimum Principal Strain and Minimum Femur Strength (MFS) (or any other value) when considering each node as the center node of a 3mm radius circle.

The input file format for each function is outlined in their respective sections.

### Average Minimum Principal Strain for Each Node

#### Calculate Average Minimum Principal Strain for Each Node

To calculate the average minimum principal strain for each node (where each node has one or more result values), first specify the input folder with all files (TXT or any other text-editor format) containing the input nodal results data in the format specified below.

<img src="https://github.com/mafazsyed/ResultsPostProcessor/assets/120568449/8f250ad7-24e4-44f9-b66a-f67d96c16d87" width="500">

#### Input Nodal Results File Format

The input file should contain, on each line, the node number followed by its result (average minimum principal strain) value. An example is shown below:

<img src="https://github.com/mafazsyed/ResultsPostProcessor/assets/120568449/3acb7102-5840-4ebb-b94c-541a3cba6280" width="500">

Note that a heading should not be included, and the nodes do not have to be in chronological order. There is no limit on the number of nodes or on the number of files simultaneously processed (number of files in the input folder).

### Average Minimum Principal Strain & Minimum Femur Strength When Considering Each Node as Center Node

#### Calculate Average Minimum Principal Strain & Minimum Femur Strength When Considering Each Node as Center Node

To calculate the average minimum principal strain and Minimum Femur Strength, first specify the input folder with all files (TXT or any other text-editor format) containing the input nodal results and coordinate data in the format specified below.

<img src="https://github.com/mafazsyed/ResultsPostProcessor/assets/120568449/4443ddf2-a913-4811-a058-d8018ceaf633" width="500">

#### Input Nodal Results & Coordinates File Format

The input file should contain, on each line, the node number followed by its result (averaged minimum principal strain) and its coordinates. 

<img src="https://github.com/mafazsyed/ResultsPostProcessor/assets/120568449/9e0d9309-548c-4b83-992c-5c4112413a21" width="500">

Note that a heading should not be included, and the nodes do not have to be in chronological order. There is no limit on the number of nodes or on the number of files simultaneously processed (number of files in the input folder).

## Troubleshooting
The Windows Terminal/Shell window displays any errors encountered and prints relevant information depending on the task performed.

## Updates & Version History
- **Version 1.0.0:** Initial Release

- **Version 1.1.0:**
    - Updated graphical user interface to a modern style
    - Other user interface and quality of life updates
    - Fixed – the application’s features only worked when 28 files were in the input folder

- **Version 1.2.0 (In Development / Awaiting Release):**
    - The equation to calculate the MFS was fixed before, however, could now be chosen by the user
    - The radius to consider could be changed by the user now
    - Looking at options to add MacOS (and direct Linux instead of using Wine) compatibility
