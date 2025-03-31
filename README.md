# Spam Email Classifier for CSE205 course

This project is a machine learning-based spam email classifier built using Python and Streamlit. The model is trained using a Naive Bayes classifier, which classifies emails as either "spam" or "not spam" based on their content.

## Features

- **Spam Detection**: Given an email, the model predicts whether the email is spam or not.
- **Streamlit Interface**: The app provides an easy-to-use interface for users to input their emails and get predictions.
- **Pre-trained Model**: The spam detection model is pre-trained and can be directly used in the Streamlit app.

## Project Structure

The project consists of the following files:

- `README.md`: This file containing project information.
- `LICENSE`: MIT License information.
- `app.py`: The main Streamlit application file for user interaction.
- `clf.pkl`: A serialized Naive Bayes model used to classify emails.
- `dataset.zip`: The dataset used to train the model, containing both spam and non-spam emails.
- `requirements.txt`: The list of required Python libraries for the project.
- `trainer.ipynb`: A Jupyter notebook that contains the steps to train the spam detection model.

## Installation

1. Clone this repository to your local machine.
   
   ```bash
   git clone https://github.com/your-username/spam-email-classifier.git
   cd spam-email-classifier
   ```

2. Install the required Python libraries using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure that the pre-trained model `clf.pkl` and dataset `dataset.zip` are available in the project directory.

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

5. Open your browser and go to `http://localhost:8501` to use the spam email classifier.

## Usage

1. On the homepage of the Streamlit app, enter the text of an email in the "Email Input" text area.
2. Click the "Check Spam" button to get the prediction.
3. The app will display whether the email is "Spam" or "Not Spam".

## Model Training (Optional)

To train the spam detection model from scratch:

1. Unzip the dataset (`dataset.zip`) and place it in the appropriate directory.
2. Open the `trainer.ipynb` Jupyter notebook.
3. Follow the steps in the notebook to load and preprocess the dataset, train the Naive Bayes model, and serialize the trained model as `clf.pkl`.
   
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

- **Ayush Dutta** - Developer
- **Ayush Verma** - Developer
- **Mourjo Bosu** - Developer
- **Harel Prasad** - Developer

---

Let me know if you'd like any adjustments or additions!
