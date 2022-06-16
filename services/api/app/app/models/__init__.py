# ###########################
# Do Not change
from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore
# ###########################

from .user import UserModel, UserCreateModel, UserReadModel
