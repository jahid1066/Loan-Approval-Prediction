from flask import Flask, request, render_template, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('random_forest_model.pkl')

@app.route('/')
def home():
    return render_template('loan_form.html')

@app.route('/loan_status', methods=['POST'])
def loan_status():
    # Get form data
    data = request.form
    features = [
        int(data['No_Of_Dependent']),
        int(data['Education']),
        int(data['Self_Employed']),
        int(data['Annual_Income']),
        int(data['Loan_Amount']),
        int(data['Loan_Term']),
        int(data['Cibil_Score']),
        int(data['Total_Assets']),
    ]
    prediction = model.predict([features])
    result = "Loan Approved" if prediction[0] == 1 else "Loan Rejected"

    return render_template('loan_form.html', predict_result=result)

if __name__ == '__main__':
    app.run(debug=True)
