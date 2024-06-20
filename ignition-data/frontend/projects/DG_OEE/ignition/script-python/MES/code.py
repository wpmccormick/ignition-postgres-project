"""Return a list of MES objects of type 'Line' that are not inactive."""
def get_line_list():
	obj_filter = system.mes.object.filter.createFilter()
	obj_filter.setMESObjectTypeName('Line')
	obj_filter.setExcludeInactiveEquipment(True)
	line_list = system.mes.searchMESObjects(obj_filter)
	return line_list 
