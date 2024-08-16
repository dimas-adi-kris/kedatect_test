from odoo import http
from odoo.http import request
import json


class KedatechController(http.Controller):

    @http.route('/api/kedatech_data', auth='public', type='http')
    def test_api_return(self):
        data = request.env['kedatech.registry'].search([])
        res = []
        for record in data:
            res.append({
                'code': record.code,
                'name': record.name,
                'type': record.type,
                'buy_price': record.buy_price,
                'supplier': record.supplier.name,
            })
        return json.dumps(res)