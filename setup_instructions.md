# Setup Instructions

## Step 1: Create a Virtual Environment

Open a terminal and navigate to the project directory:

```sh
cd "/c:/Users/MS/Downloads/Walmart sales Prediction"
```

Create a virtual environment named `salesenv`:

```sh
python -m venv salesenv
```

## Step 2: Activate the Virtual Environment

- On Windows:

```sh
salesenv\Scripts\activate
```

- On macOS and Linux:

```sh
source salesenv/bin/activate
```

## Step 3: Install Required Packages

With the virtual environment activated, install `streamlit` and `pandas`:

```sh
pip install streamlit pandas
```

Install the remaining required libraries:

```sh
pip install numpy scikit-learn matplotlib
```

## Step 4: Verify Installation

To verify that the packages are installed correctly, run:

```sh
python -c "import streamlit, pandas, numpy, sklearn, matplotlib; print('Packages installed successfully')"
```

## Step 5: Run Streamlit Application

To run the Streamlit application, execute the following command:

```sh
streamlit run app.py
```
