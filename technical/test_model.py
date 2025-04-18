import pickle
import pandas as pd

# Function to load the correct model based on the user's choice
def load_model(model_filename):
    with open(model_filename, 'rb') as file:
        model = pickle.load(file)
    return model

# Function to predict based on user input
def predict_h2_production():
    # Take input choice from the user
    print("Select the input parameter:")
    print("1. Temperature")
    print("2. Pressure")
    print("3. Both Temperature and Pressure")
    print("4. Biogas Mass Flow Rate")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        # Load the model trained on temp
        model_filename = 'gbr_model_temp_vs_h2.pkl'
        model = load_model(model_filename)
        temp = float(input("Enter the temperature (°C): "))
        input_data = pd.DataFrame({'temp': [temp]})
        
    elif choice == '2':
        # Load the model trained on press
        model_filename = 'gbr_model_press_vs_h2.pkl'
        model = load_model(model_filename)
        press = float(input("Enter the pressure (bar): "))
        input_data = pd.DataFrame({'press': [press]})
        
    elif choice == '3':
        # Load the model trained on both temp and press
        model_filename = 'gbr_model_temp_press_vs_h2.pkl'
        model = load_model(model_filename)
        temp = float(input("Enter the temperature (°C): "))
        press = float(input("Enter the pressure (bar): "))
        input_data = pd.DataFrame({'temp': [temp], 'press': [press]})
        
    elif choice == '4':
        # Load the model trained on biogas_mass
        model_filename = 'gbr_model_biogas_mass_vs_h2.pkl'
        model = load_model(model_filename)
        biogas_mass = float(input("Enter the biogas mass flow rate(kg/hr): "))
        input_data = pd.DataFrame({'biogas_mass': [biogas_mass]})
        
    else:
        print("Invalid choice. Please try again.")
        return
    
    # Make the prediction
    h2_production = model.predict(input_data)
    print(f"Predicted H₂ Production: {h2_production[0]:.9f} kg/hr")

# Run the prediction function
predict_h2_production()
