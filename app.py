import streamlit as st
import pickle

# Load the trained model (clf.pkl)
with open('clf.pkl', 'rb') as model_file:
    clf = pickle.load(model_file)

# Function to predict if the email is spam or not
def predict_email(email):
    prediction = clf.predict([email])
    if prediction == 0:
        return "Not Spam"
    else:
        return "Spam"

# Streamlit app
def main():
    st.title("Spam Email Classifier")
    st.write("Enter an email to check if it is spam or not.")

    # Taking input email from the user
    email_input = st.text_area("Email Input", "", height=200)

    if st.button("Check Spam"):
        if email_input:
            result = predict_email(email_input)
            st.write(f"The email is: **{result}**")
        else:
            st.write("Please enter an email.")

if __name__ == "__main__":
    main()
