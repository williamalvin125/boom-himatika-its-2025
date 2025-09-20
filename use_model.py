import joblib
import warnings
warnings.filterwarnings('ignore')

if __name__ == "__main__":
    # Load Model
    lr_model = joblib.load("./model/lr.joblib")
    dt_model = joblib.load("./model/dt.joblib")

    a = lr_model.coef_[0]
    b = lr_model.intercept_
    f_x = lambda x: a*x + b

    # Get Input from User
    user_input = float(input("Enter the value of x: "))
    choosen_model = input("Choose model (lr/dt): ").strip().lower()
    if choosen_model == "dt":
        prediction = dt_model.predict([[user_input]])[0]
        print(f"Decision Tree Prediction: f({user_input}) = {prediction}")
    elif choosen_model == "lr":
        prediction = f_x(user_input)
        print(f"Linear Regression Prediction: f({user_input}) = {prediction}")
    else:
        raise ValueError("Model not recognized. Re-run program and please ONLY choose 'lr' or 'dt'.")
