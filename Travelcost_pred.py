import streamlit as st
import joblib
import pandas as pd
import os


def main():
    # External CSS style
    external_css = """
        <style>

            /* Add your CSS styles here */
            .travel-package {
                background-color: #EEEEEE;
                padding: 10px;
                border: 1px solid #DCDCDC;
                border-radius: 10px;
                margin-top: 20px; 
                
            }

            .travel-package1 {
                background-image: linear-gradient(to bottom right, #FF512F, #DD2476);
                border: 1px solid #DCDCDC;
                padding: 10px;
                border-radius: 10px;
                margin-top: 20px;   
            }

            .travel-package2 {
                background-image: linear-gradient(to bottom right, #FF3E9D, #0E1F40);
                border: 1px solid #DCDCDC;
                padding: 10px;
                border-radius: 10px;
                margin-top: 20px;   
            }


            .package-details {
                font-size: 16px;
                color: #333;
            }

           
        </style>
    """
    
    # Injecting external CSS style
    st.markdown(external_css, unsafe_allow_html=True)
    html_temp = """
            <div style="background-color:lightblue;padding:16px">
            <h2 style="color:black";text-align:center>TRAVEL EXPENSE PREDICTION</h2>
            </div>
            """
    user_input=[]
    st.markdown(html_temp,unsafe_allow_html=True)
   

    
    
    p1 = st.number_input("Enter the Duration of the Travel: ", step=1, format="%d")
    user_input.append(p1)
    mm = st.text_input("Starting from :")
    #if not mm:
        #st.warning("Please enter a value.")
    p2 = st.text_input("Enter your Destination : ")
    #if not p2:
       # st.warning("Please enter destination.")

    p2 = p2.strip()
    user_input.append(p2)
    p3 = st.selectbox("Accommodation Type : ", ('Airbnb', 'Guesthouse', 'Hostel', 'Hotel', 'Resort', 'Riad', 'Vacation rental', 'Villa'))
    user_input.append(p3)
    p4 = st.selectbox("Enter your Transportation : ",('Airplane', 'Bus', 'Car', 'Car rental', 'Ferry', 'Flight', 'Plane', 'Subway', 'Train'))
    user_input.append(p4)
    columns = ["Duration (days)", "Destination", "Accommodation type", "Transportation"]
    u_dataframe = pd.DataFrame([user_input], columns=columns)
    if p2 and mm:
        df = pd.read_csv("u_t_d_f.csv")
        u_dataframe = pd.get_dummies(u_dataframe, columns=['Destination'], prefix='Destination')
        u_dataframe = pd.get_dummies(u_dataframe, columns=['Accommodation type'], prefix='Accommodation type')
        u_dataframe = pd.get_dummies(u_dataframe, columns=['Transportation'], prefix='Transportation')

        missing_col = set(df.columns) - set(u_dataframe)
        for col in missing_col:
            u_dataframe[col] = 0
        u_dataframe = u_dataframe[df.columns]
        st.write("The converted data frame of user:", u_dataframe)

        if st.button('PREDICT'):
            model_path = os.path.abspath('best_model.sav')
            if os.path.exists(model_path):
                model = joblib.load(model_path)
                # Rest of your code...
            else:
                print(f"Model file '{model_path}' not found.")
            
            res=model.predict(u_dataframe)
            st.success("Your travel expense could be around: {} $".format(round(res[0])))
        

        # Display additional details about the travel package with improved styling
            
            st.markdown("<h3 text_align=center>One plan's Package Details:</h3>", unsafe_allow_html=True)
            st.markdown(
                """
                <div class="travel-package">
                    <p class="package-details"><strong>Accommodation Type:</strong> {}</p>
                    <p class="package-details"><strong>Transportation:</strong> {}</p>
                    <p class="package-details"><strong>Duration:</strong> {} days</p>
                    <p class="package-details"><strong>Cost : </strong> {}</p>
                </div>
                """.format(user_input[2], user_input[3], user_input[0],round(res[0])),
                unsafe_allow_html=True)
        
            # Display additional details about the travel package with improved styling
            st.markdown("<h3 text_align=center>Dream planner Package Details:</h3>", unsafe_allow_html=True)
            st.markdown(
                """
                <div class="travel-package1">
                    <p class="package-details"><strong>Accommodation Type:</strong> {}</p>
                    <p class="package-details"><strong>Transportation:</strong> {}</p>
                    <p class="package-details"><strong>Duration:</strong> {} days</p>
                    <p class="package-details"><strong>Cost : </strong> {}</p>
                </div>
                """.format(user_input[2], user_input[3], user_input[0],round(res[0])),
                unsafe_allow_html=True)
        
             # Display additional details about the travel package with improved styling
            st.markdown("<h3 text_align=center>peace of mind planner Package Details:</h3>", unsafe_allow_html=True)
            st.markdown(
                """
                <div class="travel-package2">
                    <p class="package-details"><strong>Accommodation Type:</strong> {}</p>
                    <p class="package-details"><strong>Transportation:</strong> {}</p>
                    <p class="package-details"><strong>Duration:</strong> {} days</p>
                    <p class="package-details"><strong>Cost : </strong> {}</p>
                </div>
                """.format(user_input[2], user_input[3], user_input[0],round(res[0])),
                unsafe_allow_html=True)
    else:
        st.warning("Enter valid credentials.")

 
if __name__=='__main__':
    main()