from odoo import models,fields,api

class Course(models.Model):
    _inherit="training_center.course"
    enroll_ids=fields.One2many("course_enrollment","course_id")

    discount=fields.Float("Discount",default=0)
    early_bird_End_Date=fields.Date(default=lambda self: fields.Date.today(), string="Early Bird End Date")
    early_bird_discount=fields.Float("Early Bird Discount",default=0)
     
    #Compute field
    num_of_students_enrolls= fields.Integer(compute="_compute_num_of_enrollments")

    def _compute_num_of_enrollments(self):
        for course in self:
            course.num_of_students_enrolls = len(course.enroll_ids)

    def action_enrollment(self):
        domain=[('course_id','=',self.id)]
        #enrollment.acttion_course_enrollent ka external ID
        action=self.env.ref('enrollment.action_course_enrollment')
        result=action.read()[0]
        result['domain']=domain
        return result
    
    def name_get(self):
        result=[]
        for course in self:
            instrustors=course.teacher_ids.mapped('name')
            name_list =','.join(instrustors)
                
        
            result.append((course.id,course.name+f"({name_list})"))
        return result
    