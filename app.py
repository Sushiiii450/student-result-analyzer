
import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        name = request.form["name"].strip()
        roll = request.form["roll"].strip()

        marks = [
            float(request.form[f"mark{i}"])
            for i in range(1, 6)
        ]

        if not name or not roll or any(
            mark < 0 or mark > 100 for mark in marks
        ):
            return "Enter valid student details and marks.", 400

        total = sum(marks)
        percentage = total / 5

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "F"

        status = "Pass" if all(m >= 33 for m in marks) else "Fail"

        result = {
            "name": name,
            "roll": roll,
            "total": total,
            "percentage": percentage,
            "highest": max(marks),
            "lowest": min(marks),
            "grade": grade,
            "status": status
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
