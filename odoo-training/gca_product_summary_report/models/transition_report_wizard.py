from odoo import api, fields, models
from . import odoo_datetime_helper
import xlwt
from io import BytesIO
import base64


class SummaryReportWizard(models.TransientModel):
    _name = 'summary.report.wizard'

    def warehouse_id_domain(self):
        if self.env.user.warehouse_ids:
            return [('id', 'in', self.env.user.warehouse_ids.ids)]
        else:
            return [(1, '=', 1)]

    start_date = fields.Datetime(string='Start Date')
    end_date = fields.Datetime(string='End Date')
    location_ids = fields.Many2many('stock.location', string='Locations')
    product_ids = fields.Many2many('product.product', domain=[('type', '=', 'product')])
    excel_file = fields.Binary()

    def _get_data(self):
        data = []
        for wh in self.location_ids:
            for product in self.product_ids:
                helper = self.env['stock.report.helper.summary'].create({
                        'start_date': self.start_date,
                        'end_date': self.end_date,
                        'location_id': wh.id,
                        'product_id': product.id,
                })

                row = {
                    'code' : product.default_code,
                    'description' : product.name,
                    'uom' : product.uom_id.name,
                    'wh_name': wh.display_name,
                    'opening' : helper.get_qty(self.start_date),
                    'delivery' : helper.get_delivery(),
                    'delivery_return' : helper.get_delivery_return(),
                    'receiving' : helper.get_receiving(),
                    'receiving_return' : helper.get_receiving_return(),
                    'transfer_in' : helper.get_total_in() - helper.get_receiving() - helper.get_adjustment_positive() - helper.get_delivery_return(),
                    'transfer_out' : helper.get_total_out()- helper.get_delivery()- helper.get_adjustment_negative() - helper.get_receiving_return() - helper.get_scrap(),
                    'adjustment_positive': helper.get_adjustment_positive(),
                    'adjustment_negative': helper.get_adjustment_negative(),
                    'scrap': helper.get_scrap(),
                    'closing': helper.get_qty(self.end_date),
                }
                data.append(row)

        return data

    def _data(self):
        return {
            'start_date': odoo_datetime_helper.local_time(self.start_date, 'Asia/Yangon'),
            'end_date': odoo_datetime_helper.local_time(self.end_date, 'Asia/Yangon'),
            'data': self._get_data(),
        }

    def print_report_xls(self):
        # styles
        title_style = xlwt.easyxf('font: bold on, height 280; align: horiz center;')
        foot_style = xlwt.easyxf('font: bold on;')

        # prepare excel
        da = self._data()
        wb = xlwt.Workbook()
        sht = wb.add_sheet('Transition Report')
        # freeze header
        sht.set_panes_frozen(True)
        sht.set_horz_split_pos(2)

        sht.write_merge(0, 0, 0, 14, 'Product Summary Report \n For the Period Between ' \
        + da['start_date'] + ' and ' + da['end_date'] , title_style)
        sht.row(0).height = 256*3

        header = ['No.','Product Name','Product Description','UoM','Location Name', 'Opening','Sale Quantity', 'Sale Return Quantity', 
                'Purchase Quantity', 'Purchase Return Quantity', 'Transfer/in','Transfer/Out','Adjust (+)', 'Adjust (-)', 'Scrap', 'Closing']
        # main data
        body_data = da['data']
        if len(body_data) > 0:
            # NOTE: it seem dict keys are returned in order. but not sure
            # use fix dictionary for temp solution on python 3.5 server
            body_keys = ['code', 'description', 'uom', 'wh_name', 'opening',
                         'delivery', 'delivery_return', 'receiving', 'receiving_return', 'transfer_in', 'transfer_out',
                         'adjustment_positive', 'adjustment_negative', 'scrap', 'closing']
        # +2 for title and header, start from 1 to skip title
        # for row in range(1, len(self.product_ids) + 2):
        for row in range(1, len(body_data) + 2):
            for col in range(len(header)):
                # header
                if row == 1:
                    sht.write(row, col, header[col])
                else:
                    # No. column
                    if col == 0:
                        sht.write(row, col, row - 1)
                    # other columns
                    else:
                        body_data_row = row - 2
                        key = body_keys[col - 1]
                        sht.write(row, col, body_data[body_data_row][key])

        # footnote
        # sht.write_merge(len(self.product_ids) + 3, len(self.product_ids) + 3, 0, 14, \
        # 'Note: Data in Opening, Receiving, Transfer and Closing only consider good products (exclude damage products)', foot_style)

        # download excel
        stream = BytesIO()
        wb.save(stream)
        self.excel_file = base64.encodebytes(stream.getvalue())
        filename = 'Product Summary Report - ' + ' - ' + da['start_date'] + ' to ' + da['end_date']
        
        return {
            'type': 'ir.actions.act_url',
            'name': 'contract',
            'url': '/web/content/summary.report.wizard/%s/excel_file/%s.xls?download=true' %(self.id, filename),
        }