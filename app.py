from flask import Flask, request, render_template, redirect
import os,sys
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

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        return redirect("/dementia?pid=" + request.form['input_pid'])
    
    return render_template("home.html")


@app.route('/dementia',methods=['GET','POST'])
def dementia_analyse():
    if request.method == 'POST':
        return redirect("/dementia?pid=" + request.form['input_pid'])


    pid = request.args.get('pid')

    # Use the 'select' method to retrieve all data from 'buckets'
    response_patients = supabase.table('patients').select('*').execute()
    response_main = supabase.table('patients').select('*').eq("id",pid).execute().data
    response_scans = supabase.table('scans').select('*').eq("patient_id",pid).execute()

    patients_list = []

    for patient in response_patients.data:
        patients_list.append(patient)

    images_list = []

    for scan in response_scans.data:
        images_list.append(scan)

    response_main = response_main[0]

    return render_template('dementia.html', patients=patients_list, images = images_list, main=response_main, scan_type = "Dementia")

@app.route('/tumor',methods=['GET','POST'])
def tumor_analyse():
    if request.method == 'POST':
        return redirect("/tumor?pid=" + request.form['input_pid'])


    pid = request.args.get('pid')

    # Use the 'select' method to retrieve all data from 'buckets'
    response_patients = supabase.table('patients').select('*').execute()
    response_main = supabase.table('patients').select('*').eq("id",pid).execute().data
    response_scans = supabase.table('scans').select('*').eq("patient_id",pid).execute()

    patients_list = []

    for patient in response_patients.data:
        patients_list.append(patient)

    images_list = []

    for scan in response_scans.data:
        images_list.append(scan)

    response_main = response_main[0]

    return render_template('tumor.html',patients=patients_list, images = images_list, main=response_main, scan_type="Tumor")

if __name__ == '__main__':
    app.run(debug=True)
