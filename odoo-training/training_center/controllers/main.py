from odoo import http   
from odoo.http import request

class Main(http.Controller):

    @http.route('/html/courses',type="http",auth="none")
    def courses_html(self):
        course_obj=request.env['training_center.course'].sudo().search([])
        html_result="<html><body><ul>"
        for course in course_obj:
            html_result+="<li>%s</li>"%course.name
        html_result+="</ul></body></html>"
        return html_result
    
    @http.route("/api/v1/courses",type="json",auth="none")
    def courses_json(self):
        course_obj=request.env['training_center.course'].sudo().search([])
        return course_obj.read(['name','course_level'])
    
    @http.route("/html/course_details",type="http",auth="none")
    def course_details(self,course_id):
        record=request.env['training_center.course'].sudo().browse(int(course_id))
        return u"<html><body><h1> %s </h1>Instructors:%s</body></html>"%(record.name,u','.join(record.teacher_ids.mapped('name'))or 'none',)
    
    @http.route("/html/course_detail/<model('training_center.course'):course>",type="http",auth="auth")
    def course_details_in_path(self,course):
        return self.course_details(course.id)
    
    @http.route("/api/v1/login",type="json",methods=["POST"],auth="none")
    def userlogin(self):
        try:
            req = http.request.get_json_data()
            if req['login'] and req['password']:
                if not 'database' in req:
                    req['database'] = request.session.db
                login = request.session.authenticate(req['database'],req['login'].lower(),req['password'])
            return login
        except Exception as e:
            return{"error_message":e}
        
    @http.route("/api/v1/course_details/<int:course_id>",type="json",auth="user")
    def course_details_json(self,course_id):
        records = request.env['training_center.course'].sudo().search_read([('id','=',course_id)],fields=['name','teacher_ids'],order="id.create_date")
        return records
    
  
    
    @http.route('/api/v1/course_enrollment',type="json",authon="user")
    def course_enrollemnt_json(self,**kwargs):
        try:
            req = http.request.get_json_data()
            record = request.env['training_center.course'].sudo().search([('id','=',req['course'])])
            member = request.env['training_members.course_memeber'].sudo().search([('id','=',req['member'])])
            if not record:
                return{"error_message":"Invalid Course"}
            return record
        except Exception as e:
            return{"error_message":e}