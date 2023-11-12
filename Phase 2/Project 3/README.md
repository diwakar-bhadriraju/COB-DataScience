# Netflix Dataset Analysis

## Overview

This project involves analyzing a Netflix dataset using Python and popular data analysis libraries such as pandas, seaborn, and matplotlib. The dataset includes information about shows and movies available on Netflix, covering aspects like release years, types (Movie/TV Show), ratings, countries, and genres.

## Dataset

The dataset, named `netflix.csv`, is loaded into a Pandas DataFrame. It includes the following columns:

- **show_id:** Unique identifier for each show or movie.
- **type:** Indicates whether it's a Movie or TV Show.
- **title:** Title of the show or movie.
- **director:** Director(s) of the show or movie.
- **country:** Country or countries where the show or movie is available.
- **date_added:** Date when the show or movie was added to Netflix.
- **release_year:** Year when the show or movie was released.
- **rating:** Viewer rating of the show or movie.
- **duration:** Duration of the show or movie.
- **listed_in:** Categories or genres the show or movie belongs to.

## Project Structure

- **analyze_netflix.ipynb:** Jupyter Notebook containing Python code for exploring and visualizing the Netflix dataset.

## Requirements

Ensure you have the required Python libraries installed:

```bash
pip install pandas seaborn matplotlib
