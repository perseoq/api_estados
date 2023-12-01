from backend.instances import mw
from backend.models import States


class StatesSchema(mw.SQLAlchemyAutoSchema):
    class Meta:
        model = States

multiple = StatesSchema(many=True)
single = StatesSchema()