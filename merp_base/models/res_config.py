from openerp import models, fields


class StockConfigSettings(models.TransientModel):
    _inherit = 'stock.config.settings'

    module_merp_outgoing_routing = fields.Boolean(
        'Add Outgoing Routing strategy options (sort locations)')

    module_merp_custom_access_rights = fields.Boolean(
        'Enable Custom Access Rights for mERP Warehouse App')

    module_merp_receiving_wave_access_rights = fields.Boolean(
        'Enable Receiving Wave Access Rights for mERP Warehouse App')
    module_merp_receiving_wave = fields.Boolean('Enable Receiving Wave')

    module_merp_picking_wave_access_rights = fields.Boolean(
        'Enable Picking Wave Rights for mERP Warehouse App')
    module_merp_picking_wave = fields.Boolean('Enable Picking Wave')

    module_merp_picking_products_skip = fields.Boolean(
        'Allow smart skip of products in pickings and picking waves')

    module_merp_instant_move = fields.Boolean(
        'Allow add more items automatically via mERP Warehouse app')

    module_merp_inventory = fields.Boolean(
        'Advanced mERP Inventory Improvements')
