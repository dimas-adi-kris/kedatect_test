from odoo import fields, models, _, api
from odoo.exceptions import ValidationError


class KedatechRegistry(models.Model):
    _name = 'kedatech.registry'
    _description = 'Kedatech Registry'

    code = fields.Char(string='Code')
    name = fields.Text(string='Name')
    type = fields.Selection([
        ('fabric', _('Fabric')),
        ('jeans', _('Jeans')),
        ('cotton', _('Cotton')),
    ], string='Type')
    buy_price = fields.Float(string='Buy Price')
    supplier = fields.Many2one('res.partner', string=_('Supplier Name'))

    
    @api.model
    def create(self, vals):
        if vals.get('code', _('New')) == _('New'):
            vals['code'] = self.env['ir.sequence'].next_by_code('kedatech_registry')
        result = super(KedatechRegistry, self).create(vals)
        return result

    @api.constrains('buy_price')
    def _check_buy_price(self):
        for record in self:
            if record.buy_price < 100:
                raise ValidationError(_('Buy price must be greater than 100.'))
            
    def name_get(self):
        res = []
        for record in self:
            code = record.code
            if record.name:
                name = '%s - %s' % (code, record.name)
            res.append((record.id, name))
        return res