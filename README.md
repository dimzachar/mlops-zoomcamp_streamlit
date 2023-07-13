# mlops-zoomcamp_streamlit

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://issues.streamlitapp.com)

See the [mlops-zoomcamp_projects_EDA](https://github.com/dimzachar/mlops-zoomcamp_projects_EDA) repo for more details.

This project is structured into two main Python files:

1. `analysis.py` - This file contains the functions necessary for data preprocessing and analysis. It includes functions to read the data, preprocess text (tokenization, stop word removal, and lemmatization), calculate word frequency, and generate a word cloud.

2. `app.py` - This is the main file that runs the Streamlit application. It uses the functions from the `analysis.py` to load and preprocess the data, calculate word frequency, and generate a word cloud. It also uses Streamlit to display these results in a web application.

## Run locally

To run this project, you'll need to install the required Python packages. You can install these packages using pip and the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage

Navigate to the project directory and run the Streamlit application:

```bash
streamlit run app.py
```

This will start a local web server and open your default web browser to display the application.

## Data

This project uses a CSV file named `mlops_2022.csv` located in the `./Data` directory. The main column used for analysis is `project_title`.


## Contributing

We welcome contributions to this project! Here's how you can help:

1. **Fork the Repository**: Click the 'Fork' button at the top right of this page and clone your forked repository to your local machine.

2. **Create a New Branch**: From your local repository, create a new branch for your feature or bugfix.

3. **Make Your Changes**: Make your changes to the new branch. Be sure to test your changes!

4. **Commit and Push Your Changes**: Once you're happy with your changes, commit them with a meaningful commit message and push the branch to your forked repository on GitHub.

5. **Create a Pull Request**: From your forked repository on GitHub, click the 'New pull request' button located at the top of your repo. Ensure it is asking to pull from your branch to the main branch of this repository.

We will review your changes and, if they are accepted, they will be included in the project.

If you have any questions about contributing, please feel free to contact us. Thank you for your interest in improving our project!
