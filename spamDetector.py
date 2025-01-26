import streamlit as st
import pickle
model= pickle.load(open('model.pkl','rb'))
cv=pickle.load(open('tranfrom.pkl','rb'))
def main():
    st.title("SMS Spam Detection")
    st.write("This is a simple project to predict whether a SMS is spam or not")
    st.subheader("Classification")
    user_input = st.text_area("Enter the SMS",height=200)
    if st.button("Classify"):
        if user_input:
            data = [user_input]
            vect = cv.transform(data).toarray()
            result = model.predict(vect)
            if result == 1:
                st.error("This SMS is Spam")
            else:
                st.success("This SMS is not Spam")
        else:
            st.write("Please enter a SMS")
main()
