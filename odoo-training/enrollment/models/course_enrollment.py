from odoo import fields,models,api
from odoo.exceptions import UserError
class CourseEnrollment(models.Model):
    _name="course_enrollment"
    _description="Course Enrollment"
    _inherit=['mail.thread','mail.activity.mixin']

    name=fields.Char("Title")
    start_date=fields.Date(default=lambda self: fields.Date.today(), string="Enroll Date",tracking=True)
    course_start_date=fields.Date(related="course_id.start_date",string="Course Start Date",readonly=True)
    course_id=fields.Many2one("training_center.course","Course",tracking=True)

    course_enroll=fields.Many2many("training_center.course")
    member_id=fields.Many2one('training_members.course_member','Member',tracking=True)
    member_image=fields.Binary(related='member_id.image_1920')

    currency_id=fields.Many2one("res.currency")
    price=fields.Monetary("Price","currency_id",related="course_id.price")

    total_amount=fields.Monetary("Total Amount",compute="_compute_total_amount",store=True)
    early_bird_end_date=fields.Date(default=lambda self: fields.Date.today(),related="course_id.early_bird_End_Date",readonly=True)


    #compute field
    @api.depends('course_id.price','course_id.discount',"early_bird_end_date","course_id.early_bird_discount","start_date")
    def _compute_total_amount(self):
        for product in self:
            if product.early_bird_end_date < product.start_date:
                product.total_amount=product.course_id.price-(product.course_id.discount*product.course_id.price)
            elif product.early_bird_end_date >= product.start_date :
                product.total_amount=product.course_id.price-(product.course_id.early_bird_discount*product.course_id.price)
           
    state= fields.Selection(
        string="state",
        selection=[('new','New'),('draft','Draft'),('confirm','Confirm'),('canceled','Canceled')],
        default='new'
    )

    def action_do_canceled(self):
        if self.state !="completed":
            self.state="canceled"
        return True
    def action_do_confirm(self):
        return self.write({"state":"confirm"})
    
    def action_do_draft(self):
        return self.write({"state":"new"})
    
     
    @api.model
    def create(self,vals_list):
        vals_list['name']=self.env['ir.sequence'].next_by_code('course_enrollment') or '/'
        return super().create(vals_list)