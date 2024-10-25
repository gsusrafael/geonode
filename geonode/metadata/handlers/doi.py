#########################################################################
#
# Copyright (C) 2024 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

import logging

from geonode.base.models import ResourceBase
from geonode.metadata.handlers.abstract import MetadataHandler


logger = logging.getLogger(__name__)


class DOIHandler(MetadataHandler):

    def update_schema(self, jsonschema, lang=None):

        doi_schema = {
                "type": "string",
                "title": "DOI",
                "description": "a DOI will be added by Admin before publication.",
                "maxLength": 255,
                "geonode:handler": "doi",
        }

        # add DOI after edition
        self._add_after(jsonschema, "edition", "doi", doi_schema)
        return jsonschema

    def get_jsonschema_instance(self, resource: ResourceBase, field_name: str, lang=None):

        return resource.doi

    def update_resource(self, resource: ResourceBase, field_name: str, json_instance: dict):

        pass

    def load_context(self, resource: ResourceBase, context: dict):

        pass
