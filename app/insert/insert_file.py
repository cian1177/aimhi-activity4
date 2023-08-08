from flask import request, session, flash
from app.models.source import source
from app import db
import csv

def upload_file():
    # try:
        csv_file = request.files['csv_file']
        if csv_file:
            # Reads CSV file and insert data into the database
            file_data = csv.reader(csv_file.read().decode("utf-8").splitlines())
            if db.session.query(source).first() is None:
                for row in file_data:
                    new_file = source(
                        ref=row[0],
                        status=row[1],
                        location=row[2],
                        name=row[3],
                        created=row[4],
                        type=row[5],
                        status_change=row[6],
                        open_actions=row[7],
                        total_actions=row[8],
                        association=row[9],
                        overdue=row[10],
                        images=row[11],
                        comments=row[12],
                        documents=row[13],
                        project=row[14],
                        report_forms_status=row[15],
                        report_forms_group=row[16]
                    )
                    db.session.add(new_file)
                    db.session.commit()
                session.permanent = True
                flash("File uploaded and inserted into the database.", "info")
            else:
                session.permanent = True
                flash("File already uploaded", "info")
    # except:
        flash("Wrong file Uploaded", "info")

