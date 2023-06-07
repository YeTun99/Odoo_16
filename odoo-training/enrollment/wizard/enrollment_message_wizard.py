from odoo import models,fields,api

import logging
_logger =logging.getLogger(__name__)
class EnrollCourse(models.Model):
    _name='enroll.message.wizard'
    _description='Enrollment Message Wizard'
    message_subject=fields.Char(default='Hi')
    message_body=fields.Html()
    enroll_course_ids=fields.Many2many('course_enrollment',string="Enroll Course")
    
    def btn_message(self):
        for course in self.enroll_course_ids:
            course.message_post(body=self.message_body,subject=self.message_subject,subtype_xmlid="mail.mt_comment")
        _logger.info('Sent %d messages to course %s',len(self.enroll_course_ids),str(self.enroll_course_ids))
        return True
    
    def _action_open_wizard_modal(self):
        """Open Wizard"""
        return{
            'name':'Inform Message',
            'type':'ir.actions.act_window',
            'res_model':'enroll.message.wizard',
            'view_mode':'form',
            'view_type':'form',
            'res_id':self.id,
            'target':'new',
        }
    
    @api.model
    def default_get(self,field_names):
        defaults_dict=super().default_get(field_names)
        enroll_ids=self.env.context['active_ids']
        defaults_dict['enroll_course_ids']=[(6,0,enroll_ids)]
        return defaults_dict