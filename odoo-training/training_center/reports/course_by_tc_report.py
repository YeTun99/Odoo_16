from odoo import api,models

class TrainingCenterReport(models.AbstractModel):
    _name= "report.training_center.course_by_training_center"

    @api.model
    def _get_report_values(self,docids,data=None):
        domain=[("company_id","in",docids)]
        courses=self.env["training_center.course"].search(domain)
        #tc_ids=courses.mapped("company_id")
        company_course=[(courses.company_id,courses.filtered(lambda course:course.company_id ==courses.company_id))]
        docargs={"company_course":company_course}
        return docargs