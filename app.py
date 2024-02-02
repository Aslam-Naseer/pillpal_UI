from flask import Flask, render_template
import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()
app = Flask(__name__)

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
print(url)
print(key)

if not url or not key:
    raise ValueError("Supabase credentials not found in .env file")

supabase = create_client(url, key)

@app.route('/')
def index():
    # Use the 'select' method to retrieve all data from 'buckets'
    response_bucket = supabase.table('buckets').select('*').execute()
    response_medicine = supabase.table('medicines').select('*').execute()
    print("Response", response_bucket.data)
    print("Response M", response_medicine.data)
    return render_template('index.html', data_bucket=response_bucket.data, data_medicine=response_medicine.data)

if __name__ == '__main__':
    app.run(debug=True)
