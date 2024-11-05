# Linguistic-Preservation-Project

This project is designed to gather, analyze, and visualize data on endangered languages and cultural practices across the Americas. Using prompt engineering and linguistic data, this project aims to support conservation efforts by providing a comprehensive dataset on linguistic diversity, cultural attributes, and preservation risk levels. The data will be displayed in an interactive dashboard using Tableau Public, helping researchers, conservationists, and communities prioritize language and cultural preservation efforts.

## Project Overview

The goal is to create a data-driven tool that collects structured linguistic and cultural data for each language and culture in the Americas. This includes:
- Detailed linguistic features (phonology, syntax, morphology)
- Cultural practices and traditional knowledge
- Geographic information with latitude and longitude for mapping
- Endangerment risk levels and revitalization efforts
- Historical context and notable events

The project uses OpenAI's API to generate structured insights and categorizes data to create a robust dataset. The resulting dataset is visualized in Tableau Public.

## Features

- **Comprehensive Data Collection**: Collects linguistic and cultural information from diverse regions and languages.
- **Risk Level Assessment**: Provides risk levels for each language based on factors like population of speakers and conservation efforts.
- **Prompt-Generated Insights**: Uses prompt engineering to request detailed linguistic, cultural, and risk-related data.
- **Interactive Visualization**: Displays data on a geographic map with filtering options in Tableau Public.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Data Structure](#data-structure)
- [Dashboard](#dashboard)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/cultural-linguistic-preservation.git
   cd cultural-linguistic-preservation

# Cultural and Linguistic Preservation Project

This project is designed to gather, analyze, and visualize data on endangered languages and cultural practices across the Americas. Using prompt engineering and linguistic data, this project aims to support conservation efforts by providing a comprehensive dataset on linguistic diversity, cultural attributes, and preservation risk levels. The data will be displayed in an interactive dashboard using Tableau Public, helping researchers, conservationists, and communities prioritize language and cultural preservation efforts.

## Project Overview

The goal is to create a data-driven tool that collects structured linguistic and cultural data for each language and culture in the Americas. This includes:
- Detailed linguistic features (phonology, syntax, morphology)
- Cultural practices and traditional knowledge
- Geographic information with latitude and longitude for mapping
- Endangerment risk levels and revitalization efforts
- Historical context and notable events

The project uses OpenAI's API to generate structured insights and categorizes data to create a robust dataset. The resulting dataset is visualized in Tableau Public.

## Features

- **Comprehensive Data Collection**: Collects linguistic and cultural information from diverse regions and languages.
- **Risk Level Assessment**: Provides risk levels for each language based on factors like population of speakers and conservation efforts.
- **Prompt-Generated Insights**: Uses prompt engineering to request detailed linguistic, cultural, and risk-related data.
- **Interactive Visualization**: Displays data on a geographic map with filtering options in Tableau Public.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Data Structure](#data-structure)
- [Dashboard](#dashboard)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/cultural-linguistic-preservation.git
   cd cultural-linguistic-preservation

2.	Set up environment:
	•	Create a .env file in the root directory and add your OpenAI API key:
  OPENAI_API_KEY=your_openai_api_key

4.	Install dependencies:
   Install required Python packages:
   pip install openai pandas python-dotenv

## Usage

1. Generate Cultural and Linguistic Information

To gather information, the main function uses OpenAI’s API to generate structured data based on prompts designed for this project. You can adjust the parameters like location, specialty, and risk level.

2. Data Structure

Collected data is saved in a CSV format with the following fields:

	•	Location: Main region (e.g., “Amazon Basin”)
	•	Specialty: Linguistic or cultural focus area (e.g., “Indigenous Language Preservation”)
	•	Risk Level: Current risk level (e.g., “High Risk”)
	•	Language Name: Primary name of the language
	•	Language Family: Family or linguistic branch of the language
	•	Dialects: Any known dialects
	•	Cultural Practices: Traditional practices associated with the language
	•	Revitalization Efforts: Programs or resources supporting preservation
	•	Geographic Coordinates: Latitude and longitude for Tableau mapping
	•	Historical Context: Brief history of the language and cultural influences

3. Run the Project

Use the main function to start collecting data. Each API call will generate structured insights on cultural and linguistic data and save them in a CSV file:

python main.py

The script will request data for specified locations and specialties, gather relevant information, and save it to cultural_data.csv.

Data Structure

Each entry in the CSV file follows this structure:

Field	Description
Location	|  Main region of the language (e.g., “Amazon Basin”)
Specialty	 |  Focus area, such as “Indigenous Language Preservation”
Risk Level	|  Risk level, e.g., “High Risk”
Language Name	 |  Name of the language being documented
Language Family	 |  Language family or branch
Dialects	|  Known dialects, if any
Cultural Practices	|  Description of cultural practices
Revitalization Efforts	|  Preservation or revitalization efforts
Coordinates	|  Latitude and longitude
Historical Context	|  Background information about the language and culture


This standardized structure ensures the data is comprehensive and compatible with Tableau Public.

Dashboard

The project dashboard, hosted on Tableau Public, allows users to explore data interactively:

	•	Map View: Visualizes languages geographically, with color-coded risk levels.
	•	Filters: Filter by risk level, region, language family, and time period.
	•	Time Series Analysis: Analyze changes in linguistic risk over time where historical data is available.

To view the dashboard, go to Tableau Public - Cultural and Linguistic Preservation Dashboard (replace with the actual link once published).

