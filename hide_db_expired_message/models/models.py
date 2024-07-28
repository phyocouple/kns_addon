from odoo import models, http

class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    @classmethod
    def _dispatch(cls, endpoint, *args):
        request = http.request

        # Suppress the "database has expired" message
        if hasattr(request, 'db') and request.db:
            request.session._db_expired = False

        return super(IrHttp, cls)._dispatch(endpoint, *args)
