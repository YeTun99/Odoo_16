from odoo import fields,models,api
from odoo.exceptions import UserError
class CourseEnrollment(models.Model):
    _name="course_enrollment"
    _description="Course Enrollment"

    name=fields.Char("Title")
    start_date=fields.Date(default=lambda self: fields.Date.today(), string="Enroll Date")
    course_start_date=fields.Date(related="course_id.start_date",string="Course Start Date",readonly=True, attrs={'readonly': True, 'disabled': True})
    course_id=fields.Many2one("training_center.course","Course")
    currency_id=fields.Many2one("res.currency")
    price=fields.Monetary("Price","currency_id",related="course_id.price")

    total_amount=fields.Monetary("Total Amount",compute="_compute_total_amount")
    early_bird_end_date=fields.Date(related="course_id.early_bird_End_Date",readonly=True, attrs={'readonly': True, 'disabled': True})


    #compute field
    @api.depends('course_id.price','course_id.discount',"course_id.early_bird_End_Date","course_id.early_bird_discount","start_date","course_id.start_date")
    def _compute_total_amount(self):
        for product in self:
            if product.course_id.early_bird_End_Date < product.start_date:
                product.total_amount=product.course_id.price-(product.course_id.discount*product.course_id.price)
            elif product.course_id.early_bird_End_Date >= product.start_date :
                product.total_amount=product.course_id.price-(product.course_id.early_bird_discount*product.course_id.price)
           
