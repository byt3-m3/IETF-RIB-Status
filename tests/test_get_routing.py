from unittest.mock import patch

import xmltodict
from app.Modules.GetRouting import Routing

# Opens Mock return value for xmltodict.parse
with open("resources/example.xml", "r") as xml_file:
    data = xmltodict.parse(xml_file.read())

# Set up Mocks for NCC Client and xmltodict
@patch("app.Modules.GetRouting.manager")
@patch("app.Modules.GetRouting.xmltodict")
def test_get_routing(xml_mock, ncc_mock):
    """
    Basic test on the Routing object.

    :param xml_mock:
    :param ncc_mock:
    :return:
    """
    expected_route_count = 27
    xml_mock.parse.return_value = data # Saves Mock return value to data


    r = Routing()
    r.get_routing_info(host="test", port="0", username="test", password="test")

    routes = [rt for rt in r.routes.values()][0]
    assert len(routes) == expected_route_count


if __name__ == "__main__":
    main()
