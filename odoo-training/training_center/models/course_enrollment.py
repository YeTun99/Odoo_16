from odoo import fields,models

class CourseEnrollment(models.Model):
    _name="training_center.course_enrollment"
    _description="Course Enrollment"

    title=fields.Char("Title")
    currency_id = fields.Many2one("res.currency")
    price =fields.Monetary("Price","currency_id")