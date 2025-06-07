# Stress_Detection_Prediction
"A "Streamlit-based application for predicting Perceived Stress Scale (PSS) scores using machine learning models."
# PSS Score Prediction
<img src="https://github.com/rpjinu/Stress_Detection_Prediction/blob/main/stress_detection_image.png" width=600>

This project is a machine learning application designed to predict Perceived Stress Scale (PSS) scores using various behavioral, psychological, and lifestyle features.

## Overview

* Predict your stress levels based on factors like personality, sleep, and activity data.
* Streamlit-powered user interface for easy input and real-time predictions.

## Features

*   **Machine Learning Model:** Trained on a dataset including personality traits, sleep metrics, and mobility data to accurately predict PSS scores.
*   **Interactive UI:** User-friendly interface built with Streamlit for effortless data entry and stress prediction.
*   **Customizable Predictions:** Input key features like Openness, Conscientiousness, sleep duration, and more for personalized predictions.
*   **API Ready:** Integrates seamlessly with larger systems or functions as a personal stress tracking application.

## Dataset

The project utilizes a dataset encompassing the following features:

*   Personality Traits: Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism
*   Sleep Metrics: Sleep time, Wake time, Sleep duration
*   Other Features: Skin conductance, Mobility radius, and others

## Requirements

*   Python 3.7+
*   Libraries: pandas, numpy, scikit-learn, joblib, streamlit

## Installation

1.  Clone the repository:

    ```bash
    git clone [https://github.com/yourusername/pss-score-prediction.git](https://github.com/yourusername/pss-score-prediction.git)
    cd pss-score-prediction
    ```

2.  Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3.  Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

## Usage

1.  Open the app in your browser (URL: http://localhost:8501).
2.  Enter feature values using the provided sliders or input boxes.
3.  Click the "Predict" button to see your predicted PSS score.

## Model Information

The machine learning model was chosen after evaluating multiple algorithms. The best-performing model was trained and saved using joblib. It predicts PSS scores based on user-provided data.

## Demo

A demo of the application is available. (Link to be added if available)

## Author

Created by Ranjan.

## License

This project is licensed under the MIT License.
