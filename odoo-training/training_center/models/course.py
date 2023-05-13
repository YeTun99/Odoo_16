from odoo import fields,models,api
class Course(models.Model):
    _name="training_center.course"
    _description="Training Center Course"
    name = fields.Char("Course Title",required=True)
    descr= fields.Html("Description")
    course_level= fields.Selection(
        [
            ("basic","Basic"),
            ("intermediate","Intermediate"),
            ("advanced","Advanced"),
        ],"Course Level"
    )

    #Relational Fields
    company_id=fields.Many2one("res.partner",string="Company")
    teacher_ids=fields.Many2many("res.partner",string="Teacher")
    course_items_ids=fields.One2many("training_center.course.line.item","course_id")
    country_id=fields.Many2one("res.country",string="Country",related="company_id.country_id")
    #price helper
    currency_id = fields.Many2one("res.currency")
    price = fields.Monetary("Price","currency_id", groups="training_center.course_group_manager")
    #Boolean
    active=fields.Boolean("Active",default=True)
    #Date Time Field
    start_date=fields.Date(default=lambda self: fields.Date.today())
    end_date=fields.Date(default=lambda self: fields.Date.today())

    #Image
    cover_image=fields.Binary("Course Cover")

    #compute field
    num_of_contents=fields.Integer(compute="_compute_num_of_contents")

    @api.depends("course_items_ids")
    def _compute_num_of_contents(self):
        for course in self:
            course.num_of_contents=len(course.course_items_ids)