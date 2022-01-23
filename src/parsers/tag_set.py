import xml.etree.ElementTree as ET

class TagSet:
    def identify_declaration_tag(line : ET.Element) -> bool:
        return {
            'declaration' : True
        }.get(line.tag, False)

    def identify_template_tag(line : ET.Element) -> bool:
        return {
            'template' : True
        }.get(line.tag, False)

    def identify_location_tag(line : ET.Element) -> bool:
        return {
            'location' : True
        }.get(line.tag, False)

    def identify_transition_tag(line : ET.Element) -> bool:
        return {
            'transition' : True
        }.get(line.tag, False)

    def identify_init_tag(line : ET.Element) -> bool:
        return {
            'init' : True
        }.get(line.tag, False)

    def identify_name_tag(line : ET.Element) -> bool:
        return {
            'name' : True
        }.get(line.tag, False)

    def identify_system_tag(line : ET.Element) -> bool:
        return {
            'system' : True
        }.get(line.tag, False)

    def identify_queries_tag(line : ET.Element) -> bool:
        return {
            'queries' : True
        }.get(line.tag, False)

    def identify_query_tag(line : ET.Element) -> bool:
        return {
            'query' : True
        }.get(line.tag, False)

    def identify_formula_tag(line : ET.Element) -> bool:
        return {
            'formula' : True
        }.get(line.tag, False)

    def identify_comment_tag(line : ET.Element) -> bool:
        return {
            'comment' : True
        }.get(line.tag, False)

    def identify_parameter_tag(line : ET.Element) -> bool:
        return {
            'parameter' : True
        }.get(line.tag, False)