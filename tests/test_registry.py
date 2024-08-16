from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)


class TestKedatechRegistry(TransactionCase):

    def setUp(self):
        super(TestKedatechRegistry, self).setUp()
    
    def test_10_create(self):
        registry = self.env['kedatech.registry'].create({
            'name': 'Test',
            'type': 'fabric',
            'buy_price': 200
        })
        registry2 = self.env['kedatech.registry'].create({
            'name': 'Test2',
            'type': 'fabric',
            'buy_price': 200
        })
        _logger.info(registry.code)
        _logger.info(registry2.code)
        self.assertNotEqual(registry.code, registry2.code, "Code must be unique.")
    
    def test_20_buy_price(self):
        with self.assertRaises(ValidationError):
            self.env['kedatech.registry'].create({
                'name': 'Test',
                'type': 'fabric',
                'buy_price': 50
            })