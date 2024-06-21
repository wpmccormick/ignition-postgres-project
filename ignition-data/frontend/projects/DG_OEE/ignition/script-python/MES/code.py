# pylint: disable=consider-using-f-string
"""
MES Helper Functions
"""
#Return a list of MES objects of type 'Line' that are not inactive.
def get_line_list():
	obj_filter = system.mes.object.filter.createFilter()
	obj_filter.setMESObjectTypeName('Line')
	obj_filter.setExcludeInactiveEquipment(True)
	line_list = system.mes.searchMESObjects(obj_filter)
	return line_list 


#Return a List of Cell Names with their States for a given Line
def get_cell_states(line):
	obj_filter = system.mes.object.filter.createFilter()
	obj_filter.setMESObjectTypeName('LineCell')
	line_path = r'Design Group\Sacramento\Information Solutions\%s' % line

	obj_filter.setPrimaryMESObjectPath(line_path)
	
	objs = system.mes.searchMESObjects(obj_filter)

	cell_states = []
	for obj in objs:

		eq_path = obj.getMESObject().getEquipmentPath()
	
		cell_state = system.mes.getCurrentEquipmentStates(eq_path)	
		cell_states.append({'cell_name':obj.getName(),'cell_state':cell_state.values()[0]})
		
	return cell_states
