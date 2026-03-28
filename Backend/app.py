from flask import Flask, request, jsonify
from flask_cors import CORS
from snowflake_db import save_application, get_all_applications
from sas_connector import score_application
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)  

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": " LoanIQ Backend is running",
        "model": "lr_step__pipeline_2_",
        "database": "Snowflake LOAN_DB"
    })

 
@app.route("/predict", methods=["POST"])
def predict():
    try:
      
        data = request.get_json()
        print(f" Received application: {data}")

        if not data:
            return jsonify({"error": "No data received"}), 400

       
        result = score_application(data)
        print(f"🤖 SAS Viya result: {result}")

        
        save_application(
            data=data,
            prediction=result["prediction"],
            probability=result["probability"]
        )
        print(" Saved to Snowflake")

        
        return jsonify({
            "success": True,
            "approved": result["approved"],
            "prediction": result["prediction"],
            "probability": result["probability"]
        })

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route("/applications", methods=["GET"])
def applications():
    try:
        data = get_all_applications()
        return jsonify({
            "success": True,
            "count": len(data),
            "data": data
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.getenv("FLASK_PORT", 5000))
    print(f"""
    
      LoanIQ Backend Server Starting    
      http://localhost:{port}           
      Database: Snowflake              
      Model: SAS Viya lr_step_pipeline  
    """)
    app.run(debug=True, port=port)