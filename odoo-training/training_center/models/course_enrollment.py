from odoo import fields,models

class CourseEnrollment(models.Model):
    _name="training_center.course_enrollment"
    _description="Course Enrollment"

    title=fields.Char("Title",required=True)
    # currency_id = fields.Many2one("res.currency")
    # price =fields.Monetary("Price","currency_id")
    start_date=fields.Date(default=lambda self: fields.Date.today())