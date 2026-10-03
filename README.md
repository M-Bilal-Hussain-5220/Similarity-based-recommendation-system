# AI Recommendation System
## Description

This is a simple AI recommendation system developed using Python as part of the DecodeLabs internship Project 3.

The system takes user interests as input, matches them with tags assigned to different courses and projects, and recommends the most relevant items based on **Jaccard similarity**.

## Features

* Takes user interests as comma-separated input
* Cleans and processes user input
* Matches user interests with item tags
* Calculates similarity using Jaccard similarity
* Sorts recommendations by similarity score
* Displays the top 5 recommended items
* Shows matched interests for each recommendation
* Allows the user to exit the system using `exit`

## Technologies Used

* Python
* Sets
* Functions
* Jaccard Similarity
* Basic Recommendation System Logic

## How It Works

The system compares the user's interests with the tags of each item.

Jaccard similarity is calculated using:

```text
Similarity = Common Interests / Total Unique Interests
```

The items with the highest similarity scores are displayed first.

## How to Run

Make sure Python is installed, then run:

```bash
python recommendation_system.py
```

Enter your interests separated by commas, for example:

```text
Python, AI, machine learning
```

The system will then display the most relevant recommendations.

## Project Type

DecodeLabs Artificial Intelligence Internship — Project 3
