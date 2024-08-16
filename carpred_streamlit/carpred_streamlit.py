import pickle
import pandas as pd
import streamlit as st

#Add the folder path to the sys path as streamlit in deployment mode only looks for files in your main directory.
model = pickle.load(open('carpred_streamlit/pipeline.pkl', 'rb'))
image_url = 'carpred_streamlit/cars.jpg'

def main():
    st.title('Car Price Prediction')
    st.image(image_url, caption='Cars at a dealership', use_column_width=True)

    st.write('This is a simple car price prediction app. Please enter the details of the car and we will predict the price for you.')

    brand = st.text_input('Brand of the car')
    milage = st.number_input('Kilometers driven', min_value=0)
    accident = st.selectbox('Accident History', ['Yes', 'No'])
    clean_title = st.selectbox('Clean Title', ['Yes', 'No'])
    interior_color = st.selectbox('Interior Color', ['Black', 'White', 'Other'])
    exterior_color = st.selectbox('Exterior Color', ['Black', 'White', 'Other'])
    tsm = st.selectbox('Transmission', ['Manual', 'Automatic', 'DCT', 'Other'])
    fuel = st.selectbox('Fuel Type', ['Gasoline', 'Diesel', 'Hybrid', 'Other'])
    engine_displacement = st.number_input('Engine Displacement', min_value=0)
    age = st.number_input('Age', min_value=0)

    new_entry = pd.DataFrame(
        {'brand': [str(brand)],
        'milage': [int(milage)],
        'accident': [str(accident)],
        'clean_title': [str(clean_title)],
        'interior_color': [str(interior_color)],
        'exterior_color': [str(exterior_color)],
        'tsm': [str(tsm)],
        'fuel': [str(fuel)],
        'Engine_Displacement': [float(engine_displacement)],
        'age': [int(age)]}
    )



    if st.button('Predict'):
        makeprediction = model.predict(new_entry)

        output = round(makeprediction[0], 2)
        st.success('Your car is worth ${}'.format(output))

if __name__ == '__main__':
    main()