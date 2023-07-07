from odoo import models,api,fields,tools

class CourseEnrollmentStatistic(models.Model):
    _name="course.enrollment.statistics"
    _auto=False #table ma sout nae so yin auto False

    course_id=fields.Many2one('training_center.course','Course',readonly=True)
    enroll_count=fields.Integer(string="Enroll Count",readonly=True)
    total_amount=fields.Integer(string="Total",readonly=True)
    discount=fields.Integer(string="Discout",readonly=True)

    def init(self):
        tools.drop_view_if_exists(self.env.cr,self._table)
        query="""
        CREATE OR REPLACE VIEW course_enrollment_statistics AS(
        SELECT
                min(enc.id) as id,
                enc.course_id as course_id,
                count(enc.id) as enroll_count,
                SUM(enc.total_amount) AS total_amount
                
        FROM
            course_enrollment AS enc
        JOIN 
            training_center_course as tcc ON tcc.id = enc.course_id
        WHERE enc.state= 'confirm'
        GROUP BY enc.course_id
        );
        """

        self.env.cr.execute(query)

       
        