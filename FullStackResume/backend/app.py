from flask import Flask, request, jsonify, send_file
import json
from flask_cors import CORS
from main import main
import os
import subprocess
# import time

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
COMPILE_FOLDER = 'compile'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(COMPILE_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        resume = request.files.get('file')
        job_desc = request.form.get('jobDesc')
        sections_raw = request.form.get('sections')
        other_section = request.form.get('otherSection')

        if resume:
            resume_path = os.path.join(UPLOAD_FOLDER, resume.filename)
            resume.save(resume_path)


        if not resume or not job_desc or not sections_raw:
            return jsonify({"error": "Missing required fields (file, jobDesc, sections)"}), 400

        try:
            sections = json.loads(sections_raw)

            if other_section:
                sections.append(other_section)

        except json.JSONDecodeError:
            return jsonify({"error": "Invalid JSON in 'sections'"}), 400
        
        try:
            overall_sim, template = main(resume=resume_path, job_desc=job_desc, sections=sections, other_section=other_section,
                                resume_temp='template.txt')
        except Exception as e:
            return jsonify({"error": str(e)}), 500

        response = {
             "message": "File uploaded successfully",
             "overall_sim": overall_sim,
             "template" : template
        }

        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/compile', methods=['POST'])
def compile():
    
    try:
        latex_code = request.json.get('latexCode')
        tex_file_path = os.path.join(COMPILE_FOLDER, f"GeneratedResume.tex")
        pdf_file_path = os.path.join(COMPILE_FOLDER, f"GeneratedResume.pdf")

        os.chmod(pdf_file_path, 0o644)
        os.chmod(COMPILE_FOLDER, 0o755)

        # Write LaTeX content to a .tex file
        with open(tex_file_path, "w") as tex_file:
            tex_file.write(latex_code)

        try:
            result = subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", "-output-directory", COMPILE_FOLDER, tex_file_path]
        )
            return send_file(
                pdf_file_path,
                mimetype='application/pdf',
                as_attachment=False  # Change to True if you want the browser to prompt download
            )
        
        except subprocess.CalledProcessError as e:
            return jsonify({"error": str(e)}), 500
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)