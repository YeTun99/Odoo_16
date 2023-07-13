from odoo import http   
from odoo.http import request

class Main(http.Controller):



    @http.route('/html/courses/enrollemnt',type="http",auth="none")
    def course_enroll(self):
        course_obj=request.env['training_center.course'].sudo().search([])
        html_result="<html><body>"
        selection=""
        for course in course_obj:
            selection+="<option value=%s>%s</option>"%(course.id,course.name)
        html_result+="<form><select>%s</select></form></body></html>"%selection
        return html_result