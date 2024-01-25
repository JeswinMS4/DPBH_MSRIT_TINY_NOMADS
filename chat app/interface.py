import streamlit as st
from interfaceclass import DarkPatternClassifier, extract_arrays_from_input_string


def main():
    st.title('Tiny Nomads - Dark Pattern Classifier')

    website = st.text_input('Enter Website URL:')
    defects = st.text_area(
        'Enter Defects/Content :', '')

    if st.button('Classify Dark Pattern'):

        classifier = DarkPatternClassifier()
        result = classifier.classify_dark_pattern(defects, website)

        st.subheader('Result:')
        st.write(result)
        content, dark_patterns = extract_arrays_from_input_string(result)

    else:
        st.success('Input details')


if __name__ == '__main__':
    main()
